#1. 두데이터 사이의 관계를 나타내는 지표 - 공분산, 상관계수
#2. 2차원 데이터 시각화 - 산점도, 회귀선
#3. 엔스컴의 예 - 수치지표는 많은 정보를 잃어버릴수 있다. (데이터 시각화의 중요성)

import numpy as np
import pandas as pd
df = pd.read_csv('./data/ch2_scores_em.csv', index_col='student number')
df.head()

#10개 점수 얻기
en_scores = np.array(df['english'][:10])
ma_scores = np.array(df['mathematics'][:10])

indexList = [chr(ord('A')+i) for i in range(10)]
indexList
scores_df = pd.DataFrame({'eng':en_scores,'math':ma_scores},index=pd.Index(indexList,name='student'))
scores_df

#1. 두 데이터 사이의 관계를 나타내는 지표
#양의 상관관계 ex)영어 점수가 높은 학생이 수학점수도  높을때
#음의 상관관계 ex)영어 점수가 높은 학생이 수학점수도  낮을때
#무 상관관계 ex)영어 점수와 수학점수가 직접적으로 영향을 미치지 않을때

#(1) 공분산 - 각 데이터 편차들의 곱의 평균값
# cov(x,y) = E((x-u)*(y-v))
# x는 영어점수, u는 영어점수의 평균
# y는 수학점수, v는 수학점수 평균
# 공분산이 양의 값이면 양의 상관관계
# 공분산이 음의 값이면 음의 상관관계
# 공분산이 0에 가까울수록 무상관

summary_df=scores_df.copy()
summary_df['eng_dev'] = summary_df['eng']-summary_df['eng'].mean()
summary_df['math_dev'] = summary_df['math']-summary_df['math'].mean()
summary_df['product of dev']= summary_df['eng_dev']*summary_df['math_dev']
summary_df

#공분산 값
summary_df['product of dev'].mean() ##62.8 양의 상관관계
#함수
np.cov(en_scores, ma_scores, ddof=0)
#array([[86.  , 62.8 ], 분산 공분산
#       [62.8 , 68.44]])공분산 분산

##공분산 문제점 : 단위에 따라서 공분산값이 커지거나 작아진다. ex) 100점 만점인 과목과 10점 만점의 공분산 값이 다름


#상관계수 : 단위에 의존하지 않는 지표
# R = Cov(x,y)/(std(x)*Std(y))
# -1~1 사이의 값을 갖는다.
#양의 상관관계 : 1에 가까움
#음의 상관관계 : -1에 가까움
#무 상관관계 : 0에 가까움

np.cov(en_scores,ma_scores, ddof=0)[0,1]/(np.std(en_scores)*np.std(ma_scores))#0.9강한 양의 상관관계
np.corrcoef(en_scores, ma_scores)
#데이터 프레임에서 상관계수
scores_df.corr()
#-------------------------------------------------------------------------------------------------------------------------------------------------

#2차원 데이터의 시각화
#(1) 산점도
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.scatter(scores_df['eng'], scores_df['math'])
ax.set_xlabel('eng')
ax.set_ylabel('math')
for idx,data in scores_df.iterrows():
    ax.text(data['eng']+0.3, data['math'],idx,fontsize=10)
plt.show()


#(2) 회귀 직선 - 두 데이터 사이의 관계를 더욱 잘 나타내는 직선
#y= ax+b

en_scores = np.array(df['english'])
ma_scores = np.array(df['mathematics'])
#a,b의 계수를 구한다.
poly_fit = np.polyfit(en_scores,ma_scores,1)
poly_fit #y=0.621*x+42.6

#함수반환
poly_1d = np.poly1d(poly_fit)
poly_1d
poly_1d(0)#y=0.621*x+42.6 (x=0)
poly_1d(1)#y=0.621*x+42.6 (x=1)

#데이터 얻기
xs = np.linspace(en_scores.min(),en_scores.max())
xs
xs.shape
ys = poly_1d(xs)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.scatter(en_scores, ma_scores)
ax.set_xlabel('eng')
ax.set_ylabel('math')
ax.plot(xs,ys, color='gray', label = f'Y={poly_fit[0]:.2f}X+{poly_fit[1]:.2f}')    
ax.legend()
plt.show()

#(3)히트맵 - 히스토그램의 2차원 버전 색을 이용해 시각화
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
pd.Series(en_scores).describe()# min 37, max 79
pd.Series(ma_scores).describe()# min 57, max 94

c = ax.hist2d(en_scores, ma_scores,bins=[9,8], range=[(35,80),(55,95)],cmap='Reds')#계급폭 5점 으로
ax.set_xlabel('eng')
ax.set_ylabel('math')
ax.set_xticks(c[1])
ax.set_yticks(c[2])
#컬러바 표시
fig.colorbar(c[3],ax=ax)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------

# 3. 앤스컴의 예 - 데이터 분석시에 가능하면 시각화를 해야 좋다.
# 총 4개의 데이터, 2차원 , 11개
anscom_data = np.load('./data/ch3_anscombe.npy')
anscom_data
anscom_data.shape

#데이터의 통계값 정리
stats_df = pd.DataFrame(index=['X_mean','X_var','Y_mean','Y_var','X&Y_Corr','X&Y_reg_line'])
for i, data in enumerate(anscom_data) :
    dataX = data[:,0]
    dataY = data[:,1]
    poly_fit = np.polyfit(dataX, dataY,1)
    stats_df[f'data{i+1}']=[np.mean(dataX), np.var(dataX), np.mean(dataY), np.var(dataY), np.corrcoef(dataX,dataY)[0,1],f'Y={poly_fit[0]:.2f}X+{poly_fit[1]:.2f}']
stats_df
#4개의 데이터의 통계값이 비슷함

#2x2 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10),sharex=True,sharey=True)
xs = np.linspace(0,30,100)
for i, data in enumerate(anscom_data) :
    dataX = data[:,0]
    dataY = data[:,1]
    poly_fit = np.polyfit(dataX,dataY,1)
    poly_1d = np.poly1d(poly_fit)
    ys = poly_1d(xs)

    #그리기 영역
    ax = axes[i//2,i%2]
    ax.set_xlim([4,20])
    ax.set_ylim([3,13])
    #타이틀
    ax.set_title(f'data{i+1}')
    ax.scatter(dataX, dataY)
    ax.plot(xs,ys, color='gray')

#그래프 사이 간격 좁히기
plt.tight_layout()
plt.show()


##2차원 데이터의 정리까지 마무리 -----


























