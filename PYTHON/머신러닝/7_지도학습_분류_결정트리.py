#----------------------------------------------------------------------------------------------------------
#의사결정트리 : 데이터 분류 기준을 여러개 세워 분류 정확도를 높임
#데이터 분류에 대한 명확인 기준과 이유를 제시 (해석 용이)
#--------------------------------------------------------------------------------------------------------------
#Ex) 화이트와인, 레드와인 분류

#1.로지스틱 회귀분석 분류

#1)데이터 수집
import pandas as pd
import numpy as np
wine = pd.read_csv("./data/wine.csv")
wine.info()
wine.head()
#2)데이터 탐색 및 전처리 class 0 - red , 1 - white
#2-1)데이터 분할
wine.groupby('class').describe()

pd.unique(wine['class'])
X_train = wine[wine.columns[:3]].to_numpy()
X_train.shape#(159, 5) 159개 데이터 5개의 특성

Y_train = wine['class'].to_numpy()
Y_train

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_train,Y_train, random_state=42)

#2-1)데이터 정규화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)

#3) 분석모델 구축
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(X_train_scaled,Y_train)

#4)모델평가 및 결과 분석
lr.score(X_train_scaled,Y_train)#0.7859195402298851
lr.score(X_test_scaled,Y_test)#0.7655384615384615

lr.predict(X_test_scaled[:10])

Y_test[:10]

#4-1)모델에 기여하는 변수 확인
coef_df = pd.DataFrame({'feature':X_train.columns, 'coef': lr.coef_[0]})##??

#Z = 0.5*alchol + 1.68*sugar -0.688*ph +1.82

###################################################################################################################################
#2. 결정트리 모델
from sklearn.tree import DecisionTreeClassifier ##분류
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_scaled,Y_train)

dt.score(X_train_scaled,Y_train)#0.9973316912972086
dt.score(X_test_scaled,Y_test)#0.8516923076923076
#과대적합 되었지만 성능은 좋아짐.

#의사결정트리모델 시각화
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(10,7))
plot_tree(dt)
plt.show()


# plt.figure(figsize=(10,7))
# plot_tree(dt, max_depth=1, filled=True, feature_names=X_train.columns)
# plt.show()
plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1, filled=True)
plt.show()

#-------------------------------------------------------------------------------------------------------------
#노드 : 결정 트리를 구성하는 핵심요소. 노드는 훈련데이터의 특성에 대한
#테스트를 나타낸다.
#일반적으로 하나의 노드는 2개의 가지를 가진다.
#맨 위의 노드를 루프노드, 맨 아래의 노드를 리프 노드라 한다.

#노드에 있는 정보
#테스트 조건 ex(suger < -0.239)
#불순도(지니계수) gini = 0.367
#총 샘플수 : 데이터 개수 ex)5197
#클래스별 샘플 수 : value = [1258,3939]

#의사결정트리분류기준 (gini계수)
#지니불순도 = 1-(음성 클래스의 비율^2+양성 클래스의 비율^2)
#값이 작을수록 한 클래스의 비율이 높음

#정보이득 : 부모와 자식 노드의 불순도 차이
#결정트리 모델은 부모노드와 자식노드의 불순도 차이가 가장 크도록
#트리를 성장시킴
#정보이득이 최대가 되도록 데이터를 나눈다.

#과대적합방지 : 트리깊이 제한

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train_scaled,Y_train)

dt.score(X_train_scaled,Y_train)#0.8499589490968801
dt.score(X_test_scaled,Y_test)#0.8363076923076923

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True)
plt.show()

import pydotplus
from sklearn.tree import export_graphviz

dot_data = export_graphviz(dt, out_file=None, class_names=['red','white'], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('./결정트리_와인분류.png')


#결정트리는 정규화(표준화)를 안해도 된다.


dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train,Y_train)

dt.score(X_train,Y_train)#0.8499589490968801
dt.score(X_test,Y_test)#0.8363076923076923


dot_data = export_graphviz(dt, out_file=None, class_names=['red','white'], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('./결정트리_와인분류.png')

#결과 해석
#레드와인 = 당도<1.625 and 알콜 <11.025
#나머지 화이트와인

#특성 중요도 : 어떤 특성이 가장 유용한지 나타낸다.
#각 노드의 정보이득과 전체 샘플에 대한 비율을 곱한후 특성별고 계산
# dt.feature_importances_
# pd.DataFrame({'features':X_train.columns,'importances':dt.feature_importances_})
dt.feature_importances_
pd.DataFrame({'importances':dt.feature_importances_})

#결정트리 모델이 나중에 앙상블 학습 알고리즘 기반이 된다.
#앙상블학습은 신경망과 함께 가장높은 성능을 나타냄

#---------------------------------------------------------------------------------------------------------------------------------------------
#결정트리의 깊이값만 두면 깊이 만큼 좌우대칭인 트리가 됨
#min_impurity_decrease(최소 불순도) 파라미터는 
#어떤 노드의 불순도 값이 설정값보다 작으면노드는 분할하지 않는다.

#불순도 = 정보이득*(노드의 샘플수)/(전체 샘플수)

#비대칭 트리생성
dt= DecisionTreeClassifier(min_impurity_decrease=0.0005, random_state=42)
dt.fit(X_train, Y_train)
dt.score(X_train,Y_train)#0.8975779967159278
dt.score(X_test,Y_test)#0.8590769230769231


dot_data = export_graphviz(dt, out_file=None, class_names=['red','white'], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('./비대칭결정트리_와인분류.png')

##최적의 파라미터를 찾는 방법






