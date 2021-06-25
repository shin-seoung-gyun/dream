#실습5_스포츠 센터 탈퇴고객예측.py

#1) 데이터수집
import pandas as pd
customer = pd.read_csv('./data/customer_join.csv')
use_months = pd.read_csv('./data/use_log_months.csv')
customer.head()
use_months.head()

#2) 데이터 전처리
#2-1) 데이터 생성 : 현재달과 지난달 이용횟수
year_months = list(use_months['yyyymm'].unique())
year_months
uselog = pd.DataFrame()
for i in range(1, len(year_months)) :
    curData = use_months.loc[use_months['yyyymm']==year_months[i]]
    curData.rename(columns={'count':'count_0'},inplace =True)
    preData = use_months.loc[use_months['yyyymm']==year_months[i-1]]
    del preData['yyyymm']
    preData.rename(columns={'count':'count_1'},inplace =True)
    curData = pd.merge(curData, preData, 
                        on='customer_id', how='left')
    uselog = pd.concat([uselog, curData], ignore_index=True)
uselog.head()

#2-2) 데이터 생성 : 탈퇴 전월의 날짜 칼럼 생성
from dateutil.relativedelta import relativedelta
exit_customer = customer.loc[customer['is_deleted']==1]
exit_customer['exit_date'] = None
exit_customer['end_date'] = pd.to_datetime(exit_customer['end_date'])

for i in range(len(exit_customer)) :
    exit_customer['exit_date'].iloc[i] = \
        exit_customer['end_date'].iloc[i] - relativedelta(months=1)

exit_customer.info()

#탈퇴 회원 uselog데이터 
exit_customer['yyyymm'] = \
    pd.to_datetime(exit_customer['exit_date']).dt.strftime('%Y%m')
exit_customer.head()
exit_customer.info() #yyyymm 문자열 타입
uselog.info() #yyyymm int64

#타입변환
uselog['yyyymm'] = uselog['yyyymm'].astype(str)
exit_useLog = pd.merge(uselog, exit_customer, 
        on=['customer_id', 'yyyymm'], how='left')
exit_useLog.head()
len(exit_useLog)

#결측치 데이터 삭제
exit_useLog = exit_useLog.dropna(subset=['name'])
len(exit_useLog) #1104
exit_useLog.head()
#탈퇴회원수
len(exit_useLog['customer_id'].unique())
#1104

#지속회원 데이터 얻기
conti_customer = customer.loc[customer["is_deleted"]==0]
conti_uselog = pd.merge(uselog, conti_customer, on=['customer_id'],
    how='left')
conti_uselog.head()
len(conti_uselog)
#결측치 제거
conti_uselog.isnull().sum()
conti_uselog = conti_uselog.dropna(subset=['name'])
conti_uselog.head()


#탈퇴회원 데이터 1104, 지속회원 데이터 27422
#지속회원 데이터 중복제거
#70% 데이터 랜덤하게 가져오기
conti_uselog = conti_uselog.sample(frac=0.7).reset_index(drop=True)
conti_uselog.drop_duplicates(subset='customer_id', inplace=True)
len(conti_uselog) #2816

#지속회원과 탈퇴회원 세로로 결합
predict_data = pd.concat([conti_uselog, exit_useLog], 
        ignore_index=True)
len(predict_data) #3920
predict_data.head()

#다닌 기간(월) 칼럼 추가
predict_data['period'] = 0
predict_data['now_date'] = pd.to_datetime(predict_data['yyyymm'],
                            format='%Y%m')
predict_data['start_date'] = pd.to_datetime(predict_data['start_date'])
for i in range(len(predict_data)) :
    delta = relativedelta(predict_data['now_date'][i], 
            predict_data['start_date'][i])
    predict_data['period'][i] = int(delta.years*12 + delta.months)
predict_data.head() 

#결측치 제거
predict_data.isna().sum() #count_1               233
predict_data.dropna(subset=['count_1'], inplace=True)
predict_data.isna().sum() 


#분석데이터 구축
#독립변수 : count_1,class_name,campaign_name,gender,mean,routine_flg,period
#종속변수 : is_deleted

feature_col = ['gender','class_name','campaign_name','count_1','mean','routine_flg','period']
X= predict_data[feature_col]
Y= predict_data['is_deleted']
X.head()
Y.head()

#문자열 더미변수생성
X = pd.get_dummies(X)
X.head()
X.info()

#더미 칼럼 삭제
del X['gender_M']#gender_F=0 남자
del X['class_name_2_야간']#둘다0이면 야간
del X['campaign_name_2_일반']#둘다 0이면 일반
X.head()


#3) 분석모델 구축
#의사결정 트리 활용
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=0)

model = DecisionTreeClassifier(random_state=0)
scores = cross_validate(model, X_train, Y_train)
import numpy as np
np.mean(scores['test_score'])#0.9873371858374609

model.fit(X_train, Y_train)
model.score(X_train,Y_train)#1.0
model.score(X_test,Y_test)#0.9837310195227765

#최적의 파라미터 찾기 - 그리드 서치
from sklearn.model_selection import GridSearchCV
params ={
    'max_depth':range(2,15,1)
}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(X_train, Y_train)
gs.best_params_
np.max(gs.cv_results_['mean_test_score'])#0.9873378410252378



model = DecisionTreeClassifier(random_state=0, max_depth=4)

model.fit(X_train, Y_train)
model.score(X_train,Y_train)#0.9833151976786362

#-----------------------------------------------------------------------------------------------------------------------
#결정트리 시각화


import pydotplus
from sklearn.tree import export_graphviz

dot_data = export_graphviz(model, out_file=None,
                           feature_names=X_train.columns,
                           class_names=['contin','exit'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_png('./결정트리_스포츠센터탈퇴고객.png')


#모델에 기여하고있는 변수 확인
importance = pd.DataFrame({'feature_names':X.columns,'coef':model.feature_importances_})
importance

#회원탈퇴 예측
count_1 = 3
routine_flg =1
period = 10
campaign_name=[0,1]#입회비 무료
class_name=[1,0]#종일
gender = [0]#남자
mean = 5#한달평균 이용횟수
input_data = [count_1,mean,routine_flg,period]
input_data += gender
input_data += class_name
input_data += campaign_name

input_data
model.predict([input_data])#array([1.])
model.predict_proba([input_data])#array([[0.03626943, 0.96373057]])





