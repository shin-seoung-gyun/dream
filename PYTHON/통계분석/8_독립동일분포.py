#확률변수가 독립이라는 것은 확률변수가 다른 확률변수에 영향을 끼치지 않는다는 의미
#동립동일분포 : 서로 독립이고 각각 동일한 확률분포를 따르는 다차원 확률 변수
#ex) 한 학년에서 우연히 만난 20명의 점수에 대한 분포
#(X1,X2,X3,...,X20) 서로 독립인 20차원 확룰변수


#통계분석하는 가장 기본적이고 중요한 조건 설정
# 동일한 조건에서 수행되는 실험이나 관측을 여러번 반복해서 데이터를 얻는것을 
#수학용어로 나타냄

#1. 독립성
#2. 합의 분포
#3. 표본 평균의 분포
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

linestyles = ['-', '--', ':', '-.']

def E(XY, g):
    x_set, y_set, f_XY = XY
    return np.sum([g(x_i, y_j) * f_XY(x_i, y_j)
                   for x_i in x_set for y_j in y_set])

def Cov(XY):
    x_set, y_set, f_XY = XY
    mean_X = E(XY, lambda x, y: x)
    mean_Y = E(XY, lambda x, y: y)
    return np.sum([(x_i-mean_X) * (y_j-mean_Y) * f_XY(x_i, y_j)
                    for x_i in x_set for y_j in y_set])

def f_X(x):##주변확률분포
    return np.sum([f_XY(x, y_k) for y_k in y_set])

def f_Y(y):##주변확률분포
    return np.sum([f_XY(x_k, y) for x_k in x_set])

##
#1. 독립성
#확률변수의 독립성이란, 2개의 이상의 확률변수가 서로 영향을 끼치지 않으며
#관계가 없음을 나타내는 개념
#확률변수가 독립일때 결합확률은 주변확률의 곱

#독립성과 무상관성의 차이(공분산, 상관계수)
#결론 : 독립성이 더 강한 개념
#2개의 확률변수 X,Y가 독립일때 X,Y는 무상관이 되지만,
#X,Y가 무상관일때 X와 Y가 반드시 독립인 것은 아니다.


#두 변수가 무상관인데 독립인 경우
x_set = np.array([1,2,3,4,5,6])
y_set = np.array([1,2,3,4,5,6])

def f_XY(x,y):
    if x in x_set and y in y_set :
        return (x/21)*(y/21)
    else :
        return 0
XY=[x_set, y_set, f_XY]
Cov(XY)#무상관


#두 변수가 무상관인데 독립이 아닌경우

x_set = np.array([0,1])
y_set = np.array([-1,0,1])
def f_XY(x,y):
    if (x,y) in [(0,0),(1,1),(1,-1)]:
        return 1/3
    else :
        return 0
XY=[x_set,y_set,f_XY]
Cov(XY)
f_XY(0,0), f_X(0)*f_Y(0)
#공분산 값은 0이지만 x,y는 독립이 아니다.

#2. 합의 분포
#합의 값 자체가 확률변수
#ex) 학년의 모평균을 추정하기 위해 X1,X2,X3,....,X20의 점수를
#무작위로 얻고 생플합을 개수로 나누면 평균값이 된다.
#표본평균의 확률분포를 이해하기 위한 기초

#확률변수 X1,X2,X3,....,X20이 서로 독립일 경우
#E(X1+X2+...+XN)=E(X1)+E(X2)+....+E(Xn)
#V(X1+X2+...+XN)=V(X1)+V(X2)+....+V(Xn)

#(1) 정규분포의 합의 분포
#X~N(1,2)와 Y~N(2,3) X+Y의 분포
rv1=stats.norm(1,np.sqrt(2))
rv2=stats.norm(2,np.sqrt(3))
sample_size = int(1e6)
X_sample = rv1.rvs(sample_size)
Y_sample = rv2.rvs(sample_size)
sum_sample = X_sample+Y_sample

