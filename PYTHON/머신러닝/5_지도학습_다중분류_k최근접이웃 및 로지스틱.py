#----------------------------------------------------------------------------------------------------------------------------------------------
#k-최근접 이웃 다중분류
#샘플 주위에 있는 각각 클래스별(타겟별) 데이터의 개수로
#샘플의 타겟값이 무엇인지 확률로 파악
#----------------------------------------------------------------------------------------------------------------------------------------------


import pandas as pd
import numpy as np
#1)데이터 수집
fish = pd.read_csv("./data/Fish.csv")
fish.info()
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

#3)분석모델 구축
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(X_train_scaled, Y_train)

#4) 모델평가 및 결과 분석
kn.score(X_train_scaled,Y_train)#0.8907563025210085
kn.score(X_test_scaled,Y_test)#0.85

#xptmxm epdlxj 0~4번 예측결과 확인
kn.predict(X_test_scaled[:5])
#array(['Perch', 'Smelt', 'Pike', 'Perch', 'Perch'], dtype=object)

#실제결과
Y_test[:5]#array(['Perch', 'Smelt', 'Pike', 'Whitefish', 'Perch'], dtype=object)

#각 (클래스)타겟 별 확률값 
kn.classes_
proba = kn.predict_proba(X_test_scaled[:5])
np.round(proba,3)

#3번째 데이터의 거리값과 가까운 데이터들의 인덱스 값
distance, indexes = kn.kneighbors(X_test_scaled[3:4])
distance#array([[0.20774583, 0.24862983, 0.33682411]])
indexes#array([[104, 115, 106]], dtype=int64)
X_train_scaled[indexes]
Y_train[indexes]





##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#로지스틱 회귀
#-선형회귀와 동일하게 선형 방정식으로 학습
#ex) z = a*weight+b*length+c*height+f
#z값의 범위는 -무한대~+무한대 => 확률값 (0~1)
#그러기 위해 시그모이드 함수를 취해 확률값으로 바꾼다.
#시그모이드 함수(로지스틱함수) = 1/(1+e^(-z))
#타겟마다 선형방정식이 있어야하고 각 선형방정식마다 확률을 구한다.

#시그모이드 함수 시각화

import numpy as np
import matplotlib.pyplot as plt

z=np.arange(-5,5,0.1)
sig = 1/(1+np.exp(-z))
plt.plot(z,sig)
plt.show()

#이진분류 - 도미(bream), 빙어(smelt)
bream_smelt_indexes = (Y_train=='Bream')|(Y_train=='Smelt')
bream_smelt_indexes
X_train_bs = X_train_scaled[bream_smelt_indexes]
Y_train_bs = Y_train[bream_smelt_indexes]

# #numpy 마스크 인덱싱
# char_arr = np.array(['a','b','c','d','e'])
# char_arr[[True,False,False,False,False]]

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train_bs,Y_train_bs)

#테스트 데이터 도미 빙어 추출
bream_smelt_indexes = (Y_test=='Bream')|(Y_test=='Smelt')
bream_smelt_indexes
X_test_bs = X_test_scaled[bream_smelt_indexes]
Y_test_bs = Y_test[bream_smelt_indexes]

lr.score(X_train_bs,Y_train_bs)
lr.score(X_test_bs,Y_test_bs)

lr.coef_,lr.intercept_
#(array([[-0.4037798 , -0.57620209, -0.66280298, -1.01290277, -0.73168947]]), array([-2.16155132]))
#z = -0.4*weight-0.57*length-0.66*diagonal-1.01*height-0.73*width-2.16

#테스트 데이터 0~4번까지 예측
lr.predict(X_test_bs[:5])
#array(['Smelt', 'Bream', 'Smelt', 'Bream', 'Bream'], dtype=object)
#실 데이터
Y_test_bs[:5]
#array(['Smelt', 'Bream', 'Smelt', 'Bream', 'Bream'], dtype=object)

#예측확률
lr.predict_proba((X_test_bs[:5]))
lr.classes_
# array([[3.95673649e-02, 9.60432635e-01],
#        [9.99418084e-01, 5.81915885e-04],
#        [2.57680368e-02, 9.74231963e-01],
#        [9.94091561e-01, 5.90843851e-03],
#        [9.93797733e-01, 6.20226656e-03]])

#z값을 얻기
decision = lr.decision_function(X_test_bs[:5])
decision
#array([ 3.18937919, -7.44860256,  3.63251459, -5.12544773, -5.0766189 ])

#z값 시그모이드 함수로 취하면
from scipy.special import expit
expit(decision)
# array([9.60432635e-01, 5.81915885e-04, 9.74231963e-01, 5.90843851e-03,
#        6.20226656e-03])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#로지스틱회귀 다중분류
#각 클래스(타겟)마다 선형방정식 생성
#각 클래스 마다 z값을 얻고 소프트맥스 함수를 통해 확률로 변환
#e_sum = e^z1 +e^z2 +...+e^zn
#s1(타겟1의 확률= e^z1/e_sum)
#s2(타겟2의 확률= e^z2/e_sum)
#지수함수를 사용하면 특징들을 부각시킨다.

#로지스틱 회귀 클래스는 기본적으로 반복적인 알고리즘 수행(학습시)
#max_iter 매개변수로 반복횟수 지정, 기본값 100
#L2규제 : 릿지 회귀와 같이 계수의 제곱을 규제함
#규제제어 하이퍼파라미터 c (기본값 1)
#C값이 작을수록 규제가 커진다(릿지회귀의 alpha와 반대)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EX) 7개의 생선 분류
#max_iter = 1000 (그냥 수행하면 경고 메세지 뜸)
#c = 20 (규제 완화)

#모델생성
lr =LogisticRegression(C=20, max_iter=1000)
lr.fit(X_train_scaled, Y_train)

#모델평가
lr.score(X_train_scaled, Y_train)#0.9327731092436975
lr.score(X_test_scaled, Y_test)#0.925


#테스트데이터 0~4번까지 예측
lr.predict(X_test_scaled[:5])
#array(['Perch', 'Smelt', 'Pike', 'Roach', 'Perch'], dtype=object)

#실제값
Y_test[:5]
#array(['Perch', 'Smelt', 'Pike', 'Whitefish', 'Perch'], dtype=object)

#확률값
np.round(lr.predict_proba(X_test_scaled[:5]),2)
lr.classes_

#각 클래스별 선형방정식 계수
lr.coef_#7개
# array([[-1.49003025, -1.02920916,  2.59352663,  7.70353339, -1.20067499],
#        [ 0.19619603, -2.01058441, -3.77984188,  6.50489846, -1.99487383],
#        [ 3.56278059,  6.34362554, -8.48973941, -5.75756019,  3.7930946 ],
#        [-0.10458825,  3.60315886,  3.93067299, -3.61729947, -1.75070954],
#        [-1.40058388, -6.0750575 ,  5.25967252, -0.87223581,  1.8604376 ],
#        [-1.38529379,  1.49218046,  1.39228892, -5.67732313, -4.40095538],
#        [ 0.62151954, -2.32411379, -0.90657977,  1.71598675,  3.69368154]])


lr.intercept_#7개
# array([-0.09204778, -0.26290681,  3.25100913, -0.14741927,  2.65495374,
#        -6.78780461,  1.3842156 ])

#각 클래스별 z 값 얻기
decision = lr.decision_function(X_test_scaled[:5])
np.round(decision,2)

#소프트 맥스를 통한 확률 변환
from scipy.special import softmax
proba = softmax(decision, axis=1)
np.round(proba,2)



