import pandas as pd
import numpy as np
#1) 데이터수집
fish = pd.read_csv('./data/Fish.csv')
fish.head()
features = fish.drop(['Species'], axis=1)
target = fish['Species']
target.head()
#2) 데이터 탐색 및 전처리
fish.groupby('Species').mean()
np.unique(target.to_numpy(),return_counts=True)
#array(['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish'
#array([35, 11, 56, 17, 20, 14,  6]

#2-1) 데이터 표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(features)
features_scaled = ss.transform(features)

#3) 분석모델 구축
from sklearn.cluster import KMeans
km = KMeans(n_clusters=7, random_state=42)
km.fit(features)
np.unique(km.labels_,return_counts=True)
#(array([0, 1, 2, 3, 4, 5, 6]), array([39, 17, 21, 22,  3, 26, 31], dtype=int64))


#4) 모델평가및 결과분석
inertial = []
for k in range(2, 10) :
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(features_scaled)
    inertial.append(km.inertia_)

import matplotlib.pyplot as plt
plt.plot(range(2,10), inertial)
plt.xlabel('K')
plt.ylabel('inertial')
plt.show()
#3~5


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

silhouetteViz(3, features_scaled) #0.446
silhouetteViz(4, features_scaled) #0.44
silhouetteViz(5, features_scaled) #0.444
silhouetteViz(6, features_scaled) #0.485
silhouetteViz(7, features_scaled) #0.485
silhouetteViz(8, features_scaled) #0.462

#최적의 k값 6
from sklearn.cluster import KMeans
km = KMeans(n_clusters=6, random_state=42)
km.fit(features_scaled)
np.unique(km.labels_,return_counts=True)

features['label'] = km.labels_
features.head()


features.groupby('label').mean()
