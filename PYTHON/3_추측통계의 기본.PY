#1.모집단과 표본 = 표본 추출, 표본 평균
#2.확률 모형 - 확률분포
#3. 추측통계의 확률 - 모평균 추측

#1. 모집단과 표본
#-----------용어----------------
#추측통계 : 일부 데이터로부터 전체의 (모집단) 통계적 성질을 추측
#모집단 : 추측하고 싶은 관측 대상
#표본 : 추측에 사용되는 관측대상
#표본추출 : 모집단에서 표본을 골라내는일
#표본크기(샘플 사이즈) : 포본의 수
#표본 통계량 : 표본을 바탕으로 구한 평균, 분산 , 상관계수 등
#모수 : 모집단의 평균 , 분산, 상관계수 등 (알고싶은 대상)
#추정량 : 표본평균으로 모평균 추측할때, 표본평균은 모평균
#추정값 : 표본의 데이터를 이용하여 계산한 결과

#EX) 전교생 400명 모집단
#전교생의 평균, 분산
#우연히 만난 20명으로 추측통계

# 1)표본추출 방법
#무작위 추출 : 표본추출이 편향되지 않도록 무작위 추출
#복원추출 : 여러차례 동일한 표본을 선택할 수도 있는 추출
#비복원 추출 : 동일한 표본은 한 번만 선택하는 방법

from os import name, replace
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#무작위 복원 추출
np.random.seed(0)
np.random.choice([1,2,3],3)#리스트내의 값에서 3개의 표본 추출
#무작위 비복원 추출
np.random.choice([1,2,3],3,replace=False)

#전교생 데이터
df = pd.read_csv('./data/ch4_scores400.csv')
scores = np.array(df['score'])
#성적 무작위 복원 추출
np.random.seed(0)
sample = np.random.choice(scores, 20)#표본 20개 추출
sample
sample.mean(), sample.var()

scores.mean(), sample.mean() #평균값은 표본과 모집단의 추정이 가능
scores.var(), sample.var() #분산은 추가 처리가 필요함 잘 안맞음

#무작위 추출에 따른 표본값
for i in range(5) :
    sample = np.random.choice(scores, 20)
    print(f'{i+1}번째 무작위 추출로 얻은 표본평균', sample.mean())
#표본의 평균값이 모집단의 평균값을 추정을 잘한다.
#--------------------------------------------------------------------------------------------------
#2.확률모형
#1)확률기본
#확률 : 불확장성을 수반한 현상을 해석하기 위한 수단
#확률모형 : 불확실성을 확률로서 계량하기위해 수학적으로 만든 모형 (함수)
#확률변수 : 무작위 실험을 통해, 특정 확률로 발생하는 각각의 결과를 수치적 값으로 표현
#시행 : 확률변수의 결과를 관측하는 것
#실현값 : 시행에 의해 관측되는 값
#사건 : 시행결과로 나타날수 있는 값
#근원사건 : 세부적으로 더 분해될수 없는 사건 ex) 주사위 눈이 1,2,3,4,5,6
#상호배반 : 동시에 일어날수 없는 사건 (주사위의 눈이 1과 2가 동시에 나올수 없음)

#ex) 주사위
#주사위의 눈이 확률변수 X
#주사위의 눈이 2가 나올 확률 P(X=2)=1/6
#주사위의 눈이 홀수가 나올확률
#P(X=1 U X=3 U X=5) = P(X=1)+P(X=3)+P(X=5)
#확률분포
dice = [1,2,3,4,5,6]
prob = [6/1,6/1,6/1,6/1,6/1,6/1]

#불공정 주사위를 사용해서 확률분포 확인

#2) 확률분포 : 확률변수가 어떻게 움직이는 나타낸것
dice = [1,2,3,4,5,6]
prob = [1/21,2/21,3/21,4/21,5/21,6/21]
np.random.choice(dice, p=prob)


numTrial = 10000
sample = np.random.choice(dice, numTrial, p=prob)
sample

#도수분포표
freq,_=np.histogram(sample, bins = 6, range=(1,7))
pd.DataFrame({'freq':freq,'rel_freq':freq/numTrial},index=pd.Index(np.arange(1,7),name='dice'))

#시각화 - 히스토그램
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
#density : 확률밀도를 형성시키기 위해 정규화(상대도수값)
ax.hist(sample, bins=6, range=(1,7), density=True, rwidth=0.8)
#실제 확률분포를 가로선 표시
#prob y값, np.arange(1,7), np.arange(2,8) x값의 시작과 끝에 대응
ax.hlines(prob, np.arange(1,7), np.arange(2,8), colors='gray')
#눈금표시
ax.set_xticks(np.linspace(1.5,6.5,6))
ax.set_xticklabels(np.arange(1,7))
ax.set_xlabel('dice')
ax.set_ylabel('relative freq')
plt.show()

#시행횟수가 커질수록 실제 확률분포에 가까워 진다.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3.추측통계의 확률
#전교생 시험점수 분포 확인 - 히스토그램(계급값 1)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0,100),density=True)
ax.set_xlabel('score')
ax.set_ylabel('reative freq')
ax.set_xlim(20,100)
ax.set_ylim(0,0.042)
plt.show()

#모집단의 확률분포 정규분포로 바꿔서 근사화 한다.

#표본 추출 통한 확률 분포 -> 표본이 커지면 실제 분포에 수렴함
sample = np.random.choice(scores, 100)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hist(sample, bins=100, range=(0,100),density=True)
ax.set_xlabel('score')
ax.set_ylabel('reative freq')
plt.show()


#표본평균 ->확률변수임, 표본크기 20 무작위 추출 작업 10000번수행
#표본평균에 대한 확률분포를 본다.
#표본평균은 산포도 자체이므로, 모평균을 중심으로 분포
sample_mean = [np.random.choice(scores,20).mean()for _ in range(10000)]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hist(sample_mean, bins=100, range=(0,100),density=True)
#모평균을 세로선으로 표시
ax.vlines(np.mean(scores), 0,1,'gray')
ax.set_xlabel('score')
ax.set_ylabel('rel freq')
ax.set_xlim(50,90)
ax.set_ylim(0,0.13)
plt.show()

#추정 모수를 추측하는것
#점추정 : 모평균을 하나의 값으로 추정 ex)모평균을 70.4로 추정
#구간추정 : 모평균을 구간으로 추정 ex) 모평균 68~72점 사이




























