#1. 데이터 중심지표 - 평균, 중앙값, 최빈값
#2. 데이터 산포도 지표 - 분산, 표준편차, 범위, 사분위범위
#3. 데이터의 정규화 - 표준화, 편차값
#4. 1차원 데이터 시각화 - 도수분포표, 히스토그램, 박스플롯

import numpy as np
import pandas as pd

#데이터 프레임 출력을 소수점 3자리로 제한
pd.set_option('precision',3)
df = pd.read_csv("./data/ch2_scores_em.csv",index_col='student number')
df.head()

#처음 10명의 영어점수만
scores = np.array(df['english'])[:10]
scores
#데이터 프레임으로 변경
#A~Z인덱스
indexList = [chr(ord('A')+i) for i in range(10)]
indexList
scores_df = pd.DataFrame({'score':scores},index=pd.Index(indexList,name='student'))
scores_df

#1. 데이터 중심지표
#(1) 평균
sum(scores)/len(scores)
np.mean(scores)
scores_df.mean()

#(2) 중앙값 구하기 - 데이터를 크기순으로 나열할때 중앙에 위치한 값
#데이터의 개수가 홀수 : (n+1)/2의 인덱스 값
#데이터의 개수가 짝수 : n/2번째 데이터와 n/2번째 데이터의 평균값
#특징 : 평균값에 비해 이상값에 강하다
#ex) [1,2,3,4,5,6,1000] 평균 145.8, 중앙값 4
#중앙값 도출법
sorted_scores = np.sort(scores)
n = len(sorted_scores)
if n%2==1 :
    #인덱스가 0부터 시작하므로 1을뺌
    median = sorted_scores[(n+1)/2-1]
