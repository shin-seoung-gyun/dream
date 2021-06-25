#다중회귀 - 여러 개의 특성을 사용한 선형 회귀

#특성이 1개일때 선형 회귀모델이 학습하는 것은 직선
#특성이 2개일때는 평면
#특성이 3개일때는 입방체

#특성 공학 : 기존의 특성을 사용해서 새로운 특성을 뽑아 내는 작업
#EX)새로운 데이터 = 농어의 길이 * 농어의 높이


#1)데이터 수집
import pandas as pd
import numpy as np
df = pd.read_csv('./data/perch_full.csv')
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
df.head()
df.info()
perch_full = df.to_numpy()
perch_full

#훈련/테스트 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(perch_full, perch_weight, random_state=42)

#사이킷런의 변환기
from sklearn.preprocessing import PolynomialFeatures#변환기

poly = PolynomialFeatures()
poly.fit([[2,3]])
poly.transform([[2,3]])
#array([[1., 2., 3., 4., 6., 9.]])

#절편항은 제외 시키고, degree로 차수까지 변경가능
poly = PolynomialFeatures(degree=3, include_bias=False)
poly.fit([[2,3]])
poly.transform([[2,3]])

# array([[ 2.,  3.,  4.,  6.,  9.,
#   8., 12., 18., 27.]])

poly = PolynomialFeatures(include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_train_poly.shape#(42, 9) a,b,c, a^2, b^2, c^2,a*b,a*c,b*c
poly.get_feature_names()#['x0', 'x1', 'x2', 'x0^2', 'x0 x1', 'x0 x2', 'x1^2', 'x1 x2', 'x2^2']

X_test_poly = poly.transform(X_test)

#3)분석모델 구축
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train_poly, Y_train)
#


#4)모델 평가 및 결과분석
lr.score(X_train_poly, Y_train)#0.9903183436982124
lr.score(X_test_poly, Y_test)#0.9714559911594087
#과소적합 문제 해결
lr.fit(X_train, Y_train)##피쳐 추가 전
lr.score(X_train, Y_train)#0.9559326821885706
lr.score(X_test, Y_test)#0.8796419177546368

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#규제를 통해 과대적합 방지
#규제 - 머신러닝 모델이 훈련 세트를 너무 과도하게 학습하지 못하도록 훼방하는 것

#선형회귀 모델의 경우 특성에 곱해지는 계수(기울기)의 크기를 작게 만드는 일

#릿지와 라쏘 - 선형회귀 모델에서 규제를 추가한 모델방법
#릿지 : 계수를 제곱한 값을 기준으로 규제를 적용
#라쏘 : 계수의 절댓값을 기준으로 규제를 적용
#일반적으로 릿지를 많이 씀

#규제를 적용하기전에 특성들을 정규화 시켜야한다.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#데이터 정규화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)

X_train_scaled.mean(axis=0)#v평균 0
X_train_scaled.std(axis=0)#표준편차 1

#릿지 회귀 모델 구축
from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(X_train_scaled, Y_train)
ridge.score(X_train_scaled,Y_train)#0.9857915060511934
ridge.score(X_test_scaled,Y_test)#0.9835057194929057

#규제 파라미터 - 알파
#규제 량 조절 - alpha 매개편수 (기본값 1.0)
#alpha값이 크면 규제 강도가 커짐. 계수값을 더 줄이고
#과소적합되도록 유도됨

#alpha값이 작으면 계수를 줄이는 역할이 줄어들고 과대적합될 가능성이 커짐

#하이퍼파라미터 : 머신러닝 모델이 학습할수 없고 사람이 지정하는 파라미터

#적절한 alpha값 찾기 - score값(R2)에 대한 시각화
#alpha값 바꿔가면서 최적의 스코어 값을 확인
import matplotlib.pyplot as plt
train_score=[]
test_score=[]

alpha_list=[0.001,0.01,0.1,1,10,100]
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_scaled, Y_train)
    train_score.append(ridge.score(X_train_scaled,Y_train))
    test_score.append(ridge.score(X_test_scaled,Y_test))

plt.plot(np.log10(alpha_list), train_score, label='train')
plt.plot(np.log10(alpha_list), test_score, label='test')
plt.xticks(np.log10(alpha_list),labels=alpha_list)
plt.xlabel("alpha")
plt.ylabel("score")
plt.legend()
plt.show()

#테스트 점수가 가장 높은 alpha값 최종 0.1로 선택
ridge = Ridge(alpha=0.1)
ridge.fit(X_train_scaled, Y_train)
ridge.score(X_train_scaled, Y_train)#0.9889354346720892
ridge.score(X_test_scaled, Y_test)#0.9856564835209135





