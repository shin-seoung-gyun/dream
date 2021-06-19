# 추측통계 목표 : 한정된 표본으로 부터 모집단의 평균과 분산 (모수) 추정
# 비 모수적 기법 : 모집단의 확률분포에서 아무런 가정하지않고 지표 추정
# 모수적 기법 : 모집단이 이러한 성질일 것이고, 이러한 형태를 지닌 확률분포라고 가정 (정확도가 조금더 높음)

#베르누이 분포
#이항분포
#기하분포
#포아송분포


#

import numpy as np
from scipy import stats#통계처리를 하는 대표적인 모듈
import matplotlib.pyplot as plt

# 그래프 선의 종류
linestyles = ['-', '--', ':']

#1차원 이산형 확률변수의 기댓값
def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])

#1차원 이산형 확률변수의 분산
def V(X, g=lambda x: x):
    x_set, f = X
    mean = E(X, g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])

#확률변수를 인수로 가지며, 그 확률변수가 확률의 성질을 만족하지는지 확인 및 기댓값과 분산 출력
def check_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    assert np.all(prob >= 0), 'minus probability'
    prob_sum = np.round(np.sum(prob), 6)
    assert prob_sum == 1, f'sum of probability{prob_sum}'
    print(f'expected value {E(X):.4}')
    print(f'variance {(V(X)):.4}')

#확률변수의 확률함수와 기댓값 그리기 위한 함수
def plot_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.bar(x_set, prob, label='prob')
    ax.vlines(E(X), 0, 1,colors='black', label='mean')
    ax.set_xticks(np.append(x_set, E(X)))
    ax.set_ylim(0, prob.max()*1.2)
    ax.legend()
    plt.show()

#-------------------------------------------------------------------------------------------------------------자주쓸 함수 ----------------------------------------------------------------

# 1. 베르누이 분포
#확률변수가 취할수 있는 값이 0과 1밖에 없는 분포
#ex) 동전 던지기, 암진단유무
#1이 나오면 성공, 0이나오면 실패
#1이나오는 확률 p, 0이나오는 확률 1-p
#Bern(p)

#동전을 던져서 앞면이 나올 확률(성공할 확률)
#Bern(1/2)= 1/2
#주사위를 굴려서 6이 나오지 않을 확률(실패할 확률)
#Bern(1/6)= 1-1/6

#베르누이 분포의 기댓값 p
#베르누이 분포의 분산값 p*(1-p)

def Bern(p):
    x_set = np.array([0,1])
    #베르누이 분포의 확률함수
    def f(x):
        if x in x_set :\
            return p**x*(1-p)**(1-x)
        else :
            return 0
    return x_set, f

#성공확률
p=0.3
X=Bern(p)
check_prob(X)
plot_prob(X)

rv=stats.bernoulli(p)
#pmf 확률질량함수
rv.pmf(0), rv.pmf(1)
rv.pmf([0,1])
#cdf 누적밀도함수
rv.cdf([0,1])
rv.mean(), rv.var()


##베르누이 분포끝-----------------------------------------------------------------------------------------

#2.이항분포
#성공확률이 p인 베르누이 시행을 n번 했을때의 성공 횟수가 따르는 분포
#ex) 동전 10번 던져서 앞면이 3번 나올 확률
#ex)주사위를 4번 굴려서 6이 한번도 나오지 않을 확률
#nCr = n!/(r!(n-r)!) 서로다른 n에서 r개를 순서에 상관없이 조합하는 수
#이항분포 Bin(n,p)
#기댓값 E(X)=np, 분산 V(X)=np(1-p)

#6C2 => 학생 6명 2명을 뽑는 조합 콤비네이션 연습
from scipy.special import comb
comb(6,2)



def Bin(n,p) :
    x_set = np.arange(n+1)
    #이항분포의 확률함수
    def f(x) :
        if x in x_set:
            return comb(n,x)*p**x*(1-p)**(n-x)
        else :
            return 0
    return x_set, f

