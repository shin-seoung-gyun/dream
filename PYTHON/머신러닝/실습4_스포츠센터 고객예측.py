#1. 어떤 고객의 다음달 이용 횟수 예측 (회귀분석)
#독립변수 : 과거 6개월 분의 이용횟수 + 멤버십 기간
#
#1)데이터 수집
import pandas as pd

uselog =pd.read_csv('./data/use_log.csv')
uselog.info()

#2) 데이터 전처리
#2-1)월별 데이터 칼럼 생성
uselog['usedate'] = pd.to_datetime(uselog['usedate'])
uselog['yyyymm'] = uselog['usedate'].dt.strfrime("%Y%m")
uselog.head()
#회원별 월별 이용 횟수
uselog_months = uselog.groupby(['yyyymm', 'customer_id'], as_index=False).count()
uselog_months.head()
#칼럼수정
uselog_months.rename(columns={'log_id':'count'}, inplace=True)
del uselog_months['usedate']
uselog_months.head()

#2-2)현재달 이용횟수및 과거6개월 이요횟수 데이터 생성
yearMonList = list(uselog_months['yyyymm'].unique())
yearMonList
# ['201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812', '201901', '201902', '201903']

predict_data = pd.DataFrame()
for i in range(6, len(yearMonList)):
    curData = uselog_months.loc[uselog_months['yyyymm']==yearMonList[i]]
    curData.rename(columns={'count':"count_target"}, inplace=True)
    #과거 6개월 데이터
    for j in range(1,7) :
        preData = uselog_months.loc[uselog_months['yyyymm']==yearMonList[i-j]]
        del preData['yyyymm']
        preData.rename(columns={'count':f"count_{j-1}"}, inplace=True)
        curData = pd.merge(curData, preData, on='customer_id', how='left')
    
    predict_data = pd.concat([predict_data,curData], ignore_index=True)

predict_data.head()



#결측치 제거
predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)
predict_data.head()

#회원기간 독립변수(피쳐) 추가
customer = pd.read_csv('./data/customer_join.csv')
customer.head()
predict_data_mer =  pd.merge(predict_data, customer[['customer_id', 'start_date']], on='customer_id', how='left')
predict_data_mer.head()
predict_data_mer.info()
#데이트 타입 형변환
predict_data_mer['now_date']=pd.to_datetime(predict_data_mer['yyyymm'],format='%Y%m')
predict_data_mer['start_date'] = pd.to_datetime(predict_data_mer['start_date'])
#두 날짜의 계산
from dateutil.relativedelta import relativedelta
predict_data_mer['period'] = None
for i in range(len(predict_data_mer)):
    delta = relativedelta(predict_data_mer['now_date'][i],predict_data_mer['start_date'][i])
    predict_data_mer['period'] = delta.years*12 + delta.months
predict_data_mer.head()


uselog['usedate'].min()
predict_data_mer['start_date'].min()
# Timestamp('2015-05-01 00:00:00')

predict_data_mer = predict_data_mer.loc[predict_data_mer['start_date']>=pd.to_datetime('20180401')]
predict_data_mer['start_date'].min()

#3) 분석모델 구축
from sklearn import linear_model
from sklearn.model_selection import train_test_split
model = linear_model.LinearRegression()
X= predict_data_mer[['count_0','count_1','count_2','count_3','count_4','count_5','period']]
X.head()
Y=predict_data_mer['count_target']
Y.head()
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=3)
model.fit(X_train, Y_train)

model.score(X_train,Y_train)#0.6061787419944431
model.score(X_test,Y_test)#0.6067607729036852
#과소적합
#해결방안 : 독립변수 추가

#모델에 기여하는 변수 확인
coef = pd.DataFrame({'feature' : X.columns, 'coef':model.coef_})
coef


#데이터 예측
x1=[3,4,4,6,8,7,8]
x2=[2,2,3,3,4,6,8]
x_pred = [x1, x2]
model.predict(x_pred)
# array([3.74893614, 1.92550618])

uselog_months.to_csv('./data/use_log_months.csv', index=False)






