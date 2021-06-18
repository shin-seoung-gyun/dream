#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#지금까지 배운 머신러닝 알고리즘은 정형 데이터에 잘 맞다.
#비정형데이터는 딥러닝 분야

#앙상블 학습 : 정형 데이터 처리에 가장 뛰어난 성적을 내는 알고리즘
#대부분 의사결정 트리 기반으로 만들어져 있음


#랜덤 포레스트
#앙상블 학습의 대표적인 알고리즘
#결정트리를 랜덤하게 만들어 숲을 만들고, 각 결정 트리의 예측을 사용해 최종 예측을 만든다.

#부트스트랩샘플 : 입력한 훈련데이터 에서 랜덤하게 샘플추출(복원추출) 하여, 부스트랩샘플을 통해 결정트리를 개별로 훈련

#랜덤포레스트는 기본적으로 100개의 결정 트리를 위와 같은 방법으로 훈련\
#분류일때 각 트리의 클래스별 확률을 평균하여 가장 높은 확률을 가진 클래스 (타겟) 예측
#회귀일때 각 트리의 예측을 평균

#각 노드분할시 전체 특성중에서 일부특성을 무작위로고른다음 이중에서 최선의 분할을 찾는다.
#분류시 기본적으로 전체 특성개수의 제곱근만큼 특성 선택
#회귀시 전체특성모두 사용

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#알고리즘 성능테스트 - 교차 검증 수행 다시봐야할듯
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, X_train, Y_train, n_jobs=-1)
scores
#{'fit_time': array([0.19041538, 0.19141388, 0.19141388, 0.19141388, 0.19041538]), 
# 'score_time': array([0.02293897, 0.02293777, 0.02194047, 0.02194047, 0.02293897]), 
# 'test_score': array([0.88461538, 0.88942308, 0.90279115, 0.88931665, 0.88642926])}    

import numpy as np
np.mean(scores['test_score'])#0.8905151032797809
scores = cross_validate(rf, X_train, Y_train, n_jobs=-1, return_train_score=True)
scores
# {'fit_time': array([0.18510056, 0.18510056, 0.18510056, 0.18510056, 0.18510056]), 
# 'score_time': array([0.03124213, 0.03124213, 0.03124213, 0.03124213, 0.03124213]), 
# 'test_score': array([0.88461538, 0.88942308, 0.90279115, 0.88931665, 0.88642926]), 
# 'train_score': array([0.9971133 , 0.99663219, 0.9978355 , 0.9973545 , 0.9978355 ])}


np.mean(scores['train_score'])#0.9973541965122431 훈련데이터
np.mean(scores['test_score'])#0.8905151032797809 검증데이터(자동으로 나눠주는듯)
#과대적합

rf.fit(X_train, Y_train)
rf.feature_importances_
#array([0.23167441, 0.50039841, 0.26792718])
#결정트리에 비해 각 피쳐들의 중요도가 균등함.

#OOB Score : 부트스트랩 샘플에서 하나의 결정 트리모델 훈련시에 남는 샘플로 성능평가

rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=52)
rf.fit(X_train, Y_train)
rf.oob_score_#0.8968635751395035
#OOB Score는 교차검증을 대신할수 있다.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2. 그레디언트 부스팅
#깊이가 앝은 결정트리를 사용해서 이전 트리의 오차를 보완하는 방식
#기본적으로 깊이가 3인 결정트리 100개 사용
#과대적합에 강하고 일반적으로 높은 성능을 기대할 수 있다.
#경사 하강법을 사용하여 트리를 앙상블에 추가한다.
#분류에서는 로지스틱 손실 함수, 회귀에서는 평균 제곱 오차함수 사용

#경사하강법을 통해
#결정트리를 계속 추가하면서 기울기가 가장 낮은 곳으로 가중치와 절편을 조금씩 바꿈
#학습률 매개변수로 학습속도 조절 가능

#일반적으로 그레디언트 부스팅이 랜덤 포레스트보다 조금더 높은 성능을 얻을수 있다.
#단점 : n_jobs 매개변수가 없다. gpu사용 못함. 훈련속도가 느리다.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, X_train, Y_train, return_train_score=True, n_jobs=-1)
np.mean(scores['train_score']), np.mean(scores['test_score'])
# (0.8881086892152563, 0.8720430147331015)
#과대적합 되지 않음

#매개변수 최적화
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
#n_estimators : 트리의 개수(기본값 100)
#learning_rate : 학습률 (기본값 1.0)
scores = cross_validate(gb, X_train, Y_train, return_train_score=True, n_jobs=-1)
np.mean(scores['train_score']), np.mean(scores['test_score'])
#(0.9464595437171814, 0.8780082549788999)

gb.fit(X_train,Y_train)
gb.score(X_train, Y_train)#0.9382335963055609
gb.score(X_test, Y_test)#0.8707692307692307

gb.feature_importances_
#array([0.15872278, 0.68011572, 0.16116151])

#랜덤 포레스트보다 일부특성에 더 집중
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3. 히스토그램 기반 그레디언트 부스팅
#정형데이터 다루는 머신러닝 알고리즘중에 가장 인기가 높은 알고리즘
#그레디언트 부스팅의 속도와 성능을 더욱 개선한 알고리즘

#입력특성을 256개의 구간으로 나눔(노두 분할시 최적의 분할을 빠르게 찾는다)
#256개의 구간중 하나를 떼어놓고 누락된 값을 위해서 사용
#입력에 누락된 특성이 있더라도 따로 전처리할 필요가 없다.

#기본적인 파라미터로 성능이 좋다
#트리개수 지정시 max_iter 매개변수 사용 (n_estimators가 아님)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier

hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, X_train, Y_train, return_train_score=True, n_jobs=-1)
np.mean(scores['train_score']), np.mean(scores['test_score'])
#(0.9321723946453317, 0.8801241948619236)

#특성 중요도 계산 바로 얻을순 없음
from sklearn.inspection import permutation_importance
hgb.fit(X_train, Y_train)
result = permutation_importance(hgb, X_train, Y_train, n_repeats=10, random_state=42, n_jobs=-1)
#n_repeats 는 특성을 랜덤하게 섞어서 모델의 성능이 변화하는지 관찰
#n_repeats 는 랜덤하게 섞을 횟수 지정(기본값 5)
result
result.importances_mean
# array([0.08876275, 0.23438522, 0.08027708])

hgb.score(X_test, Y_test)
#0.8723076923076923

##딥러닝 이전까지 가장좋은 알고리즘이다.



