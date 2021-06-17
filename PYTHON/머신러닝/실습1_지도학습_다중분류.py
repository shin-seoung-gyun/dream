import pandas as pd
import numpy as np

#데이터 수집

#피쳐 이름 가져오기
feature_name_df = pd.read_csv('./data/features.txt',sep='\s+',header=None, names=['index','feature_name'])
feature_name_df.info()
feature_name_df.head()
feature_name_df.shape#(561,2)
feature_name_df['feature_name']=feature_name_df['index'].astype('str')+'_'+feature_name_df['feature_name']

X_train = pd.read_csv('./data/X_train.txt',sep='\s+',header=None, names=feature_name_df['feature_name'])
X_train.head()
X_train.info()

X_test = pd.read_csv('./data/X_test.txt',sep='\s+',header=None, names=feature_name_df['feature_name'])
X_test.head()
X_test.info()

Y_train = pd.read_csv('./data/Y_train.txt',sep='\s+',header=None, names=['action'])
Y_train.head()
Y_train.info()

Y_test = pd.read_csv('./data/Y_test.txt',sep='\s+',header=None, names=['action'])
Y_test.head()
Y_test.info()
#----------------------------------------------------------------------------------------------------------------------------------------------------
#데이터 정규화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)
#모델 구축
from sklearn.linear_model import LogisticRegression
lr =LogisticRegression(C=1, max_iter=100)
lr.fit(X_train_scaled,Y_train)
#모델평가
lr.score(X_train_scaled,Y_train)#0.9965995647442872
lr.score(X_test_scaled,Y_test)#0.9531727180183237

lr.predict(X_test_scaled[100:140])
Y_test[100:140]




















