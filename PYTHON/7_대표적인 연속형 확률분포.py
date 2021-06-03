#1.정규분포 - 평균 u이고, 표준편차 sigma인 x의 확률밀도함수
#2.지수분포 - 어떤 사건이 발생할 때까지 경과 시간에대한 확률분포
#3.카이제곱분포 - 모분산의 추정, 두 집단의 독립성 검정
#4.t분포 - 모평균 추정, 두 집단의 평균 동일성 검정
#5.F분포 - 두 집단의 분산 동일성 검정

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate
from scipy.optimize import minimize_scalar

linestyles = ['-', '--', ':']

def E(X, g=lambda x: x):
    x_range, f = X
    def integrand(x):
        return g(x) * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]

def V(X, g=lambda x: x):
    x_range, f = X
    mean = E(X, g)
    def integrand(x):
        return (g(x) - mean) ** 2 * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]

def check_prob(X):
    x_range, f = X
    f_min = minimize_scalar(f).fun
    assert f_min >= 0, 'density function is minus value'
    prob_sum = np.round(integrate.quad(f, -np.inf, np.inf)[0], 6)
    assert prob_sum == 1, f'sum of probability is {prob_sum}'
    print(f'expected vaue {E(X):.3f}')
    print(f'variance {V(X):.3f}')
    
def plot_prob(X, x_min, x_max):
    x_range, f = X
    def F(x):
        return integrate.quad(f, -np.inf, x)[0]

    xs = np.linspace(x_min, x_max, 100)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.plot(xs, [f(x) for x in xs],
            label='f(x)', color='gray')
    ax.plot(xs, [F(x) for x in xs],
            label='F(x)', ls='--', color='gray')
    ax.legend()
    plt.show()

#1.정규분포(가우스 분포)
#통계분석에 매우 자주 사용되는 중요한 확률분포
#자연계에서 일어나는 많은 현상을 표현할 수 있다.
#정규분포는 평균과 표준편차 지표가 필요하다.

#정규분포의 변환
#X ~ N(평균, 분산)
#aX+b ~ N(a*평균+b, a^2*분산)

#정규화 Z=(X-평균)/표준편차
#평균 0, 분산 1
#표준정규분포

def N(mu, sigma) :
    x_range = [-np.inf, np.inf]
    def f(x) :
        return 1/np.sqrt(2*np.pi*sigma**2)*\
            np.exp(-(x-mu)**2/(2*sigma**2))
    return x_range, f

#ex) 남자 고등학생의 키 평균 170cm, 표준차 5cm
#우연히 만난 남자 고등학생의 키가 165~175일 확률
#P(165<=X<=175)
x_range, f = N(170,5)
integrate.quad(f, 165, 175)[0] #68%

#모의고사 평균점수가 70점, 표준편차 8점일때
#우연히 만난 학생의 점수가 54~86점일 확률

#90점맞은 학생의 상위 몇%인지
x_range, f = N(70,8)
integrate.quad(f, 90, np.inf)[0]

mu, sigma=2, 0.5
X=N(mu,sigma)
check_prob(X)

#밀도함수 x구간을 0<=x<=4로 그래프 시각화
plot_prob(X,0,4)

#scipy.stats (norm함수)
rv = stats.norm(mu,sigma)
rv.mean(), rv.var()
rv.pdf(2) #P(X=2) 
integrate.quad(rv.pdf, -np.inf, np.inf)[0]

#어느 회사의 500명의 직원들 근무 평균기간 7년, 표준편차 2년
#이 회사에서 10년이상 근무한 직원의 수 (정규분포를 따른다고 가정)
mu,sigma = 7,2
rv = stats.norm(mu,sigma)
integrate.quad(rv.pdf, 10, np.inf)[0]
X = N(mu,sigma)
plot_prob(X, 10,30)

#누적밀도 함수이용 확률구하기
rv.cdf(np.inf)
(1-rv.cdf(10))*500

#상위 a%인 확률의 x값을 구할때 - isf 메서드활용
#P(X>=x)=a
rv.isf(0.3) #8년이상 근무한 사람들은 30%정도 된다.

#확률 a가 되는 가운데 부분 구간 얻기
rv.interval(0.9) 
rv.isf(0.95), rv.isf(0.05)

