#질적 변수와 양적 변수
#(1) 질적변수 - 선택이 필요한 변수, 종류를 구별하기 위한 변수
#ex) 설문지 - 1. 매우좋음 2. 좋음 3. 보통 4. 나쁨 5.매우나쁨
#명의 척도 : 단순 분류 ex) 학생번호, 전화번호, 성별, 혈액형
#순서 척도 : 순서 관계나 대소 관계에 의미가 있는 변수 ex) 설문지, 성적 순위


#(2)양적변수 - 양을 표현하는 변수
#간격 척도 - 대소 관계와 함께 그 차이도 의미를 두는 변수
#ex) 온도
#비례 척도 - 대소관계, 차이, 비례관계 모두 의미가 있는 변수
#ex) 키, 몸무게
#구분기준 - if(0=='없음') print('비례척도') else print('간격척도')

#이산형 변수와 연속형 변수
#(1) 이산형 변수 : 0,1,2,와 같이 하나하나의 값을 취하는 변수,
# 서로 인접한 숫자 사이에 값이 존재하지 않음
#ex) 주사위, 성적순위, 학생수, 결석수,

#(2) 연속형 변수 : 연속적인 값을 취할수 있는 변수
#ex) 길이, 무게, 시간

from numpy.core.fromnumeric import sort
import pandas as pd
df = pd.read_csv("./data/ch1_sport_test.csv")
df.info()
df

#학생번호 - 질적변수(명의척도)-이산형 변수
#학년 - 질적변수(순서척도), 이산형변수
#악력 - 양적변수(비례척도), 이산형변수(연속형으로 쓰이기도함)
#점수 - 양적변수(비례척도), 이산형
#순위 - 질적변수(순서척도), 이산형

#numpy(Numerical python) - 벡터와 행렬 연산 처리
#고성능의 수치계산을 할 수 있음

#자료형
#int(8,16,32,64) - 정수(부호가 있음)
#uint(8,16,32,64) - 정수(부호 없음)
#float(16,32,64,128) - 실수
#complex(64,128,256) - 복수
#bool - 참거짓
#문자열 - string
#object - 파이썬 클래스 객체
#unicode_ - 유니코드

import numpy as np
#(1) Array 정의 및 사용
data = [1,2,3,4,5]
arr1 = np.array(data)
arr1.shape #array의 크기
arr1.dtype #데이터타입

date2 = [1,1.5,2,2.5,4,5,6]
arr1 = np.array(date2)
arr1.shape #array의 크기
arr1.dtype #데이터타입

arr3 = np.array([[1,2,3],[4,5,6]])
arr3.shape #array의 크기
arr3.dtype #데이터타입

#(1-1) numpy 기본적인 함수
np.zeros(10)
np.zeros((3,5))
np.ones(10)
np.ones((3,5))
np.arange(10)
np.arange(3,10)
np.arange(3,10,0.1)
np.linspace(0,1,5)#시작 0 , 끝1, 요소5개 균등한 간격
#간격은 요소 개수 -1, 간격의 크기는 끝에서 시작값을 빼고 요소의 간격수로 나누면 나옴

np.random.randint(5,10,size=(2,4)) #5부터 10만이 정수

arr1= np.array([[1,2,3],[4,5,6]])
arr2= np.array(([[10,11,12],[13,14,15]]))
arr1+arr2
arr1-arr2
arr1*arr2
arr1/arr2

arr1*10
arr2**2

#array의 브로드캐스트
#행렬의 크기는 다르나 열의 개수가 같은 경우
arr1 = np.array([1,2,3],[4,5,6])
arr2 = np.array([10,11,12])
arr1+arr2
arr1-arr2
arr1*arr2
arr1/arr2

#(3)Array의 인덱싱
arr1 = np.arange(10)
arr1[0]
arr1[3:9]
arr1[::2]
arr1[::-1]

#(4)Array Boolean 인덱싱 마스크
names = np.array(['Beo','Beo','Kim','Joan','Lee','Beo'])
names_beo_mask = (names=='Beo')
names_beo_mask

names[names_beo_mask]
#randn함수는 기대값이 0이고 표준편차가 1인 정규분포에서 난수발생
data = np.random.randn(6)
data[names_beo_mask] #이름이 Beo인 사람의 Data

data = np.random.randn(6,4)
data[names_beo_mask,:]


data = np.random.randn(10)
data[data>0]
data[data<0]
data[data>0].sum()
data[data<0].sum()

#요소가 Kim인 행의 데이터 꺼내기
data = np.random.randn(6,4)
data[names=="Kim",:]


#(5) numpy 수치계산함수
arr1 = np.random.randn(5,3)
np.abs(arr1)#절대값
np.sqrt(arr1)#제곱근
#arr1**0.5
np.square(arr1)
# arr1**2
np.exp(arr1)#무리수 e 지수로 삼아서 계산
np.exp(1), np.e
np.exp(2), np.e**2

#각 성분을 자연로그, 사용로그
np.log(arr1)
np.log10(arr1)
np.log2(arr1)

#각 성분의 부호 얻기(+,-,0)
np.sign(arr1)

#올림, 내림
np.ceil(arr1)
np.floor(arr1)
#삼각함수,......

#두개의 Array에 적용하는 함수
arr1 = np.random.randn(5,3)
arr2 = np.random.randn(5,3)
#두개의 array의 같은 요소끼리 비교해서 최댓값 혹은 최소값 계산
np.maximum(arr1,arr2)
np.minimum(arr1,arr2)

#통계함수
np.sum(arr1) #전체성분의 합
np.sum(arr1, axis=1) #열간의 합 크기 == 행의 수
np.sum(arr1, axis=0) #행간의 합 크기 == 열의 수

np.mean(arr1) #전체성분 평균
np.mean(arr1,axis=1) #열간 평균
np.mean(arr1,axis=0) #행간 평균


#전체 성분의 표준편차
np.std(arr1)#표준편차
np.var(arr1)#분산
np.min(arr1)
np.max(arr1)
np.max(arr1, axis=1)#열간 최댓값

#최댓값, 최솟값의 인덱스 반환
np.argmin(arr1)#최소값의 인덱스 반환
np.argmin(arr1,axis=0)# 행간 최소값의 인덱스

#누적합, 누적곱
arr1 = np.array([[1,2,3],[4,5,6]])
np.cumsum(arr1)#전체 성분 누적합
np.cumproduct(arr1)#전체 성분 누적 곱
np.cumproduct(arr1,axis=1)#열간 누적 곱

#정렬
np.sort(arr1, axis=1)#열간정렬
np.sort(arr1, axis=0)#행간정렬







