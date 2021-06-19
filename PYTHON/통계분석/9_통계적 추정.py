#추측 통계는 추정과 검정이 있다.
#추정 : 값을 추정하는 것이고
#검정 : 값이 맞는지 확인 하는 것
#1. 점추정 : 추정하고 싶은 모수(모평균,모분산)을 하나의 수치로 추정
# 2. 구간추정 : 폭(구간)으로 모수를 추정하는 방법

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#ex)전고생 400명의 모집단, 모평균과 모분산 추정
# a 학생이 가지고 있는 데이터는 20명의 데이터만 있다.
# 데이터 준비
df = pd.read_csv('./data/ch4_scores400.csv')
df.head()
scores = np.array(df['score']) 

#모수 구하기
p_mean= np.mean(scores)
p_var=np.var(scores)
p_mean, p_var

#모집단의 분포 히스토 그램 시각화
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.arange(101)
ax.hist(scores, bins=100, range=(0,100), density=True)
rv = stats.norm(p_mean, np.sqrt(p_var))
ax.plot(xs, rv.pdf(xs), color='gray')
plt.show()
#응시자가 많을 수록 시험점수는 정규분포를 따르는 것으로 근사화 할수 있음.

#A학생이 무작위 추출 - 20개 표본 데이터
np.random.seed(0)
n=20
sample = np.random.choice(scores, n)
sample

#A학생과는 별도로 표본크기 20일때 어느정도 정확도로
#모수를 추정하는지 시뮬레이션
#표본크기 20, 표본데이터 1만개 준비
np.random.seed(1111)
n_samples = 10000
samples = np.random.choice(scores, (n_samples,n))
samples.shape #행(10000)데이터수, 열(20)표본수

#1.점추정
#무작위 추출로 얻은 20명의 시험점수는 기댓값이 p_mean 이고
#분산이 p_var인 확률분포를 따르고, 점수는 서로 독립인 확률변수라 생각할수있다.

#p_mean 을 추정하기 위해 표본평균 Xbar  가 확률변수가 되고
#Xbar의 기댓값은 p_mean, 분산 p_var/20

#(1) 모평균의 점추정
#추정량의 기댓값이 추측하려는 모수가 되는 성질을 불편성이라 한다.
#불편성(unbiasedness) 을 가진 추정량을 분편추정량이라고 한다.

for i in range(5):
    s_mean = np.mean(samples)
    print(f'{i+1}번째의 표본평균 : {s_mean:.3f}')
sample_means = np.mean(samples, axis=1)
p_mean, np.mean(sample_means)

#일치성 : 표본 크기 n을 증가시키면 추측하기 원하는 모수에 수렴하는 성질
np.mean(np.random.choice(scores, 100))

##표본평균은 불편성과 일치성 모두 가지고 있어서 모평균을 잘 추정한다고 말할수 있다.

#(2) 모분산의 점추정
for i in range(5):
    s_var = np.var(samples[i])
    print(f'{i+1}번째의 표본분산 : {s_var:.3f}')
sample_var = np.var(samples, axis=1)
p_var, np.mean(sample_var)

#표본분산은 모분산의 불편추정량이 아님
#모분산의 불편추정량이 되는 표본통계량은 불편분산
#불편분산 : 표본분산에서 나누는 수 n을 n-1계산 (자유도 1 감소)
samples.shape #행(10000)데이터수, 열(20)표본수
sample_u_vars = np.var(samples, axis=1, ddof=1)
sample_u_vars.shape
#표본들의 불편분산

for i in range(5):
    print(f'{i+1}번째의 불편분산분산 : {sample_u_vars[i]:.3f}')
p_var, np.mean(sample_u_vars)#불편분산들의 평균값
p_var, np.var(np.random.choice(scores, int(1e6)),ddof=1)#표본크기를 늘렸을때 일치성을 갖고있는지


#불편분산은 모분산에 대해서 불편성과 일치성을 지닌 좋은추정량
#A학생이 추출한 표본으로 불편분산 계산
u_var=np.var(sample, ddof=1)
p_var,u_var
#(3) 정리
#추정량은 불편성과 일치성을 가지는 것이 바람직
#불편성 : 기댓값이 추측하기 원하는 모수가 되는 성질
#일치성 : 표본 크기를 키우면 추측하기 원하는 모수에 수렴하는 성질





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2. 구간추정
#표본평균이나 불편분산이 확률변수이므로, 아무리 좋은 추정량이라고 입증되어도,
#우연히 편향된 표본을 추출해 버리는 경우 예상과 다른 추정이 될수 있음
#사전에 예상된 오차를 예측하고 모평균이 이 범위에 있다라고 주장을 할 수 있으면 
#좋은 추정이된다.

#(1) 모집단이 정규분포인 경우 모평균의 구간 추정 : 모분산을 알고 있는 경우
#표본 평균 xvar는 N(m, var/n)
#추정량의 표준편차를 표준 오차라고 함

#모평균에 대한 신뢰수준 95% 신뢰구간, 또는 95% 신뢰구간이라함.
#신뢰구간의 상한과 하한을 각각 신뢰 상한, 신뢰 하한 이라고 함.

#a학생이 뽑은 샘플 데이터

s_mean = np.mean(sample)#표본평균
#모평균, 모분산
p_mean = np.mean(scores)
p_var = np.var(scores)

rv = stats.norm()#표준정규분포
lcl = s_mean - rv.isf(0.025)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰하한
ucl = s_mean - rv.isf(0.975)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰상한

p_mean,lcl,ucl

##잘못된 해석 : 모평균이 95%확률로 구간에 들어간다.
##옳은 해석 : 모평균은 변동이 없으므로 표본을 추출하여 구간을 산출했을때 그중에 95%의 구간 추정에는 모평균이 포함되어있다.(확률로 변동하는것은 구간임.)