#(0,1), (0,2), (1,1) 정규분포의 분포 변화도를 보기
params = [(0,1),(0,2),(1,1)]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.linspace(-5,5,100)
for param, ls in zip(params, linestyles):
    mu, sigma = param
    rv = stats.norm(mu, sigma)
    ax.plot(xs, rv.pdf(xs), label=f'N({mu},{sigma**2})',
        ls=ls, color='gray')
ax.legend()
plt.show()

#2.지수분포
#어떤 사건이 발생한뒤 다음 사건이 일어날 때까지 대기시간이 따르는 분포
#X ~ Ex(lam), E(X)=1/lam, V(X)=1/(lam**2)

#ex) 하루 평균 2건의 교통사고 발생하는 지역에서
#교통사고가 발생한후 3일 이내에 또 교통사고가 발생할 확률

def Ex(lam) :
    x_range = [0, np.inf]
    def f(x) :
        if x>=0 :
            return lam*np.exp(-lam*x)
        else :
            return 0
    return x_range, f

x_range, f = Ex(2)
#P(X<=3)
integrate.quad(f,0,3)[0] #99.7%
X = Ex(2)
check_prob(X)
plot_prob(X,0,3)

#람다 1,2,3에 따른 분포 형태 변화 시각화
params = [1,2,3]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.linspace(0,3,100)
for lam, ls in zip(params, linestyles):
    rv = stats.expon(scale=1/lam)
    ax.plot(xs, rv.pdf(xs), label=f'lamda:{lam}',
        ls=ls, color='gray')
ax.legend()
plt.show()

#어느 회사에서 생산하는 배터리 수명시간이 3년이고, 지수분포를 따를때
#이 배터리의 수명시간이 5년이상 지속될 확률
lam = 1/3
rv = stats.expon(scale=1/lam)
integrate.quad(rv.pdf, 5, np.inf)[0] #18.9%
1-rv.cdf(5)

#어느 회사에서 전자제품의 평균수명 3년이고, 보증기간 1년일때
#전자제품이 1년이내에 고장나서, 보상받을 확률
lam = 1/3
rv = stats.expon(scale=1/lam)
integrate.quad(rv.pdf, 0, 1)[0] #28%
rv.cdf(1)

#어느 병원의 진료 대기시간이 평균 8분일때, 
#대기시간이 4분에서 11분일 사이일 확률
lam = 1/8
rv = stats.expon(scale=1/lam)
integrate.quad(rv.pdf, 4, 11)[0] #35%
rv.cdf(11)-rv.cdf(4)

#3.카이제곱분포
#추정과 검정에 사용하는 특수한 확률분포
#분산추정이나, 독립성 검정에 사용된다.
#확률변수가 취할 수 있는 값 0이상, 파라미터 n인 자유도(샘플개수)
#분산의 특징을 확률분포로 만든 것이다.
#자유도가 커질수록(샘플 개수가 커질수록) 좌우대칭에 가까워진다.
#자유도 값 가까이에 분포의 정점이 있다.

#자유도 10인 카이제곱분포에서 무작위추출한 표본크기 100만의 표본 데이터
n=10 
rv=stats.norm() #표준정규분포생성
rv.mean(), rv.var()
sample_size = int(1e6) #백만개
#샘플 10개의 표준정규분포에서 표본 크기 100만으로 무작위 추출
Zs_sample = rv.rvs((n, sample_size))
Zs_sample.shape

chi2_sample = np.sum(Zs_sample**2, axis=0)
chi2_sample.shape

#10개 샘플의 표준정규분포 제곱합이므로 자유도가 10인 카이제곱분포가 됨
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv = stats.chi2(n)
xs = np.linspace(0,30,100)
ax.hist(chi2_sample, bins=100, density=True, alpha=0.5, 
        label='chi2_sample')
ax.plot(xs, rv.pdf(xs), label=f'chi2({n})', color='gray')
ax.set_xlim(0,30)
ax.legend()
plt.show()

#카이제곱 자유도 n=3,5,10 변화 분포변화 시각화
params = [3,5,10]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.linspace(0,20,500)
for n,ls in zip(params, linestyles) :
    rv = stats.chi2(n)
    ax.plot(xs, rv.pdf(xs), label=f'chi2({n})',
        color='gray', ls=ls)
