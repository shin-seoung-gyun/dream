import pandas as pd
redwine = pd.read_csv('winequality-red.csv', sep=';')
redwine.head()
redwine.info()

X=redwine.iloc[:,:-1]
X
Y=redwine.iloc[:,-1]
Y

#훈련데이터/테스트데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,10))
sns.heatmap(redwine.corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm_r')
plt.show()

#random forest 를 통한 피치 중요도 확인
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=10, random_state=10)
rf_model.fit(X_train, Y_train)
rf_model.feature_importances_

import numpy as np
feature_df = pd.DataFrame(data=np.c_[X.columns, rf_model.feature_importances_], 
            columns=["feature",'importance'])
feature_df.sort_values(by='importance', ascending=False, inplace=True)
feature_df.reset_index(drop=True, inplace=True)
feature_df

plt.figure(figsize=(12,8))
plt.bar(feature_df.feature, feature_df.importance)
plt.xticks(feature_df.feature, fontsize=12, rotation=45)
plt.show()

y_cumsum = np.cumsum(feature_df.importance, axis=0)
plt.figure(figsize=(12,8))
plt.bar(feature_df.feature, y_cumsum)
plt.xticks(feature_df.feature, fontsize=12, rotation=45)
plt.show()

#RFE를 통한 최적의 k개 피쳐 찾기
from sklearn.feature_selection import RFE
rf_model = RandomForestClassifier(n_estimators=10, random_state=10)
rfe = RFE(rf_model, n_features_to_select=5)
rfe.fit(X_train,Y_train)
rfe.get_support()
# array([False,  True, False, False, False, False,  True, False,  True,
#         True,  True])
feature_rfe = pd.DataFrame(data=np.c_[X.columns.values, rfe.get_support()], columns=['feature', 'selected'])
feature_rfe.sort_values(by='selected', ascending=False)
#                  feature selected
# 1       volatile acidity     True
# 6   total sulfur dioxide     True
# 8                     pH     True
# 9              sulphates     True
# 10               alcohol     True
# 0          fixed acidity    False
# 2            citric acid    False
# 3         residual sugar    False
# 4              chlorides    False
# 5    free sulfur dioxide    False
# 7                density    False


#로지스틱 회귀분류로 
from sklearn.linear_model import LogisticRegression
lr_model= LogisticRegression()
rfe = RFE(lr_model, n_features_to_select=5)
rfe.fit(X_train,Y_train)
rfe.get_support()
# array([False,  True, False, False, False, False,  True, False,  True,
#         True,  True])
feature_rfe = pd.DataFrame(data=np.c_[X.columns.values, 
                        rfe.get_support()], columns=['feature', 'selected'])
feature_rfe.sort_values(by='selected', ascending=False)
#                 feature selected
# 1       volatile acidity     True
# 7                density     True
# 8                     pH     True
# 9              sulphates     True
# 10               alcohol     True
# 0          fixed acidity    False
# 2            citric acid    False
# 3         residual sugar    False
# 4              chlorides    False
# 5    free sulfur dioxide    False
