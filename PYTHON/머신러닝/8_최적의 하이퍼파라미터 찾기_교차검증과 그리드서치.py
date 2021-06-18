#-----------------------------------------------------------------------------------------------------------------------------------------------------
#교차검증

#현재까지 파라미터 찾는 방식
#테스트 세트 데이터를 기준으로 파라미터를 바꿔 평가하면
#문제점 : 결국 테스트 세트에 잘 맞는 모델이 만들어짐

#테스트 세트로 일반화 성능을 올바르게 예측하려면
#가능한 한 테스트 세트를 사용하지 않아야 한다.
#(마지막에 딱 한번 사용)

#훈련 세트 60%, 검증세트 20%, 테스트세트 20%
#(1) 훈련세트에서 모델 훈련
#(2) 검증세트로 모델 평가 (매개변수 바꾸며 최적화)
#(3) 최적의 매개변수로 훈련세트와 검증세트를 합쳐
#다시 모델훈련
#(4) 테스트 세트를 통해 최종점수 평가

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

#2-2) 훈련/검증 데이터분할
X_train, X_valid, Y_train, Y_valid = train_test_split(X_train,Y_train, test_size=0.2,random_state=100)

X_train.shape, X_valid.shape, X_test.shape

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, Y_train)
dt.score(X_train, Y_train)#0.9971133028626413
dt.score(X_test, Y_test)#0.8461538461538461
#과대적합모델

#------------------------------------------------------------------------------------------------------------------------
#교차검증 : 검증 세트를 떼어 내어 평가하는 과정을 여러번 반복
#점수를 평균 내어 최종 점수를 얻음

#가장유명한 교차검증 k-폴드 교차검증 : 훈련세트를 k부분으로 나눠서 교차검증 수행
#ex) 3-폴드 교차검증
#훈련 데이터를 3세트로 나눔 : 훈련 세트1, 훈련세트2, 훈련세트 3
#(1)훈련세트 1 + 훈련세트2 합쳐 모델 훈련 -> 훈련세트 3으로 모델평가(평가 점수 1)
#(1)훈련세트 1 + 훈련세트3 합쳐 모델 훈련 -> 훈련세트 2으로 모델평가(평가 점수 2)
#(1)훈련세트 2 + 훈련세트3 합쳐 모델 훈련 -> 훈련세트 1으로 모델평가(평가 점수 3)
#검증점수 평균 = mean(평가점수 1, 평가점수 2, 평가점수 3)

#보통 5-폴드 교차검증 또는 10-폴드 교차검증을 많이 사용함
#훈련데이터의 80~90%까지 훈련에 사용할수 있다.
#검증 데이터는 줄어들지만 검증 점수 평균을 활용하기에 안정된 점수로 파악가능

from sklearn.model_selection import cross_validate
#기본적으로 5-폴드 교차검증 수행, cv파라미터로 값을 바꿀수 있음
scores = cross_validate(dt, X_train, Y_train )
scores
#'test_score': array([0.86923077, 0.84615385, 0.87680462, 0.84889317, 0.83541867]
import numpy as np
np.mean(scores['test_score'])#0.855300214703487

#훈련세트 섞는 분할기 지정
from sklearn.model_selection import StratifiedKFold
scores = cross_validate(dt, X_train, Y_train, cv = StratifiedKFold())
np.mean(scores['test_score'])#0.855300214703487

#훈련세트를 섞고 10-폴드 교차 수행하기
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, X_train, Y_train, cv = splitter)
np.mean(scores['test_score'])#0.8574181117533719

#교차검증 수행 목적 : 입력한 모델에서 얻을수 있는 최상의 검증 점수를 가능할수 있다.

#-------------------------------------------------------------------------------------------------------------------------------------------------
#하이퍼 파라미터 튜닝 (최적의 하이퍼 파라미터 찾기)
#모델 마다 적게는 1~2개, 5~6개의 하이퍼파라미터가 있다.
#튜닝방법
#(1) 탐색할 매개변수 지정
#(2) 그리스 서치를 수행하여 최상의 평균 검증 점수가 나오는 매개변수 조합 찾기
#(3) 그리스 서치는 최상의 매개변수에서 전체 훈련세트를 사용해 최종 모델을 훈련

