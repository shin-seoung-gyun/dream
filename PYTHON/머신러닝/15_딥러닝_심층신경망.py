from tensorflow import keras
import numpy as np

#1) 데이터 수집 - 패션 MINIST 이미지 크기 28*28
#10가지 패션 아이템

(X_train, Y_train), (X_test, Y_test) = \
        keras.datasets.fashion_mnist.load_data()

#2) 데이터 전처리 및 탐색
#2-1) 데이터 크기 변환
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)
X_train.shape #(60000, 784)


#2-2) 데이터 정규화
#0~255 => 0~1
#(data-min(data))/(max(data)-min(data))
#(123-0)/(255-0) =  123/255
X_train_scaled = X_train/255
X_test_scaled = X_test/255

#2-3) 검증데이터 생성
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(
        X_train_scaled, Y_train, test_size=0.2, random_state=42)

#3) 모델구성하기 - 2개의 은닉층
dense1 = keras.layers.Dense(100, activation='relu',
    input_shape = [X_train.shape[1]])
dense2 = keras.layers.Dense(10, activation='softmax')
model = keras.Sequential([dense1, dense2])
model.summary() #78500, #1010
#dense1 파라미터 개수 784*100+100 = 78500
#dense2 파라미터 개수 100*10+10 = 1010

#층을 추가하는 다른 방법
model = keras.Sequential()
from keras.layers import Dense
model.add(Dense(100, activation='relu'), 
    input_shape = [X_train.shape[1]])
model.add(Dense(10, activation='softmax'))

#3-2) 모델 학습과정 설정
model.compile(optimizer='adam', 
    loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#3-3) 모델 학습
hist = model.fit(X_train, Y_train, epochs=10, 
                validation_data=(X_val, Y_val))
#accuracy: 0.8637 - val_loss: 0.4280 - val_accuracy: 0.8507

#4) 모델 평가 및 결과 분석
hist.history['accuracy']
import matplotlib.pyplot as plt
plt.plot(hist.history['accuracy'], label='acc', ls='-')
plt.plot(hist.history['val_accuracy'], label='val_acc', ls='-')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend()
plt.show()

loss_and_metrics = model.evaluate(X_test_scaled,Y_test)
loss_and_metrics
# [0.44790777564048767, 0.8436999917030334]
#----------------------------------------------------------------------------------------------------------------
#옵티마이저
#신경망 하이퍼파라미터 : 은닉층의 개수, 뉴런 개수, 활성화 함수, 층의 종류(밀집층, CNN등), 배치사이즈, 에포크 수
#옵티마이저 : compile 메서드에서 케라스의 기본 경사 하강법 알고리즘 RMSprop사용
#
#SGD확률적 경사하강법 사용
#자동 객체 생성
model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics='accuracy')

#객체생성
sgd = keras.optimizers.SGD()
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics='accuracy')

#옵티마이저 파라미터
sgd = keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics='accuracy')

#모멘텀 최적화, 0.9이상을 사용
#nesterov(네스테로프 모멘텀 최적화) : 모멘텀 최적화를 2번 반복 구현
sgd = keras.optimizers.SGD(learning_rate=0.1, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics='accuracy')

#적응적 학습률 : 모델이 최적점에 가까워 질수록 학습률을 낮춰서 학습
#=> 안정적으로 수렴함
adagrad = keras.optimizers.Adagrad()
model.compile(optimizer=adagrad, loss='sparse_categorical_crossentropy', metrics='accuracy')


#adam 모멘텀 최적화와 RMSprp의 장점 접목
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
