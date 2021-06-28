#고급 순환층 LSTM, gru

#일반적으로 RNN(기본순환층)은 긴 시퀀스를 학습하기 어렵다.
#시퀀스가 길수록 순환 되는 은닉상태에 담긴 정보가 희석된다.

#LSTM(LONG SHORT-TERM MEMORY)
#LSTM 셀에 4개의 작은 셀이 있음 (가중치 4개)


from tensorflow.keras.datasets import imdb
from tensorflow.python.keras.backend import dropout
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=500)
X_train.shape#(25000,)
Y_train.shape#(25000,)
X_train[0]#문장 하나
len(X_train[0])#218
Y_train[0]#0은 부정 1은 긍정


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

from tensorflow.keras.preprocessing.sequence import pad_sequences
X_train_seq = pad_sequences(X_train,maxlen=100)
X_val_seq = pad_sequences(X_val,maxlen=100)

#분석모델 구축
from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.Embedding(500,16,input_length=100))
model.add(keras.layers.LSTM(8))
model.add(keras.layers.Dense(1,activation='sigmoid'))
model.summary()

#순환신경망 훈련하기
adam = keras.optimizers.Adam(learning_rate=1e-4)
model.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-simplernn-model.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model.fit(X_train_seq, Y_train, epochs=100, validation_data=(X_val_seq,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)



#순환층 드롭아웃 적용하기

model2 = keras.Sequential()
model2.add(keras.layers.Embedding(500,16,input_length=100))
model2.add(keras.layers.LSTM(8,dropout=0.35))
model2.add(keras.layers.Dense(1,activation='sigmoid'))
model.summary()

#순환신경망 훈련하기
adam = keras.optimizers.Adam(learning_rate=1e-4)
model2.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])

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

#------------------------------------------------------------------------------------------------------
#2개의 순환층 연결하기





model3 = keras.Sequential()
model3.add(keras.layers.Embedding(500,16,input_length=100))
model3.add(keras.layers.LSTM(8,dropout=0.4))
model3.add(keras.layers.LSTM(8,dropout=0.3))
model3.add(keras.layers.Dense(1,activation='sigmoid'))
model3.summary()

#순환신경망 훈련하기
adam = keras.optimizers.Adam(learning_rate=1e-4)
model3.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-simplernn-model3.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model3.fit(X_train_seq, Y_train, epochs=100, validation_data=(X_val_seq,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)


import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

#------------------------------------------------------------------------------------------------------------
#GRU신경망 훈련 (gated recurrent unit)
#셀에 3개의 작은 셀이 있음 (가중치 3개)
#GRU는 LSTM보다 학습속도가 빠르다고 알려져 있지만
#LSTM과 비숫한 성능을 보임

#그래도 일반적으로 LSTM을 사용한다
#------------------------------------------------------------------------------------------------------------

model4 = keras.Sequential()
model4.add(keras.layers.Embedding(500,15,input_length=100))
model4.add(keras.layers.GRU(8, dropout=0.4))
model4.add(keras.layers.GRU(8, dropout=0.3))
model4.add(keras.layers.Dense(1,activation='sigmoid'))
model4.summary()

model4.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-simplernn-model4.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model4.fit(X_train_seq, Y_train, epochs=100, validation_data=(X_val_seq,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)

X_test_seq = pad_sequences(X_test, maxlen=100)
gru_model = keras.models.load_model('./best-simplernn-model4.h5')
gru_model.evaluate(X_test_seq,Y_test)
#[0.4324069917201996, 0.800000011920929]


LSTM_model = keras.models.load_model('./best-simplernn-model3.h5')
LSTM_model.evaluate(X_test_seq,Y_test)
#[0.426312655210495, 0.8023200035095215]




































