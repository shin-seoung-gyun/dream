from sklearn.datasets import load_iris
data = load_iris()
data.data.shape#(150, 4)
data.data

data.target.shape#(150,)

#피쳐 개수 2개
X=data.data[:,2:]
Y=data.target
feature_names = data.feature_names[2:]
feature_names
# ['petal length (cm)', 'petal width (cm)']

from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=1, random_state=0)
dt_model.fit(X,Y)

#의사결정나무 시각화
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(10,7))
plot_tree(dt_model)
plt.show()

dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)
dt_model.fit(X,Y)
plt.figure(figsize=(10,7))
plot_tree(dt_model)
plt.show()

#의사결정나무는 설명하기 좋고, 중요 피쳐 찾기 편함.
dt_model.feature_importances_#array([0.07856379, 0.92143621])
dt_model.score(X,Y)#0.9933333333333333