np.mean(sum_sample), np.var(sum_sample)


#재생성(reproductive property)
#동일한 분포를 따르는 두개의 확률변수의 합도 동일한 확률분포다.
#정규분포 + 정규분포 => 정규분포
#모든 확률분포가 재생성의 속성을 갖는것은 아니다.

#N(5,3) 분포와 함께 시각화
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv=stats.norm(3,np.sqrt(5))
xs = np.linspace(rv.isf(0.995), rv.isf(0.005),100)

ax.hist(sum_sample, bins=100, density=True, alpha=0.5, label='N(1,2)+N(2,3)')
ax.plot(xs,rv.pdf(xs),label='N(3,5)', color='gray')
ax.plot(xs,rv1.pdf(xs),label='N(1,2)', color='gray',ls='--')
ax.plot(xs,rv2.pdf(xs),label='N(2,3)', color='gray',ls=':')
ax.legend()
ax.set_xlim(rv.isf(0.995),rv.isf(0.005))
plt.show()


#(2) 포아송 분포의 합의 분포(이산형확률분포)
#서로 독립인 두 확률변수 X~Poi(3), Y~Poi(4)
#X+Y의 분포
#이론적으로는 평균 7 , 분산 7

rv1=stats.poisson(3)
rv2=stats.poisson(4)
sample_size = int(1e6)
X_sample = rv1.rvs(sample_size)
Y_sample = rv2.rvs(sample_size)
sum_sample = X_sample+Y_sample

np.mean(sum_sample), np.var(sum_sample)

# Poi(7)과 함께 시각화

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv=stats.poisson(7)
xs = np.arange(20)
hist,_ = np.histogram(sum_sample,bins=20,range=(0,20), normed=True)
ax.bar(xs,hist,alpha=0.5,label='Poi(3)+Poi(4)')
ax.plot(xs,rv.pmf(xs),label='Poi(7)', color='gray')
ax.plot(xs,rv1.pmf(xs),label='Poi(3)', color='gray',ls='--')
ax.plot(xs,rv2.pmf(xs),label='Poi(4)', color='gray',ls=':')
ax.legend()
ax.set_xlim(-0.5,20)
ax.set_xticks(np.arange(20))
plt.show()


#(3)베르누이 분포의 합의 분포
#p=0.3 베르누이 분포10개의 합의 분포
#이론 기대값 p*0.3=3 분산 p*(1-p)*10= 2.1
p=0.3
rv=stats.bernoulli(p)
sample_size = int(1e6)
Xs_sample = rv.rvs((10,sample_size))
Xs_sample.shape
sum_sample = np.sum(Xs_sample,axis=0)#행방향
sum_sample.shape
np.mean(sum_sample), np.var(sum_sample)
#(2.998394, 2.0981774207640007)

#베르누이 분포는 재생성이 없다.
#베르누이 분포의 합은 이항분포가 

#이항분포 Bin(10,0.3) 함께 시각화

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv=stats.binom(10,p)#이항분포
xs = np.arange(20)
hist,_ = np.histogram(sum_sample,bins=10,range=(0,10), normed=True)
ax.bar(xs,hist,alpha=0.5,label='Sum of 10 Bern(10)')
ax.plot(xs,rv.pmf(xs),label='Bin(10,0.3)', color='gray')
ax.legend()
ax.set_xlim(-0.5,10)
ax.set_xticks(np.arange(10))
plt.show()

#3. 표본 평균의 분포
#확률변수 X1,X2,...Xn 이 서로 독립이고,
# 기댓값이 m, 분산이 v 인 확률분포 F를 따를때
#표본 평균 Xbar의 평균 = m, 분산 = v/n

#(1) 정규 분포의 표본 평균
#X~N(1,2) , 샘플갯수 n=10
# 표본 평균의 평균값 = 1
# 표본 평균의 분산값 = 2/10 = 0.2

