##데이터 수집 -http://archive.ics.uci.edu
#online rarail
#영국 온라인 소매 플랫폼 2010.12.01~2011.12.09 거래데이터

#군집화 : 대표적인 비지도학습, 데이터 안에 숨겨진 패턴을 찾아 타깃 값을 만든다

# 군집분석 대표적 알고리즘 : k평균, 계층적 군집
#k-평균 알고리즘 - k개의 클러스터 (군집 )을 구성하기 위한것

#적절한 k값을 찾는 방법
#1)엘보방법 : 클러스터의 중심점과 클러스터 내의 데이터 거리
#차이의 제곱합을 왜곡이라고 하고, 왜곡을 활용하여 최적의 k값을 찾는다.
#클러스터 개수 k의 변화에 따른 왜곡의 변화를 그래프로 그려서
#그래프가 꺾이는 지점인 엘보가 나타나는데 그지점의 k를 최적의 k로 선정함.


#2)실루엣 분석 : 클러스터 내에 있는 데이터가 얼마나 조밀하게 모여있는지
#측정하는 그래프 도구 로서 클러스터와 데이터가 얼마나 가까운가를 나타내는 응집
#력 a(i)와 데이터가 다른 클러스터 내 의 데이터와 얼마나 떨어져있는가를 나타내는 클러스터
#분리도 b(i)를 이용한 실루엣 계수 s(i)를 계산한다.
#실루엣 계수는 -1~1사이의 값을 가지며 1에 가까울 수록 좋은 군집화.

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1)데이터 수집
retail_df = pd.read_csv("./머신러닝/OnlineRetail.csv", header=0,engine='python')
print(retail_df.head())
print(retail_df.info())

#2)데이터 탐색 및 전처리
print(retail_df.isnull().sum())
retail_df = retail_df[retail_df['CustomerID'].notnull()]

print(retail_df[retail_df['Quantity']<0])
retail_df = retail_df[retail_df['Quantity']>0]
retail_df['CustomerID']= retail_df['CustomerID'].astype(int)

print(retail_df.isnull().sum())
print(retail_df.info())
print(retail_df.head())

#중복데이터 제거
retail_df.drop_duplicates(inplace=True)
print(retail_df.info())

#제품수, 거래건수, 고객수, 나라 수 탐색
# print("제품수 : ", len(retail_df['StockCode'].value_counts()))
print("제품수 : ", len(retail_df['StockCode'].unique()))
print("거래건수 : ", len(retail_df['InvoiceNo'].unique()))
print("고객수 : ", len(retail_df['CustomerID'].unique()))
# print("나라별 거래수 : ", retail_df['Country'].value_counts())
print(retail_df.groupby('Country')['InvoiceNo'].unique().apply(lambda x : len(x)).sort_values(ascending=False))

##고객 데이터프레임 만들기
retail_df['SaleAmount']= retail_df['UnitPrice']*retail_df['Quantity']
aggressions = {'InvoiceNo':'count','SaleAmount':'sum','InvoiceDate':'max'}
customer_df = retail_df.groupby("CustomerID").agg(aggressions)
print(customer_df)

##InvoiceDate 를 데이트타입으로 변경하기
import datetime
customer_df['InvoiceDate']= pd.to_datetime(customer_df['InvoiceDate'])

#InvoiceDate를 고객의 마지막 주문 후 경과일로 변경
customer_df['InvoiceDate']= datetime.datetime(2011,12,10)-customer_df['InvoiceDate']##오늘이 2011,12,10일 이라고 가정하고 만든식 고객의 마지막 주문일로부터 2011,12,10일까지의 차이
customer_df['InvoiceDate']= customer_df['InvoiceDate'].apply(lambda x:x.days+1)
print(customer_df.head())
customer_df = customer_df.rename(columns={'InvoiceNo':'Freq',"InvoiceDate":'ElapsedDays'})
print(customer_df.head())

##박스플롯 - 고객 데이터 시각화
# fig, ax = plt.subplots()
# ax.boxplot([customer_df["Freq"],customer_df['SaleAmount'],customer_df['ElapsedDays']],sym='bo')
# plt.xticks([1,2,3],['Freq','SaleAmount','ElapsedDays'])
# plt.show()

