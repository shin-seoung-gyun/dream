#1. 1차원 이산형 확률변수 - 취할수 있는 값이 이산적인 확률변수 ex) 주사위 1개의 1~6까지의 숫자가 나올 확률

#2. 2차원 이산형 확률변수
# ex) 주사위 2개 나온 눈의 합이 확률변수인 경우

#1. 1차원 이산형 확률변수
#(1) 확률질량함수(확률함수)
#f(x) = p(X=x), X={x1,x2,x3,....}

#확률질량함수를 통해 확률분포
#확률분포 : 확률변수가 취할수 있는 값과 그 확률의 구체적인 대응

#불공정 주사위의 확률 분포
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x_set= np.array([1,2,3,4,5,6])#확률변수


def f(x) : # 확률질량함수
    if x in x_set :
        return x/21
    else :
        return 0

#확률분포 - 시각화
prob = np.array([f(x) for x in x_set])
dict(zip(x_set, prob))

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.bar(x_set,prob)
ax.set_xlabel('value')
ax.set_ylabel('probablity')
plt.show()

#확률 성질 - 확률값은 0이상, 모든 확률의 합 1
np.all(prob>=0)#모든요소가 참일때 참을 반환
np.sum(prob)

#누적분포함수 - 확률변수가 X가 x이하일때의 확률을 반환
def F(x):
    return np.sum([f(x_k)for x_k in x_set if x_k <=x])
F(3)

#확률변수의 변환 
#Y= 2X+3
#Y=5,7,9...
#확률변수를 표준화 할때 중요한 연산
y_set = np.array([2*x+3 for x in x_set])
y_set
prob = np.array([f(x)for x in x_set])
dict(zip(y_set,prob))

#(2) 1차원 이산형 확률변수의 지표
#기댓값 : 확률변수의 평균이란 확률변수를 무수히 시행하여 얻어진 실현값의 평균
#EX) 주사위를 무한번 굴려 얻은 눈의 평균값
sample = np.random.choice(x_set, int(1e6), p=prob)
sample
sample.shape
np.mean(sample)

#이산형 확률변수의 평균 : 확률변수가 취할수 있는 값과 그 확률의 곱의 총합
np.sum([x*f(x) for x in x_set])#이론값
X=[x_set,f]
def E(X, g=lambda x:x) :
    x_set, f = X #언패킹
    return np.sum([g(x)*f(x) for x in x_set])
E(X, lambda x:x)
E(X)

#확률변수 Y=2X+3의 기댓값
E(X, lambda x:2*x+3)

#기대값의 선형성
#E(aX+b) = aE(X)+b
2*E(X)+3

#이산형 확률변수의 분산
#편차제곱*f(x)의 합
mean = E(X)
np.sum([(x-mean)**2*f(x) for x in x_set])

#주사위 눈 3.5
# ((1-3.5)**2+ (2-3.5)**2+(3-3.5)**2+(4-3.5)**2+(5-3.5)**2+(6-3.5)**2)/6

#이산형 확률변수의 분산 함수 만들기
def V(X, g=lambda x:x):
    x_set, f = X
    mean = E(X,g)
    return np.sum([(g(x)-mean)**2*f(x) for x in x_set])
V(X)

#Y=2X+3의 분산
V(X, lambda x: 2*x+3)#8.889
#분산공식 : V(aX+b) = a^2V(X)
2**2*V(X)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2. 2차원 이산형 확률변수
#결합확률분포 - 2차원 확률변수에서는 1차원 확률분포를 동시에 다룬다.(X,Y)
#확률분포 - 확률변수의 움직임은 취할수 있는 값의 집합과 그 확률에 의해 정해짐
#
# 불공정 주사위를 2개를 굴리는 경우 (A,B)
# A의 눈 확률변수 X, B의 눈 확률변수 Y
# X=X+Y Y=Y 재정의
# X가 취할수 있는 값 2~12
# Y가 취할수 있는 값 1~6
# X=9이고, Y=4일때 확률 => X가 5일때의 확률과 Y=4일때의 곱
# => (5/21)*(4/21)
x_set = np.arange(2,13)
y_set = np.arange(1,7)

def f_XY(x,y):
    if (1<=y<=6) and (1<=x-y<=6) :
        return y/21 * (x-y)/21
    else :
        return 0
