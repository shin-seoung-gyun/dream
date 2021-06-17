#-------------------------------------------------------------------------------------------------
#머신러닝 프로세스 : 데이터 수집 -> 데이터 전처리 및 탐색 -> 분석모델구축 -> 모델평가및 결과 분석
# 
# k-최근접 이웃 알고리즘 
# 어떤 데이터에 대한 답을 구할 때 주위의 다른 데이터를
# 보고 다수를 차지하는 것을 정답을 사용
# 새로운 데이터에 대해 예측할 때는 가장 가까운 거리에 
# 어떤 데이터가 있는지 보고 데이터들 간의 값을 평균 냄
# 
# 단점 - 데이터가 아주 많은 경우 사용하기 어려움
# 메모리 많이 필요, 직선거리 계산에 많은 시간 소요
# 
# 소규모 데이터셋에 적합한 모델 
#-------------------------------------------------------------------------------------------------
#1) 데이터 수집(캐글)
#생선 길이에 따른 생선의 분류

#도미 데이터 준비 (35개)
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

#빙어 데이터 준비 (14개)
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

#2)데이터 전처리 및 탐색 과정
import matplotlib.pyplot as plt
plt.scatter(bream_length,bream_weight, label='bream')
plt.scatter(smelt_length,smelt_weight, label='smelt')
plt.xlabel('length')
plt.ylabel('weight')
plt.grid(True)
plt.legend()
plt.show()



##데이터 병합
length = bream_length+smelt_length
weight =  bream_weight+smelt_weight
fish_data = [[l,w]for l,w in zip(length,weight)]
fish_data

#타겟데이터 생성 - 도미 1 , 빙어 0
fish_target = [1]*35 + [0]*14


#3)분석모델구축
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

#훈련및 테스트 데이터 분할
import random
random.seed(0)
random.shuffle(fish_data)
random.seed(0)
random.shuffle(fish_target)

X_train = fish_data[:int(len(fish_data)*0.7)]
Y_train = fish_target[:int(len(fish_target)*0.7)]

X_test = fish_data[:int(len(fish_data)*0.7):]
Y_test = fish_target[:int(len(fish_target)*0.7):]

##다른방식으로 나누기
from sklearn.model_selection import train_test_split
#test_size 인수로 비율 조정 가능 기본 0.25 random_state시드값과 같음

X_train,X_test,Y_train,Y_test = train_test_split(fish_data, fish_target, random_state=42)


#모델 훈련
kn.fit(X_train,Y_train)

#4)모델 평가 및 결과 분석

#정확도
kn.score(X_test,Y_test)#1.0



#새로운 데이터 예측
newFish_len = 30
newFish_weight = 600

plt.scatter(bream_length,bream_weight, label='bream')
plt.scatter(smelt_length,smelt_weight, label='smelt')
plt.scatter(newFish_len, newFish_weight, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.grid(True)
plt.legend()
plt.show()

#예측
kn.predict([[newFish_len, newFish_weight]])
#array([1]) 도미 예측

#모델 다시만들어서 가까운 몇개의 데이터로 판단할지 정하게 할수 있음
#기본값 5
kn20 = KNeighborsClassifier(n_neighbors=20)
kn20.fit(fish_data,fish_target)
kn20.score(fish_data, fish_target)
#0.9795918367346939 정확도 내려감

#---------------------------------------------------------------------------------------------------
#KNeighborsClassifier 파라미터 종류 정리(하이퍼파라미터)
#n_neighbors : 이웃의 개수 지정 (기본값 5)
#p : 거리 재는 방법 지정( 1: 맨허튼 거리, 2: 유클리디안 거리, 기본값 2)
#n_jobs : cpu코어 지정(-1:모든코어 사용, 기본값 1)
#---------------------------------------------------------------------------------------------------

#새로운 데이터 추가예측
newFish_len = 25
newFish_weight = 150

plt.scatter(bream_length,bream_weight, label='bream')
plt.scatter(smelt_length,smelt_weight, label='smelt')
plt.scatter(newFish_len, newFish_weight, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.grid(True)
plt.legend()
plt.show()
#예측
kn.predict([[newFish_len, newFish_weight]])#array([0]) 빙어로 예측 (그래프상으로는 도미가 맞음) 데이터 표준화 작업을 해야 올바른 비교를 함.

#-----------------------------------------------------------------------------------------------------------
#데이터 표준화
import numpy as np
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

X_train_scaled= (X_train-mean)/std#Z표준화

plt.scatter(X_train_scaled[:,0],X_train_scaled[:,1], label='bream')
newData = ([newFish_len, newFish_weight]-mean)/std
plt.scatter(newData[0],newData[1],marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.grid(True)
plt.legend()
plt.show()
#다시 모델훈련

kn.fit(X_train_scaled, Y_train)

#테스트 데이터 표준화
X_test_scaled = (X_test-mean)/std

#정확도
kn.score(X_test_scaled,Y_test)

#새로운 물고기 예측
kn.predict([newData])