#데이터 값의 왜곡을 줄이기 위한 로그 함수로 분포 조정
#log1p=>log(1+x)
customer_df['Freg_log'] = np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log'] = np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log'] = np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())
##조정된 데이터로 박스플롯 - 고객 데이터 시각화
fig, ax = plt.subplots()
ax.boxplot([customer_df["Freg_log"],customer_df['SaleAmount_log'],customer_df['ElapsedDays_log']],sym='rs')
# plt.xticks([1,2,3],['Freq','SaleAmount','ElapsedDays'])
# plt.show()

##3)모델 구축 : k-평균 군집화 모델
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples,silhouette_score

#데이터 정규 분포 스케일링
from sklearn.preprocessing import StandardScaler
X_features = customer_df[['Freg_log','SaleAmount_log','ElapsedDays_log']]
X_features_scaled = StandardScaler().fit_transform(X_features)
print(X_features_scaled)

#최적의 k값 찾기
#(1) 엘보우 방법 - 클러스터 k값을 1~10까지 반복하면서 왜곡값을 리스트에 저장
distortion = []
for i in range(1,11):
    kmeans_i = KMeans(n_clusters=i,random_state=0)#모델생성
    kmeans_i.fit(X_features_scaled)#모델훈련
    distortion.append(kmeans_i.inertia_)

# plt.plot(range(1,11), distortion, marker='o')
# plt.xlabel("Number of Cluster")
# plt.ylabel("Distortion")
# plt.show()

#엘보 방법을 통한 최적의 k값 2~4
kmeans = KMeans(n_clusters=3, random_state=0)
Y_labels = kmeans.fit_predict(X_features_scaled)
customer_df['ClusterLabel']=Y_labels
print(customer_df.head())


##실루엣 함수
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

#- 클러스터 수에 따른 클러스터 데이터 분포의 시각화 함수 정의
def clusterScatter(n_cluster, X_features): 
    c_colors = []
    kmeans = KMeans(n_clusters=n_cluster, random_state=0)
    Y_labels = kmeans.fit_predict(X_features)

    for i in range(n_cluster):
        c_color = cm.jet(float(i) / n_cluster) #클러스터의 색상 설정
        c_colors.append(c_color)
        #클러스터의 데이터 분포를 동그라미로 시각화
        plt.scatter(X_features[Y_labels == i,0], X_features[Y_labels == i,1],
                     marker='o', color=c_color, edgecolor='black', s=50, 
                     label='cluster '+ str(i))       
    
    #각 클러스터의 중심점을 삼각형으로 표시
    for i in range(n_cluster):
        plt.scatter(kmeans.cluster_centers_[i,0], kmeans.cluster_centers_[i,1], 
                    marker='^', color=c_colors[i], edgecolor='w', s=200)
        
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# 실루엣 방법
#클러스터 3인 경우의 실루엣 score및 클러스터 비중 시각화
# silhouetteViz(3, X_features_scaled)#0.304
# silhouetteViz(4, X_features_scaled)#0.309
# silhouetteViz(5, X_features_scaled)#0.276
# silhouetteViz(6, X_features_scaled)#0.274

##클러스터별로 데이터 시각화
# clusterScatter(3, X_features_scaled)
# clusterScatter(4, X_features_scaled)
# clusterScatter(5, X_features_scaled)
# clusterScatter(6, X_features_scaled)

#결정된 k를 적용하여 k - mean모델 완성
best_cluster = 4

kmeans = KMeans(n_clusters=best_cluster, random_state=0)
Y_labels = kmeans.fit_predict(X_features_scaled)
customer_df['ClusterLabel']=Y_labels
print(customer_df.head())

customer_df.to_csv('./머신러닝/Online_Retail_Customer.csv')

## 클러스터 결과분석 ##

#클러스터 별 고객수
customer_df['dummy']=0
print(customer_df.groupby('ClusterLabel')['dummy'].count())

#클러스터 별 특징
customer_cluster_df = customer_df.drop(['Freg_log','SaleAmount_log','ElapsedDays_log'],axis=1,inplace=False)

#주문 1회당 평균 구매금액 : SaleAmountAvg
customer_cluster_df['SaleAmountAvg']=customer_cluster_df['SaleAmount']/customer_cluster_df['Freq']
print(customer_cluster_df.head())

##클러스터별로 평균값
print(customer_cluster_df.drop("dummy",axis=1).groupby('ClusterLabel').mean())









