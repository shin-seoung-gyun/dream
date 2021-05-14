from statsmodels.formula.api import ols
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

data_df = pd.read_csv("./머신러닝/auto-mpg.csv", header=0, engine='python')#데이터 프레임에 저장
#저장 확인
# print(data_df.head())
# print(data_df.info())


#분석하지 않을 변수 제외하기
data_df = data_df.drop(['car_name','origin','horsepower'], axis=1, inplace=False)#열 기준으로 삭제
#삭제 확인
# print(data_df.head())

print()
print("데이터 결측치 합계 출력")
print()
print(data_df.isna().sum()) #데이터 결측치 합계 출력
print()




##데이터 상관분석 히트맵으로 시각화
#히트맵에 사용할 데이터를 추출
heatmap_data = data_df[['mpg','cyilnders','weight','acceleration','model_year','displacement']]
#히트맵에 사용할 색상맵 지정
colorMap = plt.cm.RdBu
#corr() 함수로구한 상관 계수로 히트맵 생성
sns.heatmap(heatmap_data.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap = colorMap, linecolor='white', annot = True, annot_kws={'size':10})
plt.show()




##선형회귀 분석모델
Rformula = 'mpg~'+'+'.join(data_df.columns[1:])
# print(Rformula)

#선형회귀 모델 중 ols모델 사용
regression_result = ols(Rformula, data=data_df).fit()
print("생성된 모델 요약 정보")
print()
print(regression_result.summary())## 생성된 모델 요약 정보



##선형회귀 모델 그래프로 만들기
#독립변수와 종속변수를 제외한 나머지 변수 이름 추출
import statsmodels.api as sm

fig = plt.figure(figsize=(8,13))
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.show()




##회귀 분석 모델을 통한 새로운 샘플의 연비예측
data = {"cyilnders":[8],"displacement":[310],"weight":[3000],"acceleration":[11],"model_year":[85]}
#연비예측
data_predict = regression_result.predict(data)
print()
print("예측된 연비값")
print(data_predict)
print()



