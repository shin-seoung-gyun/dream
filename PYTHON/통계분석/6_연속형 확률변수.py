# 1. 1차원 연속형 확률변수
# 2. 2차원 연속형 확률변수

# 연속형 확률변수 : 확률변수가 취할 수 있는 값이 연속적인 확률변수
# 특정 값을 취하는 확률은 정의되지 않음
# 확률변수가 어느 구간에 들어가는지 확률을 정의
#1. 1차원 연속형 확률 변수
#(1) 1차원 확률변수의 정의
#확률밀도함수(밀도함수), 확률변수가 취할 수 있는 값은 구간 [a,b]로 정의
#p(x0<=x<=x1) = f(x)의 면적 (x0<=x<=x1)

# ex) 불공정 룰렛
# 룰렛의 둘레의 길이 1, 룰렛이 취할수 있는값 0~1
# 큰수일수록 나오기 쉬워지는 불공정 구조로 되어있는 경우
# 둘레의 0.5위치에서 확률 0
# 시작점에서 둘레의 길이가 0.4~0.6일때 확률은 0.2//예시

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate # 적분에서 사용하는 함수

x_range = np.array([0,1])#둘레의 길이 0~1
def f(x):
    if x_range[0] <= x <= x_range[1]:
        return 2*x
    else :
        return 0
X = [x_range,f]
#x가 0.4~0.6일때 확률값
integrate.quad(f,0.4,0.6) #0.2
#(0.19999999999999996, 2.2204460492503127e-15)
integrate.quad(f,0.4,0.6)[0]
#시각화
area = round(integrate.quad(f,0.4,0.6)[0],1)
area
xs = np.linspace(x_range[0],x_range[1],100)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
#확률밀도 함수 그래프
ax.plot(xs,[f(x)for x in xs],label='f(x)', color='gray')
#수평선
ax.hlines(0,-0.2,1.2,alpha=0.3)#y시작위치, x시작, x끝, alpah 투명도
#수직선
ax.vlines(0,-0.2,2.2,alpha=0.3)#x시작위치, y시작, y끝, alpah 투명도
#0.4~0.6까지 f(x)면적을 색칠
xs = np.linspace(0.4,0.6,100)
#xs의 범위로 f(x)와 x축으로 둘러싸인 영역에 색넣기
ax.fill_between(xs, [f(x)for x in xs], label='prob', color='g')
ax.text(0.49,0.5,area,fontsize=10)

ax.set_xticks(np.arange(-0.2,1.3,0.1))
ax.set_xlim(-0.1,1.1)
ax.set_ylim(-0.2,2.1)
ax.legend()
plt.show()

##연속형 확률변수의 성질
#f(x) >= 0
#정의역에서 정의된 f(x)의 면적 = 1

from scipy.optimize import minimize_scalar
res = minimize_scalar(f)
res.fun#함수의 최소값

integrate.quad(f,-np.inf,np.inf)[0]

#누적분포 함수
#F(x) 확률변수 X가 x이하가 될때의 확률을 반환하는함수
def F(x):
    return integrate.quad(f,-np.inf,x)[0]
F(0.6) #0.36
#P(0.4<=X<0.6)=F(0.6)-F(0.4)
F(0.6)-F(0.4)

#누적분포함수 시각화
xs = np.linspace(x_range[0],x_range[1],100)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
#누적분포함수
ax.plot(xs,[F(x)for x in xs],label='F(x)', color='gray')
#수평선
ax.hlines(0,-0.2,1.2,alpha=0.3)#y시작위치, x시작, x끝, alpah 투명도
#수직선
ax.vlines(0,-0.2,2.2,alpha=0.3)#x시작위치, y시작, y끝, alpah 투명도
##수직선하나더
ax.vlines(xs.max(),0,1, linestyle=':',color='gray')

ax.set_xticks(np.arange(-0.1,1.2,0.1))
ax.set_xlim(-0.1,1.1)
ax.set_ylim(-0.1,1.1)
ax.legend()
plt.show()

##확률변수의 변환
# Y=2X+3
# Y의 확률밀도 함수 g(y)= (y-3)/2 (3<=y<=5)
# 확률분포 G(y)

#(2) 1차원 연속형 확률변수 지표
#기대값
def integrand(x):
    return x*f(x)

integrate.quad(integrand, -np.inf, np.inf)[0]
#풀공정 룰렛의 경우 기대값 0.67

#Y=2X+3로 변환한 확률변수의 기대값
def E(X, g=lambda x:x):
    x_range, f = X
    def integrand(x) :
        return g(x)*f(x)
    return integrate.quad(integrand, -np.inf,np.inf)[0]
E(X)# 0.67
E(X, g=lambda x:2*x+3)# 4.33
#기대값의 선형성
#E(aX+b)=aE(X)+b
2*E(X)+3

#분산 
mean = E(X) 
def integrand(x):
    return (x-mean)**2*f(x)
integrate.quad(integrand, -np.inf, np.inf)[0]#0.056

def V(X, g=lambda x:x):
    x_range, f = X
    mean = E(X,g)
    def integrand(x):#피적분함수
        return (g(x)-mean)**2*f(x)
    return integrate.quad(integrand,-np.inf, np.inf)[0]
V(X)
V(X, lambda x:2*x+3)
#V(2X+3)==2^2*V(X)
2**2*V(X)

###1차원 연속형 확률변수 끝 ----------------------------------------------------------------------------------------####































































































































