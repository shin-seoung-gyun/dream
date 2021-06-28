#--------------------------------------------------------------------------------------------
#FNN(피드포워드 신경망) = 데이터의 흐름이 앞으로만 전달되는 신경망 EX) cnn,dnn
#하나의 샘플을 사용하여계산을 수행하고 나면 그 샘플은 버려지고, 다음 샘플을 처리할때 재사용 하지 않음

#RNN(순환신경망) : 뉴런의 출력이 다시 자기 자신으로 전달되어
#이전의  정보가 입력에 들어옴

#타임스텝 : 샘플을 처리하는 한 단계
#순환 신경망은 이전 타임스텝의 샘플을 기억하지만 타임스텝이 오래될수록
#순환되는 정보는 희미해진다

#은닉층의 활성화 함수로 tanh(하이퍼볼린 탄젠트)가 주로 사용
#-1~1 사이의 값을 갖는다.

#--------------------------------------------------------------------------------------------
#EX)imdb 에서 수집한 영화리뷰 분류
from tensorflow.keras.datasets import imdb
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=500)
#num_words : 자주 등장하는 단어 지정한 수 만큼 사용
#전체 어휘 사전에 있는 단어를 등장 횟수 순서대로 나열한 다음
#가장 많이 등장하는 500개의 단어 선택

X_train.shape#(25000,)
Y_train.shape#(25000,)
X_train[0]#문장 하나
len(X_train[0])#218
Y_train[0]#0은 부정 1은 긍정
#텍스트 데이터의 경우 단어를 숫자데이터로 바꿔처리 해야 한다.
#일반적인 방법으로 단어마다 고유한 정수 부여
#(명의척도, 숫자사이에 대소관계 무의미)
#영어의 경우 단어를 모두 소문자로 바꾸고 구둣점이나 특수문자 제외한 다음
#공백을 기준으로 분리
#토큰 : 분리된 단어수 ex) 한 문장에 단어가 10개 나오면 토큰 10
#1개의토큰이 하나의 타임스탬프에 해당이 된다.
#500개 어휘 사전에 없는 단어는 모두 2로 표시(텐서플로우에서 처리해줌)

#훈련/검증 세트 분리
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(X_train,Y_train, test_size=0.2, random_state=32)

#훈련세트 조사
#리뷰의 토큰 길이 평균, 중앙값 구하기
import numpy as np
lengths = np.array([len(x) for x in X_train])
np.mean(lengths), np.median(lengths)
# (238.71364, 178.0)

#단어 수 분포도 확인
import matplotlib.pyplot as plt
plt.hist(lengths)
plt.xlabel('length')
plt.ylabel('freq')
plt.show()


#100rodml 토큰만 사용, 100보다 작은리뷰는 패딩.
#100보다 크면 샘플이 잘림
#옵션에 따라 샘플의 앞의 부분이 잘릴지 뒷부분이 잘릴지 선택 가능
#truncating 매개변수 'pre' 이면 앞, 'post'이면 뒤

from tensorflow.keras.preprocessing.sequence import pad_sequences
X_train_seq = pad_sequences(X_train,maxlen=100)
#truncating 디폴트 값으로 'pre'
X_train_seq.shape#25000,100
X_train_seq[0]
X_train[0]
#앞부분이잘림
X_train_seq[5]
#100개보다 작은 문장은 앞부분이 0으로 채워짐

#검증세트 길이 100
X_val_seq = pad_sequences(X_val,maxlen=100)

#모델구축
from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.SimpleRNN(8,input_shape=(100,500)))#원핫 인코딩을 위해 500을 넣음
#100은 토큰 , 500은 단어의 총수가 500이니 한단어를 원핫 인코딩으로 바꾸기 위한 배열의 크기
# 출력층
model.add(keras.layers.Dense(1, activation='sigmoid')) 

X_train_oh = keras.utils.to_categorical(X_train_seq)
X_train_oh.shape#(25000, 100, 500)

X_val_oh =  keras.utils.to_categorical(X_val_seq)
model.summary()
#4072
#입력 데이터의 크기 : 500
#500*8 =4000개(일반 가중치) + 8*8=64개(순환되는 가중치) + 8개*절편

#순환신경망 훈련하기
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-simplernn-model.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model.fit(X_train_oh, Y_train, epochs=100, validation_data=(X_val_oh,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)



import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('accuracy')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

X_test_seq = pad_sequences(X_test,maxlen=100)
X_test_oh =  keras.utils.to_categorical(X_test_seq)
model.evaluate(X_test_oh,Y_test)#[0.4477943480014801, 0.7930399775505066]

#원핫 인코딩 단점 = 토큰 1개를 500차원으로 늘렸기에, 대략 데이터가 500배 커짐

#-----------------------------------------------------------------------------------------------------------

#단어 임베딩 : 각 단어를 고정된 크기의 실수 벡터로 바꿔준다.
#원-핫 인코딩 벡터보다 훨씬 의미있는 값으로 채워져 있기에
#좋은 성능을 내는 경우가 많다.
#모든 벡터가 랜덤하게 초기화 되지만, 훈련을 통해 데이터에 좋은 단어
#임베딩을 학습

#입력으로 정수 데이터를 받는것이 장점

model2 = keras.Sequential()
model2.add(keras.layers.Embedding(500,16,input_length=100))
#500은 총 단어 수, 16은 임베딩 벡터의 크기
model2.add(keras.layers.SimpleRNN(8))
model2.add(keras.layers.Dense(1,activation='sigmoid'))
model2.summary()

rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model2.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-simplernn-model2.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model2.fit(X_train_seq, Y_train, epochs=100, validation_data=(X_val_seq,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)



import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('accuracy')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

#출력결과 = 원핫인코딩과 비슷한 성능
#순환층의 가충지 개수는 훨씬 작고, epoch의 크기도 줄음 단어 임베딩이 조금더 좋다

