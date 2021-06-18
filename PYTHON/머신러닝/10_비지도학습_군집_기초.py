#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#군집 : 비숫한 샘플끼리 그룹으로 모으는 작업
#클러스터 : 군집 알고리즘에서 만든 그룹을 클러스터라고 함
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EX) 과일 흑백사진 분류

import numpy as np
import matplotlib.pyplot as plt

#1) 데이터 수집
fruits = np.load('./data/fruits_300.npy')
fruits.shape#(300, 100, 100)
#총 300장의 사진, 100*100픽셀 (사진크기)
#흑백사진 픽셀마다 값 : 0~255 (0에 가까울수록 어두움)

#2) 데이터 탐색 및 전처리
plt.imshow(fruits[0], cmap='gray')
plt.show()
plt.imshow(fruits[100], cmap='gray')
plt.show()
plt.imshow(fruits[200], cmap='gray')
plt.show()
#사과 100, 파인애플100 , 바나나100
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

#픽셀값 분석하기
#100*100 행렬을 펼쳐 길이가 10,000인 1차원 배열로 변경
#계산하기 좋게 변경
apple = fruits[0:100].reshape(-1,100*100)
pineapple = fruits[100:200].reshape(-1,100*100)
banana = fruits[200:30000].reshape(-1,100*100)

apple.shape#(100, 10000)
#사과사진 100, 사과사진당 10,000개 데이터

apple.mean(axis=1)#사과 사진별 픽셀값들의 평균값
apple.mean(axis=1).shape

#과일별 픽셀 평균값의 히스토그램
plt.hist(np.mean(apple, axis=1), alpha=0.8)
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple','pineapple','banana'])
plt.show()

#픽셀별 평균 계산
#픽셀별 (0~10,000)값의 평균 시각화 - 막대그래프
fig, axs = plt.subplots(1, 3, figsize=(20,5))
axs[0].bar(range(10000), np.mean(apple, axis=0))
axs[1].bar(range(10000), np.mean(pineapple, axis=0))
axs[2].bar(range(10000), np.mean(banana, axis=0))
plt.show()
#사과는 사진 아래쪽 (픽셀 아래쪽) 갈수록 값이 높아지고
#파인애플은 비교적 값이 고르게 분포하면서 값이 높음
#바나나는 중앙의 픽셀값이 높음

#픽셀별 평균 사진을 이미지
apple_mean = np.mean(apple, axis=0).reshape(100,100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100,100)
banana_mean = np.mean(banana, axis=0).reshape(100,100)

fig, axs = plt.subplots(1,3,figsize=(20,5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()

#3) 분석모델 구축
#방법 : 평균값과 가장 가까운 사진 고르기
abs_diff = np.abs(fruits-apple_mean)
abs_diff.shape 

#각 사진 픽셀들의 오차 평균값
abs_mean = np.mean(abs_diff, axis=(1,2))
abs_mean.shape
#=>오차가 작으면 사과

#4) 모델평가 및 결과 분석
#오차가 작은 100개의 이미지 출력
apple_index = np.argsort(abs_mean)[:100]#argsort는 abs를 오름차순을 정렬하여 해당하는 인덱스 값을 출력
#오차가 가장 작은 인덱스 값을 저장
fig, axs = plt.subplots(10,10, figsize = (10,10))
for i in range(10):
    for j in range(10):
        axs[i,j].imshow(fruits[apple_index[i*10+j]],cmap='gray_r')
plt.show()
##사과

#방법 : 평균값과 가장 가까운 사진 고르기
abs_diff = np.abs(fruits-pineapple_mean)
abs_diff.shape 

#각 사진 픽셀들의 오차 평균값
abs_mean = np.mean(abs_diff, axis=(1,2))
abs_mean.shape
#=>오차가 작으면 파인애플

#4) 모델평가 및 결과 분석
#오차가 작은 100개의 이미지 출력
pineapple_index = np.argsort(abs_mean)[:100]#argsort는 abs를 오름차순을 정렬하여 해당하는 인덱스 값을 출력
#오차가 가장 작은 인덱스 값을 저장
fig, axs = plt.subplots(10,10, figsize = (10,10))
for i in range(10):
    for j in range(10):
        axs[i,j].imshow(fruits[pineapple_index[i*10+j]],cmap='gray_r')
plt.show()

##파인애플

#방법 : 평균값과 가장 가까운 사진 고르기
abs_diff = np.abs(fruits-banana_mean)
abs_diff.shape 

#각 사진 픽셀들의 오차 평균값
abs_mean = np.mean(abs_diff, axis=(1,2))
abs_mean.shape
#=>오차가 작으면 파인애플

#4) 모델평가 및 결과 분석
#오차가 작은 100개의 이미지 출력
banana_index = np.argsort(abs_mean)[:100]#argsort는 abs를 오름차순을 정렬하여 해당하는 인덱스 값을 출력
#오차가 가장 작은 인덱스 값을 저장
fig, axs = plt.subplots(10,10, figsize = (10,10))
for i in range(10):
    for j in range(10):
        axs[i,j].imshow(fruits[banana_index[i*10+j]],cmap='gray_r')
plt.show()


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#지금과 같은 경우 타깃값을 알기에 샘플들의 평균값
#(사과, 바나나, 파인애플 평균) 을 구함

#실제 비지도학습에서는 타깃값을 모르기 때문에 이처럼 샘플들의 평균값을 미리 구할수가 없다.

#타깃값을 모르면서 세 과일들의 각각 평균값을 찾는 알고리즘
#대표적으로 k-means알고리즘 (엘보우 방법, 실루엣방법)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
































































