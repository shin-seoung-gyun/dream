#질적 변수와 양적변수
##(1) 질적변수 : 선택이 필요한 변수, 종류를 구별하기 위한 변수
#명의 척도 : 단순 분류 순서나 대소 관계와 연관없이 그저 구별만함 ex) 학생번호, 전화번호, 성별, 혈액형
#순서 척도 : 순서나 대소관계에 연관하는 변수 ex) 설문지, 성적

#(2) 양적변수 - 양을 표현하는 변수
#간격 척도 - 대소 관계와 함께 그 차이도 의미를 두는 변수
#비례 척도 - 대소 관계, 차이 비례관계 모두 의미가 있는 변수
#간격 척도와 비례척도를 구분하는법
#0이 없음을 뜻하면 비례척도 아니면 간격 척도
#온도는 0이 없다는 뜻이 아니므로 간격척도
#몸무게는 0이 없다는 뜻이므로 비례척도

#이산형 변수 와 연속형 변수
#(1) 이산형 변수 : 0,1,2와 같이 하나하나의 값을 취하는 변수.
#서로 인접한 값 사이에 값이 존재하지 않음
#주사위는 1,2,3,4,5,6 의 값이 있지만 1.1,1.2 같은 값은 존재 하지 않음.

#(2) 연속형 변수 : 연속적인 값을 취할수 있는 변수
#길이 같은경우 1cm와 2cm사이에 1.1cm등이 존재함 그러나 데이터에서는 이산형 변수로 취급되는 경우가 많은듯
import pandas as pd
df = pd.read_csv('./data/ch1_sport_test.csv')
df.head()
df
#    학생번호  학년    악력  윗몸일으키기  점수  순위
# 0     1   1  40.2      34  15   4
# 1     2   1  34.2      14   7  10
# 2     3   1  28.8      27  11   7
# 3     4   2  39.0      27  14   5
# 4     5   2  50.9      32  17   2

#해당 데이터에서 학생번호는
#질적변수이고, 명의척도이다.

#학년은
#질적변수이고, 순서척도이다.

#악력은
#양적변수이고, 연속형변수인것같은 이산형변수이다.

#점수는
#양적변수이고, 이산형 변수이다.

#순위는
#질적변수이고, 순서척도이다.

#Numpy는 벡터와 행렬을 연산처리하는 라이브러리이고
#고성능의 수치계산을 할 수 있다

#고성능의 수치계산을 위해 일반 파이썬문법과 달리 자료형을 사용한다.

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

data2 = [1,1.5,2,2.5,4,5,6]
arr1 = np.array(data2)
arr1.shape #array의 크기
arr1.dtype #데이터 타입

arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr3.shape 
arr3.dtype

#(1-1) numpy 기본적인 함수
np.zeros(10)
np.zeros((3,5))
np.ones(10)
np.ones((3,5))
np.arange(10)
np.arange(3,10)
np.arange(3,10,0.1)
np.linspace(0,1,5)
#시작값 0 , 마지막값 1, 요소 4개로 균등한 간격으로.
#간격의 값을 구하려면
#간격은 요소에서 1을 뺀값, 간격의 크기는 마지막 값에서 시작값을 빼고 요소의 간격수로 나누면 됨.

np.random.randint(5,10,size=(2,4)) #5부터 10미만의 정수 //랜덤 뽑는 방법

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[10,11,12],[13,14,15]])
arr1+arr2
#넘파이 array는 배열간의 계산이 가능.일반 리스트와 달라서 확인이 필요함.
#array의 브로드캐스트
#행렬의 크기는 다르나 열의 개수가 같은 경우 각각의 열에 브로드 캐스트한다.

#(4) Array Boolean 인덱싱 마스크

names = np.array(['Beo','Beo','Kim','Joan','Lee','Beo'])
names_beo_mask = (names=='Beo')
names_beo_mask
names[names_beo_mask]
#randn함수는 기대값이 0이고 표준편차가 1인 정규분포에서 난수 발생
data
##여기서까지 함.

















