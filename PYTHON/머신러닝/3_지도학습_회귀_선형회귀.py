#---------------------------------------------------------------------------------------------------------------------
#k-최근접이웃의 한계는 새로운 데이터가 훈련데이터의 범위를 벗어나면예측을 잘 못함.

#선형회귀 - 대표적인 회귀 알고리즘
#모델이 비교적 간단하고 성능이 뛰어남.


#1) 데이터 수집
from os import linesep
import numpy as np
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 
     1000.0, 1000.0]
     )

#2) 데이터 탐색 및 전처리
#훈련데이터와 테스트 데이터 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(perch_length, perch_weight, random_state=42)
X_train.shape, X_test.shape
X_train=X_train.reshape(-1,1)#데이터 개수 * 1 의 행렬
X_test=X_test.reshape(-1,1)#데이터 개수 * 1 의 행렬


#3)분석모델구축
from sklearn.linear_model import LinearRegression#선형회귀
lr=LinearRegression()

#모델 훈련
lr.fit(X_train, Y_train)

#4) 모델 평가 및 결과 분석
lr.score(X_train, Y_train)#0.9398463339976041
lr.score(X_test, Y_test)#0.824750312331356

#과대적합
lr.coef_,lr.intercept_
#(array([39.01714496]), -709.0186449535474)

prediction=lr.predict([[50]])#array([1241.83860323])

#결과 시각화
import matplotlib.pyplot as plt
plt.scatter(X_train, Y_train)

#회귀선 그리기
plt.plot([15,50], [15*lr.coef_+lr.intercept_,50*lr.coef_+lr.intercept_])

#50cm 농어
plt. scatter(50, prediction, marker='^')
plt.show()


#-----------------------------------------------------------------------------------------------------------------------------
#다항회귀 - 독립변수가 2개 이상

#데이터 추가
#길이 제곱 추가
X_train_poly = np.column_stack((X_train**2, X_train))
X_train_poly
#기존의 데이터로 새로운 데이터를 만드는 작업 - 특성공학
#독립변수 - 특성(feature)
#종속변수 - 목표(target)
X_test_poly= np.column_stack((X_test**2, X_test))

lr = LinearRegression()
lr.fit(X_train_poly, Y_train)

lr.score(X_train_poly, Y_train)#0.9706807451768623
lr.score(X_test_poly, Y_test)#0.9775935108325121

#과소적합 (기본적으로 트레이닝 데이터의 적합도가 더 높아야 정상. 너무 차이나면 과대적합)

lr.coef_,lr.intercept_#회귀계수값과 절편값
#(array([  1.01433211, -21.55792498]), 116.05021078278259)
#무게=1.01*길이^2  -21.6*길이 + 116.05

#2차방정식도 선형회귀처럼 변환됨.
#무게=1.01*길이제곱  -21.6*길이 + 116.05

#시각화
xpoint = np.arange(15,50)
#회귀곡선
plt.plot(xpoint, 1.01*xpoint**2-21.6*xpoint+116.05)
#훈련데이터 산점도
plt.scatter(X_train, Y_train)
#50cm 농어 산점도
prediction = lr.predict([[50**2,50]])
plt.scatter([50],[prediction],marker='^')
plt.show()

#과소적합문제 해결
#=> 훈련 데이터 양을 늘리거나 , 모델 복잡하게 만들기
#물고기의 길이, 높이 , 두께 데이터 추가
#무게 예측
























