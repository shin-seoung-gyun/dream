#머신러닝 프로세스
#데이터 수집 -> 데이터 전처리 및 탐색 -> 훈련데이터/테스트데이터 분할 -> 모델 구축및 학습-> 모델평가 -> 모델예측
#머신러닝 - 지도학습(데이터의 결과값이 있어야함) 
# 선형회귀분석(예측),로지스틱회귀분석(분석),결정트리모델(다중분류)
# 비지도 학습(데이터만 가지고 학습)
#k-means 군집 (비슷한 데이터들 끼리 군집화 시켜준다)
#소비자 유형 분석

#사이킷런 라이브러리 - 머신러닝 대표적인 라이브러리
#보스턴 집값, 붓꽃(아이리스), 당뇨병환자 데이터

#1) 데이터 수집
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()

#2)데이터 전처리 및 탐색
print(boston.DESCR)
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(boston_df.head())
boston_df['PRICE']=boston.target
print(boston_df.info())

#3)분석모델 구축 - 선형회귀분석
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#x(독립변수), y(종속변수-결과) 데이터 나누기
Y = boston_df['PRICE']
X = boston_df.drop(['PRICE'], axis=1, inplace=False)

#훈련용 데이터와 평가용 데이터 분할(7:3)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=156)

#선형회귀분석 : 모델 생성
lr = LinearRegression()
#모델훈련
lr.fit(X_train,Y_train)
#평가데이터에 대한 예측 수행
Y_predict = lr.predict(X_test)
for i in range(len(Y_test)) :
    print(Y_test.iloc[i], Y_predict[i])

#4)모델 성능평가
mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)
print(f'MSE:{mse:>0.3}, RSME:{rmse:>1.3}')
print(f'R^2(Variance score): {r2_score(Y_test, Y_predict)}')

print("회귀 계수 값 :", np.round(lr.coef_,1))
print("Y 절편 값 : ", np.round(lr.intercept_,1))
coef = pd.Series(data=np.round(lr.coef_,1),index=X.columns)
coef.sort_values(ascending=False)
print(coef)

#5) 결과분석 시각화-회귀분석결과 산점도 그래프
import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize=(16,16), ncols=3,nrows=5)
x_features=list(X.columns)
for i, feature in enumerate(x_features):
    row = int(i/3)
    col =i%3
    sns.regplot(x=feature, y="PRICE",data=boston_df, ax=axs[row][col])
plt.subplots_adjust(hspace=0.4)
plt.show()











