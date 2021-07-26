import seaborn as sns
iris = sns.load_dataset('iris')
iris
iris.info()
X = iris.iloc[:,:-1]
X
Y = iris.iloc[:,-1]
Y

#훈련/ 테스트 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=1, stratify=Y)
X_train.shape
X_test.shape

#모델생성
#의사결정나무
from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier(random_state=1)
dt_model.fit(X_train, Y_train)

#사이킷런 간단한 신경망모델
from sklearn.neural_network import MLPClassifier
mlp_model = MLPClassifier(hidden_layer_sizes=(50,50,20), max_iter=500, random_state=1)
mlp_model.fit(X_train, Y_train)

dt_pred_y=dt_model.predict(X_test)
mlp_pred_y=mlp_model.predict(X_test)

#모델 평가
dt_model.score(X_test, Y_test)
mlp_model.score(X_test, Y_test)

#교차집계표로 결과 시각화
import pandas as pd
pd.crosstab(Y_test, dt_pred_y)
pd.crosstab(Y_test, mlp_pred_y)