XY= [x_set,y_set,f_XY]

#확률분포 히트맵 시각화 (2차원)
prob = np.array([[f_XY(x,y)for y in y_set]for x in x_set])
prob.shape

#확률의 성질 확인
np.all(prob>=0)
np.sum(prob)

fig = plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)
c = ax.pcolor(prob, cmap='Reds')
#prob.shape[1]=6 (0~5)+0.5
ax.set_xticks(np.arange(prob.shape[1])+0.5, minor=False)#minor 세분화된 틱 제거 ex)1.5
#prob.shape[0]=11 (0~10)+0.5
ax.set_yticks(np.arange(prob.shape[0])+0.5, minor=False)
ax.set_xticklabels(np.arange(1,7),minor=False)
ax.set_yticklabels(np.arange(2,13),minor=False)
#y축이 내림차순의 숫자되도록 위 아래 역전
ax.invert_yaxis()
#x축 눈금 그래프 위쪽 표시
ax.xaxis.tick_top()
#컬러바 표시
fig.colorbar(c, ax=ax)

plt.show()

#주변확률분포(주변분포) - 확률변수 (X,Y)는 결합분포에 의해 동시에 정의 되지만,
#확률변수 X의 확률함수 f(x)를 알고싶을때
#f_XY에서 X=x 일때, Y가 취할수 있는 모든 값의 각각의 확률을 더한다
#y의 영향력 제거

def f_X(x):
    return np.sum([f_XY(x,y) for y in y_set])
def f_Y(y):
    return np.sum([f_XY(x,y) for x in x_set])

#막대그래프로 시각화
X = [x_set, f_X]
Y = [y_set, f_Y]
prob_x = np.array([f_X(x)for x in x_set])
prob_y = np.array([f_Y(y)for y in y_set])
prob_x
prob_y
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,4))
axes[0].bar(x_set,prob_x)
axes[0].set_title('X_marginal probablity distribution')
axes[0].set_xlabel('X_value')
axes[0].set_ylabel('Probability')

axes[1].bar(y_set,prob_y)
axes[1].set_title('Y_marginal probablity distribution')
axes[1].set_xlabel('Y_value')
axes[1].set_ylabel('Probability')
plt.show()

#(2) 2차원 이산형 확률변수의 지표
#X의 기댓값
np.sum([x*f_XY(x,y)for x in x_set for y in y_set])

def E(XY,g):
    x_set, y_set, f_XY = XY
    return np.sum([g(x,y)*f_XY(x,y)for x in x_set for y in y_set])

mean_X = E(XY, lambda x,y:x)
mean_y = E(XY, lambda x,y:y)
mean_X,mean_y

#기댓값 선형성
#E(aX+bY) = aE(X)+bE(Y)
a,b =2,3
E(XY, lambda x,y:a*x+b*y)
a*mean_X+b*mean_y

#분산
#X의 분산은 편차 제곱의 기대값
np.sum([(x-mean_X)**2*f_XY(x,y)for x in x_set for y in y_set])

def V(XY, g) :
    x_set, y_set, f_XY =XY
    mean = E(XY, g)
    return np.sum([(g(x,y)-mean)**2*f_XY(x,y)for x in x_set for y in y_set])
var_X = V(XY, g=lambda x,y:x)
var_Y = V(XY, g=lambda x,y:y)
var_X, var_Y

#공분산 값
def Cov(XY):
    x_set, y_set, f_XY =XY
    mean_X = E(XY, g=lambda x,y:x)
    mean_Y = E(XY, g=lambda x,y:y)
    return np.sum([(x-mean_X)*(y-mean_Y)*f_XY(x,y)for x in x_set for y in y_set])

cov_xy = Cov(XY)
cov_xy

#분산 공식
#V(aX+bY) = a^2*V(X)+b^2*V(Y) + 2/a*b*Cov(X,Y)
#V(2X+3Y) = 4V(X)+9V(Y)+12*Cov(XY)
a,b = 2,3
V(XY, lambda x,y:a*x+b*y)
a**2*var_X+b**2*var_Y+2*a*b*cov_xy

#상관계수 = 공분산 / 각각 표준편차의 곱
cov_xy/np.sqrt(var_X*var_Y)

