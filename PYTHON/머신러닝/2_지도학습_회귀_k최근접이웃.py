#-----------------------------------------------------------------------------------------------------
#회귀는  데이터를 예측합

#이웃한 샘플의 수치를 사용해 새로운 샘플 X의 타깃을 예측하는 방법으로 이웃한 수치들의 평균을 내어 새오운 타깃 값을 도출

#단점 : 가장 가까운 생플을 찾아 타깃의 평균을 구하므로
#새로운 샘플이 훈련세트의 범위를 벗어나면 잘못된 값을 예측
#-----------------------------------------------------------------------------------------------------------------
# EX)물고기의 길이만 보고 무게를 예측

#1) 데이터 수집
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

#2)데이터 탐색 및 전처리
import matplotlib.pyplot as plt
plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#훈련데이터와 테스트 데이터 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(perch_length, perch_weight, random_state=42)
X_train.shape, X_test.shape
X_train=X_train.reshape(-1,1)#데이터 개수 * 1 의 행렬
X_test=X_test.reshape(-1,1)#데이터 개수 * 1 의 행렬

#3)분석모델구축
from sklearn.neighbors import KNeighborsRegressor#회귀용도
knr=KNeighborsRegressor()
knr.fit(X_train, Y_train)

#4) 모델평가 및 결과 분석
#정확도 : 데스트세트에 있는 타겟을 정확하게 분류한 비율
#결정계수 를 통해 모델성능을 평가
#R^2 - 0~1사잉의 값을 갖고, 1에 가까울수록 모델이 데이터에 잘 들어맞는다.

knr.score(X_test, Y_test) #0.992809406101064

#평균 절대값 오차
#오차값 = |실제값 - 예측값|
from sklearn.metrics import mean_absolute_error
test_prediction = knr.predict(X_test)
test_prediction #예측값
Y_test#실제값

mae = mean_absolute_error(Y_test, test_prediction)
mae #19.157142857142862


#테스트데이터 스코어
knr.score(X_test, Y_test) #0.992809406101064
#훈련데이터 스코어
knr.score(X_train, Y_train)#0.9698823289099254
##과소적합으로 인해 테스트 데이터가 R^2가 더 크다.

#과대적합과 과소적합
#과대적합 : 훈련세트에서 점수가 좋게 나왔는데,테스트세트에서 점수가 나쁜경우
#모델이 너무 복잡하거나 테스트 데이터에 너무나 맞춰져있어 새로운 데이터의 예측성능이 떨어짐
#해결책 => K최근접 이웃의 k개수를 늘림.

#과소적합 : 훈련세트보다 테스트 세트의 점수가 높거나
#두 점수 모두가 낮은 경우
#모델이 단순하거나, 훈련데이터 양이 부족하여 학습이 잘 이루어 지지 않음
#해결책 => k최근접 이웃의 k개수를 줄임,
#또는 훈련 데이터를 늘림


#과소적합 해결
#k를 줄이기

knr.n_neighbors = 3
knr.fit(X_train, Y_train)
knr.score(X_train, Y_train)#0.9804899950518966
knr.score(X_test, Y_test)#0.9746459963987609

#k값에 따라서 예측 모델 시각화
knr = KNeighborsRegressor()
#예측 데이터
x = np.arange(5,45).reshape(-1,1)

#k=1,5,10일때 예측 결과 시각화
for k in [1,5,10] :
    knr.n_neighbors = k
    knr.fit(X_train, Y_train)
#예측값 얻기
    prediction = knr.predict(x)
    plt.scatter(X_train, Y_train)
    plt.plot(x, prediction)
    plt.title(f'n_neighbors={k}')
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()

#---------------------------------------------------------------------------------------------------------------------------------------
#k최근접 이웃 회귀의 한계(문제점)
X_train.max(),X_train.min()#(44.0, 13.7)

newData = [50]
plt.scatter(X_train,Y_train)
prediction = knr.predict([newData])
plt.scatter(newData, prediction, marker='^')
plt.show()