else :
    m0 = sorted_scores[n//2-1]
    m1 = sorted_scores[n//2]
    median = (m0+m1)/2
sorted_scores
median
#함수
np.median(scores)
scores_df.median()

#(3) 최빈값 - 데이터에서 가장 많이 나타나는 값
scores_df.mode()

from scipy.stats import mode##통계처리 모듈
mode(scores)

# ---------------------------------------------------------------------------------------------------------------------
# 2. 데이터 산포도 지표
# (1) 편차 - (데이터-데이터의 평균)
# 모든 데이터 편차의 합은 0이 되는 특징이 있다.
mean = np.mean(scores)
deviation = scores-mean
deviation
np.sum(deviation)

#(2) 분산 - 편차 제곱의평균
devSquare = deviation**2
np.mean(devSquare)
np.var(scores)
scores_df.var(ddof=0)#표본을 통해서 분산을 구할때 1 줄어듬 데이터프레임에서 분산을 구하면 표본분산으로 구함

#(3) 표준 편차 - 분산의 제곱근, 데이터와 동일한 단위
np.sqrt(np.var(scores))
np.std(scores)
scores_df.std(ddof=0)

#(4) 범위 - 데이터의 최댓값 - 최솟값
#특징 : 이상값에 약하다
np.max(scores) - np.min(scores)

#(5) 사분위 범위 - 데이터를 정렬했을때 데이터 하위 25%를 Q1, 데이터 하위 75%는 Q3
#IQR = Q3-Q1
scores_Q1=np.percentile(scores,25)
scores_Q3=np.percentile(scores,75)
scores_IQR = scores_Q3-scores_Q1
scores_IQR

pd.Series(scores).describe()
summary_df=pd.Series(scores).describe()
summary_df['75%']-summary_df['25%']

#---------------------------------------------------------------------------------------------------------------------------------
#3.데이터의 정규화
#평균이나 분산에 의존하지 않고도 데이터의 상대적 위치를 알수있다.

#(1) 표준화
#데이터에서 평균을 빼고 표준 편자로 나누는 작업, Z값이라 한다.
#표준화데이터는 평균 0, 표준편차 1된다.
#단위는 없다.
# z = (x-mean)/std

z=(scores-np.mean(scores))/np.std(scores)
z



#(2) 편차값 - 평균 50 , 표준편차 10 되도록 정규화
# z=50+10*(x-mean)/std

dev_value = 50+10*(scores-np.mean(scores))/np.std(scores)
dev_value
scores_df['dev_value']=dev_value
scores_df
#편차값을 통해 어떤 학생이 우수한 성적을 얻었는지 한눈에 파악 가능

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#4. 1차원데이터의 시각화
#전체학생 영어점수
eng_scores = np.array(df['english'])
pd.Series(eng_scores).describe()

#(1) 도수 분포표 - 분할된 구간과 그 구간에 속한 데이터 갯수를 표로 정리
#계급 = 0~10,10~20,20~30 구간들
#도수 = 각 계급에 속한 학생수
#계급 폭 = 0~10점 계급 폭 10, 0~5점 계급 폭 5
#계급 수 = 계급의 개수 (10개)

#bins = 계급수, range로 최소값, 최대값 지정
freq, cls = np.histogram(eng_scores, bins=10, range=(0,100))
freq #도수
cls # 계급

freq_class=[f'{int(cls[i])}~{int(cls[i+1])}' for i in range(len(cls)) if i!=len(cls)-1]
freq_class

freq_dist_df = pd.DataFrame({'freq':freq},index=pd.Index(freq_class, name='class'))
freq_dist_df

#계급 값 : 계급을 대표하는 값, 계급의 중앙값
#ex) 60~70점의 계급값 65
class_value =[sum(map(int, cal.split('~')))/2 for cal in freq_class]
class_value

freq_dist_df['class value']= class_value
freq_dist_df

#상대 도수
#전체 데이터에서 해당 계급의 데이터가 어느정도의 비율을 차지하고 있는지 나타내는 비율

rel_freq = freq/freq.sum()
rel_freq
freq_dist_df['rel_freq']=rel_freq
freq_dist_df

#누적 상대 도수 : 해당 계급 까지의 상대도수 합
cum_rel_freq = np.cumsum(rel_freq)
freq_dist_df['cum_rel_freq']=cum_rel_freq
freq_dist_df

#도수분포표를 통해 양적 데이터에 대해서 최빈값 구하기
#도수분포표의 최빈값은 최대가 되는 도수의 계급값
freq_dist_df.loc[freq_dist_df['freq'].idxmax(),'class value'] #loc (index, col)

#(2) 히스토그램 - 도수분포표를 막대그래프로 시각화
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
freq,_,_=ax.hist(eng_scores,bins=10,range=(0,100))
ax.set_xlable('score')
ax.set_ylable('person number')
ax.set_xticks(np.linspace(0,100,11))#구간
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()


#Quiz 계급수를 25, 계급 폭 4점으로 하는 히스토그램 출력
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
freq,_,_=ax.hist(eng_scores,bins=25,range=(0,100))
ax.set_xlable('score')
ax.set_ylable('person number')
ax.set_xticks(np.linspace(0,100,26))#구간
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()

#상대도수의 히스토그램과 누적상대도수의 꺾은선 그래프 시각화
fig = plt.figure(figsize=(10,6))
ax1=fig.add_subplot(111)
#y축의 스케일이 다른 그래프를 ax1과 동일한 영역에서 생성
ax2 = ax1.twinx()

#데이터별 가중치 얻기
np.ones_like(eng_scores)
weights = np.ones_like(eng_scores)/len(eng_scores)
rel_freq,_,_ = ax1.hist(eng_scores, bins=25,range=(0,100),weights=weights)
#누적상대도수
cum_rel_freq = np.cumsum(rel_freq)
#계급값
class_value = [(i+(i+4))//2 for i in range(0,100,4)]
class_value

ax2.plot(class_value,cum_rel_freq,ls='--',marker='o',color='gray')

ax1.set_xlabel("score")
ax1.set_ylabel("relative freq")
ax2.set_ylabel("cumulative relative freq")
ax1.set_xticks(np.linspace(0,100,25+1))#x축눈금생성
plt.show()

#(4) 상자그림 - 데이터 분포와 이상값을 시각적으로 파악
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
ax.boxplot(eng_scores,labels=['english'])
plt.show()

#--------------------------------------------------------------------------------------------------------
#그래프 그리기
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)#2행1열의 1행
ax2 = fig.add_subplot(2,1,2)#2행1열의 2행
x= range(0,100)
y= [v*v for v in x]
ax1.plot(x,y)
ax2.bar(x,y)
plt.show()


fig = plt.figure()
ax = fig.subplots(nrows=1,ncols=2, sharex=False, sharey=True)#2행1열의 1행

x= range(0,100)
y= [v*v for v in x]
ax[0].plot(x,y)
ax[1].bar(x,y)
plt.show()





























