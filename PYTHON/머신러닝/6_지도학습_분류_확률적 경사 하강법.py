#딥러닝에서 필수로 사용하는 알고리즘
#일반적인 학습 방법 : 전체 데이터를 불러와서 학습
#단점 : 컴퓨터의 자원을 많이 소모, 학습 속도가 느리다.

#점진적 학습방법 : 일부 데이터를 불러와서 학습
#경사 하강법이 대표적

#경사하강법
#최적의 해를 찾기 위해서 함수의 기울기를 이용하여 가중치를 업데이트 하는 방법
#오차 함수(손실함수)의 미분값이 0인 지점 찾기
#오차 함수의 기울기를 구하고 가중치를 계속 업데이트하여 미분값이 가장 작은 지점에 이를때 까지 반복

#확률적 경사하강법
#전체 데이터 중 하나의 랜덤한 샘플 데이터를 통해 경사하강법 진행

#손실함수
#머신러닝 알고리즘의 얼마나 부정확한지 척도 (오차척도)
#평균 제곱오차와 교차엔트로비 오차등을 사용
#평균제곱오차 =mean((예측값=실제값)^2)
#

#에포크(epoch)
#훈련세트에 샘플 데이터를 채워 넣고 훈련 세트를 한번 모두 사용하는 과정을 에포크
#일반적으로 경사 하강법은 수십, 수백 번 이상의 에포크 수행

#미니매치 경사 하강법
#1개의 샘플데이터가 아닌 무작위 몇개의 샘플데이터를 선택해 경사하강법 진행

#배치 경사하강법
#모든데이터를 사용해서 경사하강법으로 훈련
#가장 안정적인 방법이 될수 있지만, 컴퓨터 자원 소모가 큼

#1) 데이터 수집
import pandas as pd
fish = pd.read_csv('./data/Fish.csv')

fish.head()

#2)데이터 탐색및 전처리
#물고기 종 확인
pd.unique(fish['Species'])
#array(['Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt'],

#훈련데이터 생성
X_train = fish[fish.columns[1:]].to_numpy()
X_train.shape#(159, 5) 159개 데이터 5개의 특성

#타겟 데이터
Y_train = fish['Species'].to_numpy()

#훈련데이터, 테스트 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_train,Y_train,random_state=42)

#데이터 정규화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)

#3) 분석모델구축 - 확률적 경사하강법
from sklearn.linear_model import SGDClassifier#분류
#손실함수 log(로지스틱 손실함수) - 기본값은 hinge(서포트벡터머신의 손실함수)
#max_iter 에포크 횟수 10, 전체 훈련세트를 10회 반복
#전달한 훈련세트에서 1개씩 랜덤으로 샘플을 꺼내어 경사하강법 수행

sc = SGDClassifier(loss='log', max_iter=10, random_state=42)
sc.fit(X_train_scaled,Y_train)

#4) 모델평가 및 결과분석
sc.score(X_train_scaled, Y_train)#0.773109243697479
sc.score(X_test_scaled, Y_test)#0.775
#과소적합 -> 훈련을 더 많이 시키면 된다.

#모델 재학습
#확률적 경사하강법은 점진적 학습이 가능하다.

#기존 훈련된 모델에서 1에포크씩 이어서 훈련
sc.partial_fit(X_test_scaled, Y_test)
sc.score(X_train_scaled, Y_train)#0.773109243697479
sc.score(X_test_scaled, Y_test)#0.775
#여전히 과소적합

##########################################
#최적의 에포크 찾기
import numpy as np
sc = SGDClassifier(loss='log', random_state=42)
train_score = []
test_score = []
classes = np.unique(Y_train)

#partial fit만으로 모델훈련
for _ in range(0,300) :
    sc.partial_fit(X_train_scaled, Y_train, classes=classes)
    train_score.append(sc.score(X_train_scaled,Y_train))
    test_score.append(sc.score(X_test_scaled,Y_test))

#에포크에 따른 점수 시각화
import matplotlib.pyplot as plt
plt.plot(np.arange(1,301), train_score, label='train')
plt.plot(np.arange(1,301), test_score, label='test')
plt.xlabel('epoch')
plt.ylabel('score')
plt.legend()
plt.show()
#############################################

#최적 에포크 100으로 선정
#tol : 정확도, 반복시 이 값보다 감소되지 않을 경우 반복중단.
sc = SGDClassifier(loss='log', max_iter=100, random_state=42, tol=None)
sc.fit(X_train_scaled,Y_train)
sc.score(X_train_scaled, Y_train)#0.957983193277311
sc.score(X_test_scaled, Y_test)#0.925













































