#결정트리의 하이퍼 파라미터
#max_depth : 최대 깊이
#min_impurity_decrease : 불순도
#min_samples_split : 최소 샘플 개수에 따른 노드 분할 여부

from sklearn.model_selection import GridSearchCV
params ={'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}

#GridSearchCV의 cv(교차검증 기본값 5)
#총 5*5개의 훈련 모델 생성
gs = GridSearchCV(DecisionTreeClassifier(random_state=52),params,n_jobs=-1)#n_jobs : cpu코어 사용 개수 , -1 은 모두 사용
gs.fit(X_train, Y_train)
gs.cv_results_

gs.cv_results_['mean_test_score']#5번의 교차검증으로 얻은 평균점수
#array([0.86819186, 0.86549845, 0.86492263, 0.86780891, 0.86761605])
gs.cv_results_['rank_test_score']
#array([1, 4, 5, 2, 3])
gs.best_params_#베스트 파라미터
# {'min_impurity_decrease': 0.0001}

dt=gs.best_estimator_#베스트모델
dt.score(X_train,Y_train)#0.9613238406773138

#-----------------------------------------------------------------------------------------------------------------------------------------------
#최적의 매개변수 찾기 - 다양한 매개변수
params = {'min_impurity_decrease': np.arange(0.0001,0.001,0.0001), 'max_depth':range(3,20,1), 'min_samples_split':range(2,100,10)}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params, n_jobs=-1)
gs.fit(X_train, Y_train)
gs.best_params_
#{'max_depth': 14, 'min_impurity_decrease': 0.0004, 'min_samples_split': 12}
np.max(gs.cv_results_['mean_test_score'])#최상의 교차검증 점수
#0.8683865773302731

#최상의 모델
dt = gs.best_estimator_
dt.score(X_train,Y_train)#0.892053107562055

#----------------------------------------------------------------------------------------------------------------------------------------------
#랜덤서치 - 매개변수 범위값 랜덤
#매개변수의 값이 수치일 대 값의 범위나 감격을 미리 정하기 어려울수있다.
#또는 많은 매개변수로 테스트하기에 시간이 너무 오래걸린다.
#이런경우 랜덤 서치를 먼저 사용하는것이 좋다.

#랜덤서치에는 매개변수 값의 목록을 전달하지 않음
#매개변수를 샘플링 할 수 있는 확률분포 객체를 전달.

from scipy.stats import uniform, randint
#균등분포 샘플링 : 주어진 범위에서 고르게 값을 뽑는다.
#randint(이산형-정수), uniform(연속형 - 실수)
rgen = randint(0,10)#0~9까지 랜덤한수
rgen.rvs(10)#10개 샘플 추출

ugen = uniform(0,1)#0~1사이의 랜덤한 실수
ugen.rvs(10)

params = {'min_impurity_decrease': uniform(0.0001,0.001), 'max_depth':randint(2,50), 'min_samples_split':randint(2,25),'min_samples_leaf':randint(1,25)}
#min_samples_leaf : 리프노드가 되기위한 최소한의 샘플데이터 수
#min_samples_split : 노드를 분할하기위한 최소한의 샘플 데이터수
#둘다 과적합 제어 용도

from sklearn.model_selection import RandomizedSearchCV
#n_iter 만큼 샘플링하여 교차검증을 수행하고 최적의 매개변수 조합짜기
gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=52), params, n_iter=100, n_jobs=-1, random_state=30)

gs.fit(X_train,Y_train)

gs.best_params_
#{'max_depth': 34, 'min_impurity_decrease': 0.00042054899392536294, 'min_samples_leaf': 4, 'min_samples_split': 10}

np.max(gs.cv_results_['mean_test_score'])#0.8703105796994152
dt = gs.best_estimator_
dt.score(X_train,Y_train)#0.8903213392341736
dt.score(X_test,Y_test)#0.8592307692307692



















