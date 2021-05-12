#로지스틱 회귀는 분류에 사용된다.
#추세를 예측하는 선형회귀와 달리 S자 함수를 사용하여 참, 거짓을 분류한다.
#로지스틱에서 많이 사용하는 S함수가 시그모이드함수(1/(1+e^x))
#이진 분류에 사용



import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

#1) 데이터 수집
b_cancer = load_breast_cancer()

#2) 데이터 전처리 및 탐색
print(b_cancer.DESCR)
b_cancer_df = pd.DataFrame(b_cancer.data,columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target
print(b_cancer_df.head())
print("유방암 진단 데이터셋 크기 :",b_cancer_df.shape)
print(b_cancer_df.info())

#3) 데이터 정규화 작업(평균 0 , 분산 1 - 정규분포형태)
#정규화 식 : (X-X평균)/(X표준편차)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)
print(b_cancer.data[0])#  1.799e+01=1.799*10
print(b_cancer_scaled[0])# 1

# b_cancer_df = b_cancer_df.apply(lambda x : (x-x.mean())/x.std(),axis=0)
# print(b_cancer_scaled[0])
# print(b_cancer_df.iloc[0])

#3) 분석모델 구축 : 로지스틱 회귀 모델
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#x,y데이터 생성 - Y-유방암 여부, X- 환자의료 데이터
Y=b_cancer_df['diagnosis']
X = b_cancer_scaled

#훈련 및 테스트 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=0)
#모델생성
lr_b_cancer = LogisticRegression()
lr_b_cancer.fit(X_train, Y_train)

#4)모델 평가 및 결과 분석
Y_predict = lr_b_cancer.predict(X_test)
for i in range(len(Y_predict)):
    print("예측값 : ",Y_predict[i], end=", ")
    print("실제값 : ",Y_test.iloc[i])

#오차 행렬 출력
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, roc_auc_score,recall_score,f1_score
print(confusion_matrix(Y_test,Y_predict))
#[[ 60   3]
# [  1 107]]

#정확도 - (예측결과와 실제값이 동일한 건수)/ 전체 데이터수
accuracy = accuracy_score(Y_test, Y_predict)
print(f"정확도 : {accuracy:>0.3}")

#정밀도 - 예측이 참인것 중에서, 실제 결과값이 참인것의 비율
precision = precision_score(Y_test, Y_predict)
print(f"정밀도 : {precision:>0.3}")

#재현율 = 실제값이 참인것중에서 예측값이 참인것의 비율
#실제 Positive 데이터를 정확히 예측했는지 평가 지표 (민감도)
recall = recall_score(Y_test, Y_predict)
print(f"재현율 : {recall:>0.3}")

#F1스코어 = 정밀도와 재현율을 결합한 평가 지표
f1 = f1_score(Y_test, Y_predict)
print(f"f1스코어 : {f1:>0.3}")

#roc auc - FPR(실제는 거짓인데 참이라 예측한 경우)이 변할때 TPR(실제는 참인데 참이라 예측한 경우)이 어떻게 변하는지 나타내는 곡선, roc곡선의 
# 면적을 구한 값이 1에 가까울수록 성능이 좋다

roc_auc=roc_auc_score(Y_test, Y_predict)
print(f"roc_auc : {roc_auc:>0.3}")

##새로운 데이터를 통해 유방암 여부 진단(정규화된 데이터를 입력해야함)
print("새로운 환자 유방암 여부",b_cancer_df.loc[0,'diagnosis'])
b_cancer_df.drop(['diagnosis'],inplace=True,axis=1)
pData = b_cancer_df.iloc[0]
meanSr=b_cancer_df.mean()
stdSr=b_cancer_df.std()
pDataList = []
print(pData)
for i,val in enumerate(pData) :
    pDataList.append(val-meanSr[i]/stdSr[i])
print(pDataList)

b_cancer_predict = lr_b_cancer.predict([pDataList])
print("새로운 환자의 유방암 여부 :", b_cancer_predict)





