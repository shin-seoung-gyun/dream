import matplotlib.pyplot as plt
import numpy as np ## 행렬 연산시 좋은 라이브러리 [딥러닝쪽]
from math import *
##(1)직선 그리기
# plot([x좌표리스트],[y좌표리스트])
plt.plot([1,2,3], [2,4,6])
#axis([x축 시작, x축 끝, y축 시작, y축 끝])
plt.axis([0,4,0,7])
plt.show()


x = np.arange(0.0,5.0,0.01)##소숫점 증감 가능
plt.plot(x, x**2, 'r--')
plt.plot(x, 3**x, 'b')
plt.axis([0,6,0,40])
plt.show()


x = np.arange(0.0,5.0,0.01)##소숫점 증감 가능 리스트처럼 생긴 수식이 가능한 다른 형
# print(type(x),x)
# y = x^2의 그래프
plt.subplot(221)
plt.plot(x,x**2,'r--')

# y=3^x 그래프
plt.subplot(222)
plt.plot(x,3**x,'b')

# y=x 그래프
plt.subplot(223)
plt.plot(x,x,'g-')

# y=1/(x+1) 그래프
plt.subplot(224)
plt.plot(x,1/(x+1),'y')
plt.show()


##그래프 상세히 그리기
plt.title('my graph')
plt.plot(x,x,'g', label='y=x')
plt.plot(x, 2*(x+1), 'r', label='y=2*(x+1')
#축 이름 붙이기
plt.xlabel('X Data')
plt.ylabel('y Data')
#범례표시
plt.legend()
#그래프눈금
plt.grid(True)
plt.show()

x = np.arange(0.0,2*np.pi,0.01)
y=np.sin(x)
plt.title('my graph')
#y =sin(x)빨강
#y = 3*sin(2*x)파랑
plt.plot(x,np.sin(x),'r',label='y =sin(x)')
plt.plot(x,3*np.sin(2*x),'b',label='y =3*sin(2*x)')
plt.xlabel('X Data')
plt.ylabel('y Data')
plt.legend()
plt.grid(True)
plt.show()
