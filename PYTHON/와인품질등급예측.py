##와인의 속성을 이용해서 품질등급 예측
##데이터분석 방법 : 기술통계. 회귀분석, t-검정
##시각화 : 히스토그램
from os import sep
import pandas as pd
red_df = pd.read_csv("./데이터분석/winequality-red.csv", sep=';',header=0, engine='python')

white_df = pd.read_csv("./데이터분석/winequality-white.csv", sep=';',header=0, engine='python')

#와인정보 합치기
red_df.insert(0, column='type', value='red')
white_df.insert(0, column='type', value='white')
wineDf = pd.concat([red_df,white_df])

# print(wineDf.info())#열정보 요약
# print(wineDf.head())#인자값이 없을때 5개의 정보를 보여준다
# print(wineDf.shape)#행개수 열개수

##기술 통계 구하기
#칼럼 문자열 중 띄어쓰기 있으면 '_'로 바꿈
wineDf.columns = wineDf.columns.str.replace(' ','_')
wineDf.to_csv("wine.csv",index=False)
# print(wineDf.head())
# print(sorted(wineDf.quality.unique()))
# print(wineDf.quality.value_counts())

# print(wineDf.groupby('type')['quality'].mean())
# print(wineDf.groupby('type')['quality'].std())
# print(wineDf.groupby('type')['quality'].agg(['mean','std']))

# print(wineDf.groupby('type')['quality'].describe())

#t검정 - 그룹간 차이가 있는지 비교
red_wine_quality = wineDf.loc[wineDf['type']=='red','quality']
white_wine_quality = wineDf.loc[wineDf['type']=='white','quality']
# print(red_wine_quality)
# print(white_wine_quality)
from scipy import stats
from statsmodels.formula.api import ols, glm
tResult = stats.ttest_ind(red_wine_quality,white_wine_quality,equal_var=False)
print(tResult)##pvalue가 0.05미만이면 유의미하다

##선형회귀 분석모델
Rformula = 'quality~'+'+'.join(wineDf.columns[1:-1])
print(Rformula)
#선형회귀 모델 중 ols모델 사용
regression_result = ols(Rformula, data=wineDf).fit()
print(regression_result.summary())

##회귀 분석 모델을 통한 새로운 샘플의 품질등급 예측
##quality와 type열을 제외하고 회귀분석모델에 사용할 샘플 데이터 가져오기
sample1 = wineDf[wineDf.columns.difference(['quality','type'])]
sample1 = sample1[0:5][:]
#품질예측
sample1_predict = regression_result.predict(sample1)
print(sample1_predict)

#실제 품질
print(wineDf[0:5]['quality'])

##새로운 데이터로 품질 예측
data = {'fixed_acidity':[8.5,8.1],'volatile_acidity':[0.8,0.5],'citric_acid':[0.3,0.4],'residual_sugar':[6.1,5.8],'chlorides':[0.055,0.04],'free_sulfur_dioxide':[30.0,31.0], \
    'total_sulfur_dioxide':[98.0,99],'density':[0.996,0.91],'pH':[3.25,3.01],'sulphates':[0.4,0.35],'alcohol':[9.0,0.88]}

sample2 = pd.DataFrame(data, columns=sample1.columns)
sample2_predict = regression_result.predict(sample2)
print(sample2_predict)


##시각화 : 히스토그램
import matplotlib.pyplot as plt
import seaborn as sns

#스타일 테마 설정(darkgrid, whitegrid, dark, white, ticks)
sns.set_style('dark')
#커널 밀도 추정(kde)을 적용한 히스토그램 그리기
sns.distplot(red_wine_quality, kde=True, color='red',label='red wine')
sns.distplot(white_wine_quality, kde=True, color='blue',label='white wine')
plt.title('Quality of Wine Type')
plt.legend()
plt.show()

##선형회귀 모델 그래프로 만들기 volatile_acidity가 종속변수 quality에 미치는 영향력 시각화
#독립변수와 종속변수를 제외한 나머지 변수 이름 추출\
others = list(set(wineDf.columns).difference(set(['quality','volatile_acidity'])))
#나머지 변수 고정하고 volatile_acidity가 종속변수
#quality에 미치는 영향에 부분 회귀 수행
import statsmodels.api as sm
# p, resis = sm.graphics.plot_partregress('quality','volatile_acidity',others,data=wineDf,ret_coords=True)
# plt.show()

fig = plt.figure(figsize=(8,13))
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.show()








