mean = 1
var = 2
rv = stats.norm(mean, np.sqrt(var)) 
n=10
sample_size = int(1e6)
Xs_sample = rv.rvs((n,sample_size))
sample_means = np.mean(Xs_sample, axis=0)#행방향
sample_means.shape#표본평균값들이 총 1000000개 있음
np.mean(sample_means), np.var(sample_means)
#(0.9993086508361346, 0.20012634436108118)

#모집단이 정규분포의 경우, 표본평균 xbar도 정규분포가 된다.
#xbar~N(1,0.2)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv = stats.norm(mean, np.sqrt(var/n))
xs= np.linspace(rv.isf(0.999), rv.isf(0.001),100)
ax.hist(sample_means, bins = 100, density=True, alpha=0.5, label='sample mean of 10*N(1,2)')
ax.plot(xs, rv.pdf(xs), label = 'N(1,0.2)')
ax.legend()
ax.set_xlim(rv.isf(0.999), rv.isf(0.001))
plt.show()

#(2) 포아송 분포의 표본평균 분포
#모집단 X~Poi(3)일때 n=10
#표본평균 의 평균값 = 3
#표본평균의 분산값 = 0.3
lam =3
rv = stats.poisson(lam) 
n=30
sample_size = int(1e6)
Xs_sample = rv.rvs((n,sample_size))
sample_means = np.mean(Xs_sample, axis=0)#행방향
sample_means.shape#표본평균값들이 총 1000000개 있음
np.mean(sample_means), np.var(sample_means)
#(2.9996219000000006, 0.29965120704039006)

#포아송분포는 표본평균에 대해 포아송 분포를 유지하지 않는다.
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.hist(sample_means, bins = 100, density=True, alpha=0.5, label='sample mean of 10*Poi(3)')
rv = stats.norm(3, np.sqrt(np.var(sample_means)))
xs = np.linspace(0,6,100)
ax.plot(xs, rv.pdf(xs), label=f'N(3, {np.var(sample_means):.1f})')
ax.legend()
ax.set_xlim(0,6)
plt.show()

#포아송 분포의 표본평균 분포는 근사적으로 정규분포를 따른다.
# N(3,0.3)

##(3) 중심극한정리
#모집단의 원래 분포가 뭐였든간에, 표본이 크면 (N>=30)
#표본평균의 분포(합의 분포)는 정규분포에 가깝다.

#모집단 Poi(3), 표본크기 10000
#이론적으로 표본 평균의 분포는 N(3, 3/10000)


lam =3
rv = stats.poisson(lam) 
n=10000
sample_size = 10000
Xs_sample = rv.rvs((n,sample_size))
sample_means = np.mean(Xs_sample, axis=0)#행방향
sample_means.shape
np.mean(sample_means), np.var(sample_means)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.hist(sample_means, bins = 100, density=True, alpha=0.5, label='sample mean of 10000*Poi(3)')
rv = stats.norm(3, np.sqrt(np.var(sample_means)))
xs = np.linspace(rv.isf(0.999),rv.isf(0.001),100)
ax.plot(xs, rv.pdf(xs), label=f'N(3, {np.var(sample_means):.1f})')
ax.legend()
ax.set_xlim(rv.isf(0.999),rv.isf(0.001))
plt.show()

#(4) 대수의 법칙
# 표본의 크기를 키우면 표본평균의 평균은 모평균에 수렴한다.
#ex)주사위의 눈이 6이나올 확률이 1/6에 수렴

p=1/6
rv = stats.bernoulli(p)
n = int(1e5)
sample=rv.rvs((n,4))
space = np.linspace(100, n, 50).astype(int)
plot_list = np.array([np.mean(sample[:sp], axis=0)for sp in space])
plot_list.shape
plot_list = plot_list.T
plot_list #샘플 수에 따른 표본 평균값 4그룹
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
for pl, ls in zip(plot_list, linestyles):
    ax.plot(space, pl,ls=ls, color='gray')
ax.hline(p,-1,n)
ax.set_xlabel('sample size')
ax.set_ylabel('sample mean')
plt.show()












































