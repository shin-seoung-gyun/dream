#실습3_스포츠 센터 고객분류.py

#1) 데이터 수집
import pandas as pd
#회원 데이터 가져오기2019-03월 말 시점
customer = pd.read_csv('./data/customer_master.csv')
customer.info()
customer.head()
customer['start_date'].max()#'2019-03-15 00:00:00'

class_master =pd.read_csv('./data/class_master.csv')
class_master.info()
class_master.head()

campain_master =pd.read_csv('./data/campaign_master.csv')
campain_master.info()
campain_master.head()

#약1년치의 스포츠 센터 이용내역
uselog =pd.read_csv('./data/use_log.csv')
uselog.info()
uselog.head()
uselog['usedate'].min()#'2018-04-01'
uselog['usedate'].max()#'2019-03-31'

#2)데이터 전처리 및 탐색
#2-1) 데이터 병합
customer_join = pd.merge(customer, class_master, on='class', how='left')
customer_join = pd.merge(customer_join, campain_master, on='campaign_id', how='left')
customer_join.head()
customer_join.info()

#2-2)고객 타입별 수 탐색
#고객수 
len(customer_join)#4192
# 캠페인 별 고객수
customer_join.groupby('campaign_id').count()['customer_id']
# campaign_id
# CA1    3050
# CA2     650
# CA3     492
# Name: customer_id, dtype: int64

#클래스별 고객수
customer_join.groupby('class').count()['customer_id']
# class
# C01    2045
# C02    1019
# C03    1128
# Name: customer_id, dtype: int64

#성별별 고객수
customer_join.groupby('gender').count()['customer_id']
# gender
# F    1983
# M    2209

#탈퇴 여부 별 고객수
customer_join.groupby('is_deleted').count()['customer_id']
# is_deleted
# 0    2842
# 1    1350
# Name: customer_id, dtype: int64

#2-3) 새로운 데이터 생성
#주기적 방문횟수를 통한 데이터 비교
#이용 이력 데이터 집계
uselog.head()
uselog.info()
#날자데이터의 타입변경
uselog['usedate']=pd.to_datetime(uselog['usedate'])
uselog.info()

#고객별 월별 출입 횟수
#월별 데이터 생성
uselog['yyyymm'] = uselog['usedate'].dt.strftime('%Y%m')
uselog.head()

uselog_months = uselog.groupby(['yyyymm','customer_id'], as_index=False).count()
uselog_months.head()
uselog_months[uselog_months['customer_id']=='AS002855']

uselog_months.rename(columns={'log_id':'count'},inplace=True)
del uselog_months['usedate']
uselog_months.head()


#고객별로 달별 이용 횟수 집계
uselog_customer = uselog_months.groupby(['customer_id'], as_index=False).agg(['mean','median','max','min'])['count']
uselog_customer.head()

#customer_id를 인덱스가 아닌 값으로 변경
uselog_customer = uselog_customer.reset_index(drop=False)
uselog_customer.head()

#주기적 이용 고객 체크, 같은 달 같은 요일 4번이상 나온 고객
#고객이 규칙적으로 운동하는지 여부 체크
uselog['weekday'] = uselog['usedate'].dt.weekday
uselog.head()#0~6 => 월 ~ 일
uselog_weekday = uselog.groupby(['customer_id','yyyymm','weekday'],as_index=False).count()[['customer_id','yyyymm','weekday','log_id']]
uselog_weekday.head()

uselog_weekday.rename(columns={'log_id':'count'},inplace=True)
uselog_weekday.head()

#flag 칼럼 추가
uselog_weekday = uselog_weekday.groupby('customer_id', as_index=False).max()[['customer_id','count']]

uselog_weekday['routine_flg']=0
uselog_weekday.loc[uselog_weekday['count']>=4, 'routine_flg']=1
uselog_weekday.head()

#고객데이터와 이용이역 데이터 병합
customer_join = pd.merge(customer_join, uselog_customer, on="customer_id", how='left')
customer_join = pd.merge(customer_join, uselog_weekday[['customer_id','routine_flg']], on="customer_id", how='left')
customer_join.head()

#회원기간 계산
from dateutil.relativedelta import relativedelta
customer_join['calc_date']=customer_join['end_date']
customer_join['calc_date']=customer_join['end_date'].fillna(pd.to_datetime("20190430"))
customer_join.head()
customer_join['membership_period']=0


customer_join['start_date']=pd.to_datetime(customer_join['start_date'])
customer_join['calc_date']=pd.to_datetime(customer_join['calc_date'])
relativedelta(customer_join['calc_date'].iloc[0],customer_join['start_date'].iloc[0])


for i in range(len(customer_join)):
    delta = relativedelta(customer_join['calc_date'].iloc[i],customer_join['start_date'].iloc[i])

    customer_join['membership_period'].iloc[i] = delta.years*12 + delta.months + delta.days/30

customer_join.head()

#2-4)정기 이용 고객수
customer_join.groupby('routine_flg').count()['customer_id']

