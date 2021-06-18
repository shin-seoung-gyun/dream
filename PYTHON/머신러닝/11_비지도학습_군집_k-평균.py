#----------------------------------------------------------------------------------------------------------------------------------------------------------
#k-평균 군집 알고리즘
#각 클러스터(타겟) 별 평균값을 자동으로 찾아준다.
#평균값이 클러스터의 중심에 위치하기 때문에 클러스터 중심
#또는 센트로이드라고 부른다.

#알고리즘 작동순서
#(1) 무작위로 k개의 클러스터 중심을 정한다.
#(2) 각 샘플에서 가장 가까운 클러스터 중심을 찾아
#해당 클러스터의 샘플로 지정한다.
#(3)클러스터에 속한 샘플의 평균값으로 클러스터 중심을 변경한다.
#(4)클러스터 중심에 변화가 없을때 까지 (2)번으로 돌아가 반복한다.

#----------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import _return_float_dtype
#1)데이터 수집
fruits = np.load('./data/fruits_300.npy')
#2)데이터 탐색 및 전처리
fruits_2d = fruits.reshape(-1,100*100)
fruits_2d.shape

#3)분석모델 구축
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)

#4) 모델평가 및 결과분석
km.labels_#라벨 0,1,2
#라벨별 개수
np.unique(km.labels_, return_counts=True)
# (array([0, 1, 2]), array([111,  98,  91], dtype=int64))

#라벨별 시각화
label0 = fruits[km.labels_==0][12].reshape(100,100)
plt.imshow(label0, cmap='gray_r')
plt.show()#label0은 파인애플

label1 = fruits[km.labels_==1][2].reshape(100,100)
plt.imshow(label1, cmap='gray_r')
plt.show()#label0은 바나나


label2 = fruits[km.labels_==2][30].reshape(100,100)
plt.imshow(label2, cmap='gray_r')
plt.show()#label0은 사과

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

draw_fruits(fruits[km.labels_==0])#주로 파인애플
draw_fruits(fruits[km.labels_==1])#모두 바나나
draw_fruits(fruits[km.labels_==2])#모두 사과

#클러스터 중심(라벨에 따른 100*100픽셀별 평균)
km.cluster_centers_.shape#(3, 10000)
draw_fruits(km.cluster_centers_.reshape(-1,100,100), fig_size_ratio=3)

#훈련 데이터 샘플에서 클러스터 별 중심까지 거리값
km.transform((fruits_2d[100:101]))
# array([[3393.8136117 , 8837.37750892, 5267.70439881]])
km.labels_[100]

#새로운 데이터가 있을때 라벨예측
km.predict(fruits_2d[100:101])#array([0])
draw_fruits(fruits[100:101])

#최적의 클러스터 평균값 찾기 위한 알고리즘이 반복한 횃수
km.n_iter_#4

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#최적의 k값을 찾는 방법
#실전에서는 클러스터의 개수를 알수가 없다.
#최적의 k값을 찾아야한다.

#(1) 엘보우 방법
#(2) 실루엣 방법

#(1) 엘보우 방법
#inertial : 클러스터 중심과 샘플 사이의 거리의 제곱합
#클러스터에 속한 샘플이 얼마나 중심에 가깝게 모여 있는지 생각
#할수 있다.

#클러스터가 늘어가면 (중심이 많아지면) 이너셔가 줄어듬
#엘보우 방법은 클러스터 개수를 늘려가면서 이너셔의 변화를 관찰

#감소하는 속도가 꺾이는 지점이 있다.
#이 이후 부터는 클러스터 개수를 늘려도 잘 밀집된 정도가 크게 개선되지 않음

