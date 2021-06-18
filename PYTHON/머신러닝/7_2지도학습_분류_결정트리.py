#------------------------------------------------------
#의사결정트리 : 데이터 분류 기준을 여러개 세워 분류 정확도를 높임
#데이터 분류에 대한 명확한 기준과 이유를 제시 (해석이 용이)
#-------------------------------------------------------
#Ex) 화이트와인, 레드와인 분류
#클래스 0이면 레드와인, 1이면 화이트와인

#1.로지스틱회귀분석 분류
#1) 데이터 수집
import pandas as pd
wine = pd.read_csv('./data/wine.csv') 
wine.head()
wine.info()

#2) 데이터 탐색 및 전처리
wine.groupby('class').describe()
data = wine.drop('class', axis=1)
target = wine['class']
#2-1) 훈련/테스트 데이터분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    data, target, test_size=0.2, random_state=42)
X_train.shape, X_test.shape
#2-2) 데이터 표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)

#3) 분석모델구축
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter=1000, C=20)
lr.fit(X_train_scaled, Y_train)

#4) 모델평가 및 결과분석
lr.score(X_train_scaled, Y_train) #0.7808
lr.score(X_test_scaled, Y_test) #0.77
#4-1) 모델에 기여하는 변수 확인
coef_df = pd.DataFrame({'features':X_train.columns, 'coef':lr.coef_[0]})
coef_df

coef_df = pd.DataFrame(lr.coef_, columns=X_train.columns)
coef_df

#Z = 0.5*alchol + 1.68*sugar-0.688*ph+1.82
#sigmoid(z) => 확률값 0~1

#-----------------------------------------------------------
#2.결정트리 모델
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_scaled, Y_train)

dt.score(X_train_scaled, Y_train) #0.9969
dt.score(X_test_scaled, Y_test) #0.859
#성능은 향상되었으나 과대적합

#의사결정트리 모델 시각화
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(10, 7))
plot_tree(dt)
plt.show()

plt.figure(figsize=(10, 7))
plot_tree(dt, max_depth=1, filled=True, feature_names=X_train.columns)
plt.show()

#---------------------------------------------
#노드 : 결정 트리를 구성하는 핵심요소. 노드는 훈련 데이터의 특성에 대한
#테스트를 나타낸다.
#일반적으로 하나의 노드는 2개의 가지를 가진다.
#맨 위의 노드를 루프노드, 맨 아래의 노드를 리프노드라 한다.

#노드에 있는 정보
#테스트 조건  : sugar < -0.239
#불순도(지니계수) : gini = 0.367
#총샘플수 :  samples = 5197
#클래스별 샘플 수 : value = [1258, 3939]

#의사결정트리분류기준 (gini계수)
#지니불순도 = 1-(음성 클래스의 비율^2 + 양성 클래스의 비율^2)
#값이 작을수록 한 클래스의 비율이 높음

#정보이득 : 부모와 자식 노드의 불순도 차이
#결정트리모델은 부모노드와 자식노드의 불순도 차이가 가장 크도록 
#트리를 성장시킴
#정보이득이 최대가 되도록 데이터를 나눈다.

#과대적합방지 : 트리의 깊이 제한
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train_scaled, Y_train)

dt.score(X_train_scaled, Y_train) #0.84548
dt.score(X_test_scaled, Y_test) #0.8415

plt.figure(figsize=(20, 15))
plot_tree(dt, filled=True, feature_names=X_train.columns)
plt.show()


#pip install pydotplus
#pip install graphviz


# out_file=None : 결과를 파일로 저장하지 않겠다.
# filled=True : 상자 채우기
# rounded=True : 상자모서리 둥그렇게 만들기
# special_characters=True : 상자안에 내용 넣기

import pydotplus
from sklearn.tree import export_graphviz

dot_data = export_graphviz(dt, out_file=None,
                           feature_names=X_train.columns,
                           class_names=['red','white'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_png('./결정트리_와인분류.png')


#결정트리는 데이터 표준화를 안해도 된다.
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, Y_train)

dt.score(X_train, Y_train) #0.84548
dt.score(X_test, Y_test) #0.8415

dot_data = export_graphviz(dt, out_file=None,
                           feature_names=X_train.columns,
                           class_names=['red','white'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_png('./결정트리_와인분류.png')

#결과해석
#레드와인 = 당도<1.625 AND 알콜<11.025
#나머지 화이트와인

#특성중요도 : 어떤 특성이 가장 유용한지 나타낸다.
#각 노드의 정보이득과 전체 샘플에 대한 비율을 곱한 후
#특성별로 계산
dt.feature_importances_

pd.DataFrame({'features':X_train.columns, 
    'importances':dt.feature_importances_})
#  features  importances
#0  alcohol     0.123456
#1    sugar     0.868629
#2       pH     0.007914

#결정트리 모델이 나중에 앙상블 학습 알고리즘 기반이된다.
#앙상블학습은 신경망과 함꼐 가장 높은 성능을 나타냄

#-----------------------------------------
#결정트리의 깊이값만 두면 깊이만큼 좌우대칭인 트리가됨
#min_impurity_decrease(최소 불순도) 파라미터는
#어떤 노드의 불술도값이 설정값보다 작으면 노드는 분할하지
#않는다.
#불순도 = 정보이득*(노드의 샘플수)/(전체 샘플수)

#비대칭 트리 생성
dt =  DecisionTreeClassifier(
    min_impurity_decrease=0.0005, random_state=42)
dt.fit(X_train, Y_train)
dt.score(X_train, Y_train)
dt.score(X_test, Y_test)
dot_data = export_graphviz(dt, out_file=None,
                           feature_names=X_train.columns,
                           class_names=['red','white'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('./비대칭결정트리_와인분류.png')