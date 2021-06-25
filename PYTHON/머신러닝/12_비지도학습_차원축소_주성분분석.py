#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#주성분 분석 (PCA)
#차원 : 머신러닝에서는 특성을 차원이라고 한다. (특성수 = 차원수)
#ex) 10000개 특성 => 10000차원

#차원 축소: 데이터를 가장 잘 나타내는 일부 특성을 선택하여,
#데이터의 크기를 줄이고 지도학습모델의 성능을 향상시킬수 있는 방법

#또한 줄어든 차원에서 다시 원본차원으로 손실을 최대한 줄이면서
#복원도 가능

#주성분 : 데이터의 분산이 큰 방향의 벡터 (데이터의 분포를 가장 잘 표현)
#원본데이터를 주성분 벡터로 투영하여 차원을 줄일수 있다.

#그다음으로 분산이 큰 방향의 벡터를 찾음
#주성분은 원본 특성의 개수 만큼 찾을수 있다.
#ex) 2차원 데이터의 최대 주 성분 수 2개

#주성분은 원본 데이터에서 가장 분산이 큰 반향을 순서대로 나타낸것
#데이터 셋에 있는 어떤 특징을 잡아냈다고 생각하면 좋다.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ex) 과일 그림 데이터 차원축소
import numpy as np
import matplotlib.pyplot as plt
def draw_fruits(arr, fig_size_ratio=1):
    n = len(arr)    # n은 샘플 개수입니다
    # 한 줄에 10개씩 이미지를 그립니다. 샘플 개수를 10으로 나누어 전체 행 개수를 계산합니다. 
    rows = int(np.ceil(n/10))
    # 행이 1개 이면 열 개수는 샘플 개수입니다. 그렇지 않으면 10개입니다.
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols, 
                            figsize=(cols*fig_size_ratio, rows*fig_size_ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:    # n 개까지만 그립니다.
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()

#1) 데이터 수집
fruits = np.load('./data/fruits_300.npy')
fruits.shape#(300, 100, 100)

#2)데이터 탐색 및 전처리
#2차원 행렬 이미지 데이터을 1차원 벡터화
fruit_2d = fruits.reshape(-1,100*100)
fruit_2d.shape

#3) 분석모델구축
from sklearn.decomposition import PCA
pca = PCA(n_components=50)#n_components는 주성분의 개수
#10000 차원 => 차원
pca.fit(fruit_2d)

pca.components_.shape#(50, 10000)
#50개의 주성분
draw_fruits(pca.components_.reshape(-1,100,100))


#주성분을 통한 데이터
fruits_pca=pca.transform(fruit_2d)
fruits_pca.shape#(300, 50)

#주성분 데이터 => 원본데이터로 재구성
fruits_inverse = pca.inverse_transform(fruits_pca)
fruits_inverse.shape#(300, 10000)
fruits_reconstruct = fruits_inverse.reshape(-1,100,100)
for start in [0,100,200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print('\n')

#설명된 분산 : 주성분이 원본데이터의 분산을 얼마나 잘 나타내는지 기록한 값.
#첫번째 주성분이 설명된 분산이가장 큼(정보를 가장 많이 포함하고있다.)
pca.explained_variance_ratio_
# array([0.42357017, 0.09941755, 0.06577863, 0.04031172, 0.03416875,
#        0.03281329, 0.02573267, 0.02054963, 0.01372276, 0.01342773,
#        0.01152146, 0.00944596, 0.00878232, 0.00846697, 0.00693049,
#        0.00645188, 0.00578896, 0.00511202, 0.00486383, 0.00480347,
#        0.00447835, 0.00437314, 0.0040804 , 0.00389476, 0.00372425,
#        0.00359283, 0.00331471, 0.00317804, 0.00304289, 0.00303734,
#        0.00288859, 0.00275777, 0.00264858, 0.00255808, 0.00252008,
#        0.00247425, 0.00239488, 0.00230334, 0.00222093, 0.00217025,
#        0.0021356 , 0.00195694, 0.00192561, 0.0019102 , 0.0018422 ,
#        0.0018023 , 0.00174225, 0.00168978, 0.00161902, 0.00159982])

plt.plot(pca.explained_variance_ratio_)
plt.show()

np.sum(pca.explained_variance_ratio_)
# 0.9215374443815147
#원본 데이터 대비 92%넘는 분산 유지 (92% 데이터 복구 가능)

#설명된 분산이 50%에 달하는 주성분 모델
pca=PCA(n_components=0.5)#0~1사이의 실수 비율 입력(설명된 분산)
pca.fit(fruit_2d)
pca.n_components_#주성분 개수 2개
pca.explained_variance_ratio_
# array([0.42357017, 0.09941755])
np.sum(pca.explained_variance_ratio_)
# 0.5229877245800594

fruits_pca = pca.transform(fruit_2d)
fruits_pca.shape#(300, 2)

fruits_inverse = pca.inverse_transform(fruits_pca)
fruits_inverse.shape#(300, 10000)
fruits_reconstruct = fruits_inverse.reshape(-1,100,100)
for start in [0,100,200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print('\n')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#다른 알고리즘과 함께 주성분분석 사용하기
#로지스틱 회귀분석
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#타겟 생성
target = np.array([0]*100+[1]*100+[2]*100)
#0사과, 1파인애플, 2바나나

#특성 10,000개 그대로 훈련
#교차검증으로 점수 확인
from sklearn.model_selection import cross_validate
scores = cross_validate(lr, fruit_2d, target)
np.mean(scores['test_score']) #0.9966666666666667 테스트 점수 예측
np.mean(scores['fit_time'])#0.3240376949310303 훈련 시간
#특성이 많아서 과대적합 모델을 만들기 쉽다.

pca = PCA(n_components=50)#n_components는 주성분의 개수
#10000 차원 => 차원
pca.fit(fruit_2d)

pca.components_.shape#(50, 10000)

#주성분을 통한 데이터
fruits_pca=pca.transform(fruit_2d)
fruits_pca.shape#(300, 50)

scores = cross_validate(lr, fruits_pca, target)
np.mean(scores['test_score']) #1.0 테스트 점수 예측
np.mean(scores['fit_time'])#0.01815037727355957 훈련 시간
#정확도 100%, 훈련시간 10배이상 감소


pca = PCA(n_components=0.5)#n_components는 주성분의 개수
#10000 차원 => 차원
pca.fit(fruit_2d)

pca.components_.shape#(50, 10000)

#주성분을 통한 데이터
fruits_pca=pca.transform(fruit_2d)
fruits_pca.shape#(300, 50)

scores = cross_validate(lr, fruits_pca, target)
np.mean(scores['test_score']) #0.9933333333333334 테스트 점수 예측
np.mean(scores['fit_time'])#0.03090348243713379 훈련 시간
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#다른 알고리즘과 함께 주성분분석 사용하기
#k-means 알고리즘으로 군집화
from sklearn.cluster import KMeans
km=KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)
np.unique(km.labels_, return_counts=True)
# (array([0, 1, 2]), array([110,  99,  91], dtype=int64))

#라벨별 시각화
for label in range(0,3):
    draw_fruits(fruits[km.labels_==label])
    print('\n')


#0번 : 파인애플 1번:바나나(100%) 3번 : 사과(100%)

#2차원 데이터 - 클러스터별 산점도 시각화
for label in range(0,3):
    data = fruits_pca[km.labels_==label]
    plt.scatter(data[:,0],data[:,1])
plt.legend('pinapple', 'banana', 'apple')
plt.show()


