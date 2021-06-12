
import numpy as np
import pandas as pd
from scipy import stats


#1번문제
n=10
sample = [30.8,31.9,30.4,30.5,32.0,29.0,28.8,30.3,31.3,29.3]
s_mean = np.mean(sample)
s_mean
rv = stats.t(df=n-1)
u_var=np.var(sample, ddof=1)
lcl = s_mean - rv.isf(0.025)*np.sqrt(u_var/n)
ucl = s_mean - rv.isf(0.975)*np.sqrt(u_var/n)
#답
lcl, ucl
#맞음


#2번 문제

s_mean=415/700
#구간추정
n=700#자유도
rv = stats.norm()
lcl = s_mean - rv.isf(0.005)*np.sqrt(s_mean*(1-s_mean)/n)
ucl = s_mean - rv.isf(0.995)*np.sqrt(s_mean*(1-s_mean)/n)
#답
lcl,ucl
#맞음



#3번 문제

n1=7.5

Y= 14*7.5/3.75
rv=stats.chi2(14)
#신뢰구간
p=rv.interval(0.95)
p
#답 : p
#틀림


#4번 문제
# H0 = 평균 수명 300일
# H1 = 평균 수명 300일 보다 작다
#정규분포 실패
#단측검정
#검정통계량
z=(290-300)/np.sqrt(30**2/25)
#임계값 
rv= stats.norm()
rv.isf(0.95)
#검정통계량 임계값 비교
z, rv.isf(0.95) #검정통계량 < 임계값 (귀무가설 기각)
#답 : 귀무가설 기각

#틀림.

#5번문제
# H0 = 불량률 1%
# H1 = 불량률 1% 보다크다
#단측검정
#베르누이분포
z=(0.02-0.01)/np.sqrt(0.0196)
rv= stats.bernoulli(0.02) 
z, rv.isf(0.95)
#답 : 귀무가설 채택

#틀림.

#6번 문제
# H0 = 표준편차 10일
# H1 = 표준편차 10일 보다크다
#단측
#카이분포
#검정통계량
Y= 19*225/100
rv=stats.chi2(19)
#임계값
p=rv.isf(0.95)
Y,p
#답 : 귀무가설 기각
#틀림.


#7번 문제
#평균값 검정.
red_df = pd.read_csv('./winequality-red.csv', sep=';')
white_df = pd.read_csv('./winequality-white.csv', sep=';')

red_al = np.array(red_df['alcohol'])
white_al = np.array(white_df['alcohol'])

t,p = stats.ttest_ind(red_al, white_al, equal_var=False)
p#0.004 귀무가설 기각 평균값에 차이가 있다.
red_al.mean(), white_al.mean()


#F 분포
#자유도 각각 필요함.
red_n = len(red_al)
white_n = len(white_al)

rv = stats.f(red_n-1, white_n-1)
#임계값
rv.interval(0.95)
#검통량= 두분산의 비율
red_var = red_al.var(ddof=1)
white_var = white_al.var(ddof=1)
red_var/white_var#검정통계량
#기각 = 분산값에 차이가 있다.