#실험적으로 신뢰구간 20개를 구한후 , 그중 몇개가 모평균을 포함하고 있는지 확인
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
rv = stats.norm()
n_samples =20
ax.vlines(p_mean, 0 , 21)

for i in range(n_samples):
    sample = samples[i]
    s_mean = np.mean(sample)
    lcl = s_mean - rv.isf(0.025)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰하한
    ucl = s_mean - rv.isf(0.975)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰상한
    if lcl <= p_mean <= ucl:
        ax.scatter(s_mean, i, color='gray')#점찍기
        ax.hlines(i, lcl, ucl, color='gray')#수평선 그리기
    else :
        ax.scatter(s_mean, i, color='b')#점찍기
        ax.hlines(i, lcl, ucl, color='b')#수평선 그리기
plt.show()
#95%신뢰구간 이미지 : 20번중 1번 모평균을 포함하지 않는 구간 추정 이 됨.
#5% * 20개 = 1개

#신뢰구간을 1만번 계산후, 신뢰구간에 모평균이 포함된 것이 몇 %인지 확인
rv = stats.norm()
cnt = 0
for sample in samples :
    s_mean = np.mean(sample)
    lcl = s_mean - rv.isf(0.025)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰하한
    ucl = s_mean - rv.isf(0.975)*np.sqrt(p_var/n) #95%신뢰구간의 신뢰상한
    if lcl <= p_mean <= ucl:
        cnt +=1
cnt/len(samples) #0.9512
#신뢰 구간 약 95%가 모평균을 포함하고 있음을 확인
#
#(2) 정규분포의 모평균 구간 추정 : 모분산을 모르는 경우
#실제로는 모평균, 모분산 둘다 모름
#모분산 대신 불편분산을 사용하여 표준오차로 대신한다.
#t=(Xbar-p_mean)/sqrt(s^2/n)
#자유도가 n-1인 t(n-1)를 따름

#모평균의 95% 신뢰구간
#p(t0.975(n-1)<=t<=t.0.025(n-1))=0.95
#

rv = stats.t(df=n-1)##ddof=1 :자유도를 1 감소하겠다. df = 자유도 
lcl = s_mean - rv.isf(0.025)*np.sqrt(u_var/n)
ucl = s_mean - rv.isf(0.975)*np.sqrt(u_var/n)
p_mean, lcl, ucl
#모분산을 가는 경우와 차이점 z분포가 t분포로 바뀌고 모분산이 불편분산으로 바뀜

#(3) 정규분포의모분산 구간 추정
#모집단 모평균을 모르는 경우
#P(*<=p_var<=*) = 0.95

#P(chi2_0.975(n-1)<= y <= chi2_0.025(n-1))=0.95

#A학생의 표본데이터를 사용하여 모분산에 대한 95% 신뢰구간
rv=stats.chi2(df=n-1)
lcl = (n-1)*u_var/rv.isf(0.025)
ucl = (n-1)*u_var/rv.isf(0.975)
p_var,lcl,ucl

#(4) 모집단이 베르누이 분포인 모평균의 구간 추정
#ex) 정권의 지지율(찬성/반대), 국민의 흡연율(흡연자/비흡연자)
#설문조사에서 찬성/반대, 흡연/ 금연이라는 확률변수가 2진변수가 됨(0,1)

#중심극한정리에 따라서 (표본이 30개 이상인 경우) 표본평균 Xbar는 근사적으로 
#N(p, p(1-P)/n)
#Z = (Xbar-p)/sqrt(p(1-p)/n))
#P(z0.975<= z<=z0.025)=0.95

#ex)상품A에 대한 인지도 조사 ,1000명 조사 -> 국민 전체의 인지도 p추정
enquete_df = pd.read_csv('./data/ch10_enquete.csv')
enquete_df.info()
enquete_df.head()
enquete = np.array(enquete_df['known'])
#0모른다, 1 안다
#점추정
s_mean = enquete.mean()
s_mean#0.709 #A상품의 인지도 약 70.9%라고 추정
#구간추정
n=len(enquete)#자유도
rv = stats.norm()
lcl = s_mean - rv.isf(0.025)*np.sqrt(s_mean*(1-s_mean)/n)
ucl = s_mean - rv.isf(0.975)*np.sqrt(s_mean*(1-s_mean)/n)
lcl,ucl
#(0.6808474522924337, 0.7371525477075662)
#베르누이 분포의 구간추정


#(5)모집단이 포아송 분포의 모평균 신뢰구간

#ex) 어떤 사이트에 1시간당 액세스 수가 과거 72시간 분량이 들어간데이터
#사이트에 대한 1시간당 평균 액세스 (추정)

n_access_df = pd.read_csv('./data/ch10_access.csv')
n_access_df.info()
n_access_df.head()
n_access = np.array(n_access_df['access number'])
n=len(n_access)
#포아송 분포의 기댓값과 분산 모두 lam
#포아송 분포의 표본 평균의 분포의 기댓값 lam , 분산 lam

#모평균의 점추정
s_mean = n_access.mean()
s_mean#10.4 한시간에 10번정도 출입

#모평균의 구간추정
#중심극한정리에 의해 표본 평균 Xbar는 근사적으로 N(lam, lam/n)을 따름
#정규화 Z=(Xbar-lam)/sqrt(lam/n)

rv = stats.norm()
lcl = s_mean - rv.isf(0.025)*np.sqrt(s_mean/n)
ucl = s_mean - rv.isf(0.975)*np.sqrt(s_mean/n)
lcl , ucl #모집단 lam에 대한 95%신뢰구간



