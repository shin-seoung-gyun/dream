from tensorflow import keras
import numpy as np
#1)데이터 수집 - 패션 minist 이미지 크기 28*28
#10가지 패션 아이템

(X_train, Y_train), (X_test, Y_test) = keras.datasets.fashion_mnist.load_data()
X_train.shape
Y_train.shape
X_test.shape
Y_test.shape

#2)데이터 전처리 및 탐색
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 10, figsize=(10,10))
for i in range(10):
    axs[i].imshow(X_train[i], cmap='gray')
    axs[i].axis('off')
plt.show()

np.unique(Y_train, return_counts=True)
#0티셔츠 1:바지 2:스웨터 3: 드레스 4:코트 5:샌들 6:셔츠 7:스니커즈 8:가방 9:앵클부츠

X_train[0] #0번째 아이템의 데이터

#2-1) 데이터 크기변환
X_train = X_train.reshape(-1,28*28)
X_test = X_test.reshape(-1,28*28)
X_train.shape
X_test.shape

#2-2) 데이터 정규화
#0~255 =>0~1
#표준정규화가 아닌 다른 정규화 사용
#(data-min(data))/(max(data)-min(data))
#(123-0)/(288-0)=123/255
#이미지 데이터에서 많이 사용하는 정규화
X_train_scaled = X_train/255
X_test_scaled = X_test/255

#3)분석모델구축 -확률적 경사하강법(로지스틱회귀)
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log',max_iter=5, random_state=52)
#z_티셔츠 = w1*(픽셀1)+w2*(픽셀2)......+w784(픽셀784)+b
#z_바지 = w1*(픽셀1)+w2*(픽셀2)......+w784(픽셀784)+b
#소프트맥스 함수를 통해서 각 타겟의 확률을 구함.
scores = cross_validate(sc, X_train_scaled,Y_train, n_jobs=-1)
np.mean(scores['test_score'])#0.8228

sc = SGDClassifier(loss='log',max_iter=30, random_state=52)
scores = cross_validate(sc, X_train_scaled,Y_train, n_jobs=-1)
np.mean(scores['test_score'])#0.8397833333333333


#----------------------------------------------------------------------------------------------
#3)분석모델 구축 - 인공신경망
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

#검증데이터 생성
X_train, X_val, Y_train, Y_val = train_test_split(X_train_scaled, Y_train, test_size=0.2, random_state=52)

#뉴런 개수, 뉴런의 출력에 적용할 함수, 입력크기

dense = keras.layers.Dense(10, activation='softmax', input_shape=[X_train.shape[1]])
model = keras.Sequential(dense)
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'] )
model.fit(X_train, Y_train, epochs=5, validation_data=(X_val,Y_val))

model.evaluate(X_test_scaled,Y_test)#[0.4792102575302124, 0.84579998254776]

#활성화 함수 
#(1) 은닉층 : ReLU, Leaky ReLU
#은닉층 개수가 많아지면 입력층에 가까워 질수록 기울기가 0에 가까워 지는 기울기 소실 문제 발생 (학습이 잘 안됨.)
#제대로 학습이 이루어 지지않아, 시그모이드 함수 대신 ReLU함수 주로 사용

#(2) 출력층 : 시그모이드함수(이진분류), 소프트맥스(다중분류), 활성화함수사용안함(회귀)
#

#손실함수 

#이진 크로스 엔트로피(이진분류 - 출력 0,1)
#binary_crossentropy

#범주형 크로스 엔트로피(다중분류 - 출력 : 원핫 인코딩)
#categorical_crossentropy

#희소 범주형 크로스 엔트로피(다중분류 - 출력 : 정수)
#Sparse_categorical_crossentropy

#평균 제곱 오차 (회귀에서)
#mean_squared_error


#옵티마이져 - 가중치와 편향을 찾기위한 방법(학습방법)
#SGD(확률적경사하강법) : 몇몇 샘플을 무작위로 추출하여 일부만 경사하강법을 사용해 학습속도 개선

#RMSProp : 기울기에 따라 학습률 조절

#Momentum : 관성개념을 추가

#Adam : RMSProp,Momentum의 아이디어 합침.