#꺾이는 지점을 최적의 k값으로 판단.
inertial =[]
for k in range(2,7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertial.append(km.inertia_)

inertial
#[5856532545.983113, 5074977316.088372, 4673588404.8560705, 4344167864.512114, 3997030130.9539833]

plt.plot(range(2,7), inertial)
plt.xlabel('k')
plt.ylabel('inertial')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#2) 실루엣 분석

#클러스터 내에 있는 데이터가 얼마나 조밀하게 모여있는지
#측정하는 그래프 도구로서 클러스터와 데이터가 얼마나 가까운가
#를 나타내는 응집력 a(i)와 데이터가 다른 클러스터로 부터
#얼마나 떨어져 있는가를 나타내는 클러스터 분리도 b(i)를
#이용한 실루엣 계수 s(i)를 계산한다.
#실루엣 계수는 -1~1사이의 값을 가지며 1에 가까울수록 좋은 군집화

#실루엣 계수값 구하는 함수
from sklearn.metrics import silhouette_samples
from matplotlib import cm
def silhouetteViz(n_cluster, X_features): 
    
    kmeans = KMeans(n_clusters=n_cluster, random_state=0)
    Y_labels = kmeans.fit_predict(X_features)
    
    silhouette_values = silhouette_samples(X_features, Y_labels, metric='euclidean')

    y_ax_lower, y_ax_upper = 0, 0
    y_ticks = []

    for c in range(n_cluster):
        c_silhouettes = silhouette_values[Y_labels == c]
        c_silhouettes.sort()
        y_ax_upper += len(c_silhouettes)
        color = cm.jet(float(c) / n_cluster)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouettes,
                 height=1.0, edgecolor='none', color=color)
        y_ticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouettes)
    
    silhouette_avg = np.mean(silhouette_values)
    plt.axvline(silhouette_avg, color='red', linestyle='--')
    plt.title('Number of Cluster : '+ str(n_cluster)+'\n' \
              + 'Silhouette Score : '+ str(round(silhouette_avg,3)))
    plt.yticks(y_ticks, range(n_cluster))   
    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient')
    plt.tight_layout()
    plt.show()

silhouetteViz(3, fruits_2d)#0.242
silhouetteViz(4, fruits_2d)#0.208
silhouetteViz(5, fruits_2d)#0.228
silhouetteViz(6, fruits_2d)#0.211
silhouetteViz(7, fruits_2d)#0.224

silhouetteViz(2, fruits_2d)#0.393

#----------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
#1)데이터 수집 및 전처리
fish = pd.read_csv('./data/Fish.csv')
fish.head()
fish_data = fish.drop('Species', axis=1)
fish_data.head()

#표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(fish_data)
fish_data_scaled = ss.transform(fish_data)




#1-2)k값 구하기
#(1) 엘보우 방법
inertial =[]
for k in range(2,10):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fish_data_scaled)
    inertial.append(km.inertia_)

inertial
#[5856532545.983113, 5074977316.088372, 4673588404.8560705, 4344167864.512114, 3997030130.9539833]

plt.plot(range(2,10), inertial)
plt.xlabel('k')
plt.ylabel('inertial')
plt.show()

#2) 실루엣 분석
silhouetteViz(3, fish_data_scaled)#0.44
silhouetteViz(4, fish_data_scaled)#0.44
silhouetteViz(5, fish_data_scaled)#0.44
silhouetteViz(6, fish_data_scaled)#0.485
silhouetteViz(7, fish_data_scaled)#0.485
silhouetteViz(8, fish_data_scaled)#0.462

silhouetteViz(2, fish_data_scaled)#0.552



#2)모델 생성
km = KMeans(n_clusters=6, random_state=42)
km.fit(fish_data_scaled)

#3)모델 평가를 못함. 비지도학습이라 정답이 없음. 모델평가 할 필요도없음. 
km.labels_#라벨 0, 1, 2, 3, 4, 5, 6
#라벨별 개수
np.unique(km.labels_, return_counts=True)#[44, 30, 11, 26,  5, 25, 18]

fish_data['label'] = km.labels_
fish_data.head()

fish_data.groupby('label').mean()

#             Weight     Length   Diagonal     Height     Width
# label
# 0       116.920455  20.686364  22.550000   6.315832  3.328132
# 1       866.133333  38.763333  42.390000  13.813520  6.769810
# 2       456.181818  40.890909  43.872727   6.903782  4.560800
# 3       526.076923  31.715385  36.426923  13.701535  5.252727
# 4      1400.000000  58.220000  62.160000   9.924900  6.584820
# 5       249.400000  26.456000  28.900000   8.309496  4.252632
# 6        15.244444  12.116667  13.233333   2.474578  1.492694