#2-5)고객행동에대한 집계
customer_join[['mean','median','max','min']].describe()
#고객별 한달 이용 집계에 대한 전체 고객의 집계
#               mean       median          max          min
# mean      5.333127     5.250596     7.823950     3.041269

#고객회원기가에 따른 고객수 히스토그램 시각화
import matplotlib.pyplot as plt
plt.hist(customer_join['membership_period'])
plt.xlabel('mon')
plt.ylabel('persom num')
plt.show()

#10개월 이내의 고객이 가장 많음

#10개월 이내의 고객 기준 - 지속회원과 탈퇴회원 차이확인
customer_end = customer_join.loc[(customer_join['is_deleted']==1)&(customer_join['membership_period']<=10)]
customer_stay = customer_join.loc[(customer_join['is_deleted']==0)&(customer_join['membership_period']<=10)]

customer_end.describe()##10개월 이내 탈퇴회원 920명 평균 한달 4번출입 max=7,min=2,루틴 0.4
customer_stay.describe()##10개월 이내 지속회원 590명 평균 한달 8번출입  9.8  6.6   0.9

#결론 : 탈퇴 회원의 매월 이용횟수의 평균, 중앙값, 최대, 최소, 루틴값
#모두 지속회원 보다 작다.

#시각화 - 평균값, 칼럼(is_delete, price빼고 모두)
plt.plot(customer_end.describe().loc['mean'][2:-1],label='short')
plt.plot(customer_stay.describe().loc['mean'][2:-1],label='long')
plt.legend()
plt.show()


#고객 병합 데이터 저장
customer_join.to_csv('./data/customer_join.csv', index=False)

#=====================================================================================================================================================================
#3) 분석모델 구축
#k-means 회원군집화
#3-1) 분석데이터 확립

customer_clustering = customer_join[['mean','median','max','min','routine_flg','membership_period']]
customer_clustering.head()

#3-2)데이터 정규화
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)

#3-3) 모델훈련
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering['label'] = clusters.labels_
customer_clustering.head()

#4) 모델평가 및 결과분석
#4-1) 모델평가
#엘보우 방법으로 최적의 k값 찾기
inertial = []
for k in range(2, 7) :
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(customer_clustering_sc)
    inertial.append(km.inertia_)

inertial
#[5856532545.983113, 5074977316.088372, 4673588404.8560705, 4344167864.512114, 3997030130.9539833]

plt.plot(range(2,7), inertial)
plt.xlabel('K')
plt.ylabel('inertial')
plt.show()

#최적의 k값은 3


#실루엣 방법으로 최적의 k값 구하기
import numpy as np
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

silhouetteViz(3, customer_clustering_sc) #0.456
silhouetteViz(4, customer_clustering_sc) #0.34
silhouetteViz(5, customer_clustering_sc) #0.36
silhouetteViz(6, customer_clustering_sc) #0.4
silhouetteViz(7, customer_clustering_sc) #0.358

silhouetteViz(2, customer_clustering_sc) #0.387
#k값이 3일때가 가장 최적이다.

#4-3) 그룹별 특징 확인
customer_clustering.head()
customer_clustering.groupby('label').count()
customer_clustering.groupby('label').mean()

#0: 회원기간 평균 8개월(신입회원), 주기적으로 운동 오지 않음, 한달평균 3회
#1: 회원기간 평균 9개월(신입회원), 주기적으로 운동옴, 한달평균 7회
#2: 회원기간 평균 28개월(장기회원), 주기적으로 운동옴, 한달평균 5회
#  


#차원축소 PCA - 5개의변수  -> 2차원 축소
from sklearn.decomposition import PCA
X = customer_clustering_sc
pca = PCA(n_components=2)
pca.fit(X)
pca.explained_variance_ratio_
# array([0.60299416, 0.24302354])

x_pca = pca.transform(X)
pca_df = pd.DataFrame(x_pca)
pca_df['label']=customer_clustering['label']
pca_df.head()


import matplotlib.pyplot as plt
for i in customer_clustering['label'].unique() :
    data = pca_df.loc[pca_df['label']==i]
    plt.scatter(data[0], data[1], label=f'{i}')
plt.legend()
plt.show()

pca.components_[0]
# array([ 0.52097852,  0.50560327,  0.44160572,  0.44501407,  0.24819124,
    #    -0.13525788])
#주성분 1축 월평균 이용횟수


pca.components_[1]
# array([ 0.02911291, -0.00818763, -0.09628486,  0.21067394, -0.64660475,
#        -0.72617726])
#주성분 2축 주기적으로 이용하지 않은 횟수 + 장기적이지도 않다.

#클러스터링 결과를 바탕으로 탈퇴 회원 수와 꾸준한 사람 수 파악
customer_join = pd.concat([customer_clustering['label'],customer_join],axis=1)
customer_join.head()
customer_join.groupby(['label','is_deleted'], as_index=False).count()[['label', 'is_deleted', 'customer_id']]

#    label  is_deleted  customer_id
# 0      0           0            6
# 1      0           1          728
# 2      1           0         1024
# 3      1           1           50
# 4      2           0         1812
# 5      2           1          572