ax.legend()
plt.show()

#카이제곱 분포 특징
#좌우비대칭으로, 왼쪽으로 치우치고 오른쪽으로 넓어짐
#자유도가 커질수록 좌우대칭이 가까워짐
#자유도의 값 가까이에 분포의 정점이 있다.

#자유도 5인 카이제곱분포에서 상위 5%인 x의 값을 얻기
rv = stats.chi2(5)
#P(X>=x)=0.05인 x의 값 얻기
rv.isf(0.05) 
integrate.quad(rv.pdf, rv.isf(0.05), np.inf)[0]

#4.t분포
#정규분포에서 모평균의 구간추정등에 사용하는 확률분포
#정규분포보다 한 단계 예측범위가 넓은 분포
#샘플개수 30개 이상일 때는 정규분포로 추정
#샘플개수 30개 이하일 때 t분포로 추정
#t= Z/(sqrt(Y/n))

#자유도가 10인 t분포
sample_size = int(1e6)
n=10
rv1 = stats.norm()
rv2 = stats.chi2(n)
Z_sample = rv1.rvs(sample_size)
chi2_sample = rv2.rvs(sample_size)
t_sample = Z_sample/np.sqrt(chi2_sample/n)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv = stats.t(n)
xs = np.linspace(-3,3,100)
ax.hist(t_sample, bins=100, range=(-3,3), density=True,
    alpha=0.5, label='t_sample')
ax.plot(xs, rv.pdf(xs), label=f't({n})', color='gray')
ax.legend()
ax.set_xlim(-3,3)
plt.show()

#t분포 자유도 n=3,5,10으로 변화시키고 표준정규분포와 함께 시각화
params = [3,5,10]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.linspace(-3,3,100)
for n,ls in zip(params, linestyles) :
    rv = stats.t(n)
    ax.plot(xs, rv.pdf(xs), label=f't({n})',
        color='gray', ls=ls)
rv = stats.norm()
ax.plot(xs, rv.pdf(xs), label=f'N(0,1)')
ax.legend()
plt.show()

#t분포 특징
#표준정규분포보다 양쪽 끝이 두껍다
#자유도가 커지면 표준정규분포에 가까워진다.
#좌우 대칭이다.

#자유도 10인 t분포에서 95%확률의 x값 범위(중심으로부터)
rv = stats.t(10)
rv.interval(0.95)
rv.isf(1-0.025), rv.isf(0.025)

#5.F분포
#분산분석 등에 사용되는 확률분포
#카이제곱분포는 한집단의 분산을 다뤘다면, F분포 두 집단의 분산을 다룬다.
#두집단의 분산을 나눠서 비교를 함 (1에 가까우면 두 집단의 분산이 같다.)

#Y1=chai(5), Y2=chai(10), F분포 생성
n1,n2 = 5,10
rv1 = stats.chi2(n1)
rv2 = stats.chi2(n2)
sample_size = int(1e6)
sample1 = rv1.rvs(sample_size)
sample2 = rv2.rvs(sample_size)

f_sample = (sample1/n1)/(sample2/n2)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
rv = stats.f(n1,n2)
xs = np.linspace(0,6,200)
ax.hist(f_sample, bins=100, range=(0,6), density=True,
    alpha=0.5, label='f_sample')
ax.plot(xs, rv.pdf(xs), label=f'F({n1},{n2})',color='gray')
ax.legend()
ax.set_xlim(0,6)
plt.show()

#F분포 n2=10고정 , n1=3,5,10변화 시각화
params = [3,5,10]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.linspace(0,6,200)
for n,ls in zip(params, linestyles) :
    rv = stats.f(n, 10)
    ax.plot(xs, rv.pdf(xs), label=f'f({n})',
        color='gray', ls=ls)
ax.legend()
plt.show()

#F분포 특징
#좌우비대칭, 왼쪽으로 치우치고 오른쪽으로 넓어지는 분포
#분포의 정점은 1에 가깝다
#자유도가 커지면(표본수가 많아지면) 1을 중심으로 대칭적으로 분포한다.






