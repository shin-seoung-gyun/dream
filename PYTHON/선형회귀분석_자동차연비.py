
import numpy as np
import pandas as pd

# 1) 데이터 수집 - 자동차 연비

data_df = pd.read_csv("./머신러닝/auto-mpg.csv", header=0, engine='python')


#2) 데이터 탐색
print("데이터 셋 크기 : ", data_df.shape)
print(data_df.head())
print(data_df.info())
# print(data_df.isna().sum()) 각 열별로 결측치 확인

#분석하지 않을 변수 제외하기
data_df = data_df.drop(['car_name','origin','horsepower'], axis=1, inplace=False)#열 기준으로 삭제, 본 데이터는 없에지 않음 axis 0 인덱스 기준으로 삭제됨
print(data_df.head())

## 3) 분석모델 구축 - 선형회귀모델 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#X,Y데이터 분할 - Y 연비 ,X(배기량 ....)
Y = data_df['mpg']
X = data_df.drop(['mpg'],axis=1,inplace=False)

#훈련용 데이터와 테스트용 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=0)#언패킹 방식 파이선에서만 가능

#선형회귀모델 생성 및 학습
lr = LinearRegression()
lr.fit(X_train, Y_train)#모델 학습

#모델 예측및 평가
Y_predict = lr.predict(X_test)
for i in range(len(Y_test)):
    print(Y_test.iloc[i], Y_predict[i])#Y_test는 데이터 프레임구조라 iloc로 가져와야함 Y_predict는 리스트구조라 그냥 가져옴

#모델 성능평가
mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(f"MSE:{mse:>0.3},RMSE:{rmse:>0.3}")
print(f"R^2(Variance Score):{r2_score(Y_test,Y_predict):>0.3}")

print("회귀계수값 : ", np.round(lr.coef_,1))
print("Y절편값 : ", np.round(lr.intercept_,1))
coef = pd.Series(data=np.round(lr.coef_,1), index=X.columns)
coef.sort_values(ascending=False,inplace=True)
print(coef)

# 5) 결과분석 시각화 - 회귀분석결과 산점도 그래프
import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize=(16,16),ncols=3,nrows=2)
x_features = list(X_train.columns)
plot_color = ['r','b','y','g','m']
for i, feature in enumerate(x_features):
    row = int(i/3)
    col = i%3
    sns.regplot(x=feature, y='mpg',data=data_df, ax = axs[row][col], color= plot_color[i])
plt.show()