n=10
p=0.3
X = Bin(n,p)
check_prob(X)
plot_prob(X)


##이항분포를 scipy로 사용

rv = stats.binom(10,0.3)
rv.pmf(3)

#p를 0.3, 0.5, 0.7로 변화시키면서 이항분포가 어떻게 형성되는지 보기
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
x_set = np.arange(n+1)
for p, ls in zip([0.3,0.5,0.7], linestyles) :
    rv = stats.binom(n,p)
    ax.plot(x_set, rv.pmf(x_set), label=f'p:{p}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()

##이항분포 끝 ------------------------------------------------------------------------------------------

#3.기하분포 
# 베르누이 시행에서 처음 성공할때까지 반복한 시행횟수가 따르는 분포
# Ge(p)
# 확률변수가 취할수 있는값 1이상의 전체 정수
# (처음 성공 할수도 있고, 연달아서 계속 실패할수도 있다.)
# ex)동전을 던져서 5번째에서 처음으로 앞면이 나올 확률
# ex) 주사위를 세번 굴려서 처음으로 6이 나오는 확률
# 
# 기하분포의 기대값과 분산
# E(X)=1/p,V(X)=(1-p)/p^2
#  

def Ge(p):
    x_set = np.arange(1,30)#편의상 30까지
    def f(x) :
        if x in x_set:
            return p*(1-p)**(x-1)
        else :
            return 0
    return x_set, f

p=0.5
X=Ge(p)
X[0],X[1]
X[1](5)#동전을 던져서 5번째에 처음으로 앞면이 나올 확률
check_prob(X)
plot_prob(X)

#scipy함수에서 지원됨

rv = stats.geom(p)
rv.pmf(5)
#p = 0.2,0.5,0.8 경우 기하분포 그리기

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
x_set = np.arange(1,15)
for p, ls in zip([0.2,0.5,0.8], linestyles) :
    rv = stats.geom(p)
    ax.plot(x_set, rv.pmf(x_set), label=f'p:{p}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()

##p값이 무엇이든 확률변수값이 커질수록 확률은 지수적으로 감소
##기하분포 끝-----------------------------------------------------------------------------------------------------------------------------

#4.포아송 분포
# 임의의 사건이 단위 시간당 발생하는 건수가 따르는 확룰 분포   
# x의 값은 발생하는 건수, {0,1,2,3,.....} 0이상의 정수
#Poi(lambda), lambda 단위시간당 평균 발생건수
# ex)하루에 평균 2건의 교통사고가 발생하는 지역에서, 하루 교통사고 발생건수
#Poi(2)를 따른다.

#확률함수 만들기
#Poi(2)를 따를때 하루동안 교통사고가 한건도 발생하지 않을 경우
from scipy.special import factorial
2**(0)/factorial(0)*np.e**(-2)

#ex) 한시간에 평균10번 엑세스 하는 사이트에 대한 한 시간당 엑세스 건수
#한시간에 15번 엑세스가 발생할 확률
10**(15)/factorial(15)*np.e**(-10)

#Poi(lam) 의 기댓값과 분산
#E(X)=lam, V(X)=lam

def Poi(lam) :
    x_set = np.arange(20)#편의상
    #확률함수
    def f(x):
        if x in x_set:
            return (lam**x)/factorial(x)*np.exp(-lam)
        else :
            return 0
    return x_set, f

lam =3
X = Poi(lam)
check_prob(X)
plot_prob(X)

#scipy 에서 지원하는 함수
rv= stats.poisson(lam)
rv.pmf(10)

#lam = 3,5,8로 변할때 포아송 분포시각화

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
x_set = np.arange(20)
for lam, ls in zip([3,5,8], linestyles) :
    rv = stats.poisson(lam)
    ax.plot(x_set, rv.pmf(x_set), label=f'lam:{lam}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()

#분포의 정상에는 람다가 있고, 람다가 커질수록 경사면이 더욱 완만해짐


