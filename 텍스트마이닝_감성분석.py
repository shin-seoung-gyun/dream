#텍스트 마이닝 : 의미 있는 인사이트를 도출하기위해
#머신러닝의 고급 기술을 적용하여 발전된 분석기술

#텍스트 마이닝 분야 - 감성분석, 토픽 모델링
#감성분석 - 텍스트에서 사용자의 긍정 또는 부정의 감성을 결정
#감성 사전 기반의 감정분석은 감성 단어를 검색하여 점수 계산
#최근에는 머신러닝 기반의 감성분석으로 지도학습 방법으로 훈련

#토픽 모델링 - 문저를 구성하는 키워드 기반으로 토픽 추출
#LDA - 대표적인 머신러닝 기반 토픽 모델링 방법


#1) 데이터 수집 : https://github.com/e9t/nsmc

import pandas as pd

#한글 UnicodeEncodingError 방지하기 위해 기본인코딩 'utf-8'로 설정
import os
os.environ["PYTHONENCODING"]='UTF-8'
import warnings
warnings.filterwarnings(action='ignore')

#훈련용 데이터 로드
train_df = pd.read_csv("./머신러닝/ratings_train.txt",encoding='utf-8',sep='\t',engine='python')
print(train_df.head())
#데이터 전처리 및 탐색
print(train_df.info())
train_df = train_df[train_df['document'].notnull()]
train_df.info()

#타겟 컬럼 label 확인 (0:부정, 1:긍정)
train_df['label'].value_counts()
#desc 한글이외의 단어는 공백으로 변환 (정규표현식 활용)
import re
train_df['document']= train_df['document'].apply(lambda x:re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ",x))
train_df.head()

#평가용 데이터 준비
test_df = pd.read_csv("./머신러닝/ratings_test.txt",encoding='utf-8',sep='\t',engine='python')
test_df.head()
test_df.info()
test_df = test_df[test_df['document'].notnull()]
test_df['document']= test_df['document'].apply(lambda x:re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ",x))
test_df.head()
test_df.info()

# 3) 분석 모델 구축
# 3-1) 피처 벡터화 : TF-IDF
# 형태소 분석하여 토큰화 : Okt이용
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
okt = Okt()
def okt_tokenizer(text) :
    tokens = okt.morphs(text)
    return tokens
#TF-IDF기반  피처 벡터 생성

tfidf = TfidfVectorizer(tokenizer=okt_tokenizer, ngram_range=(1,2),min_df=3,max_df=0.9)
tfidf.fit(train_df['document'])
import pickle
with open('./머신러닝/tfidf.pickle','wb') as f:
    pickle.dump(tfidf, f)

train_tfidf = tfidf.transform(train_df['document'])
import pickle
with open('./머신러닝/train_tfidf.pickle','wb') as f:
    pickle.dump(train_tfidf, f)


#3-2) 감성 분류 모델 구축 : 로지스틱 회귀 모델 이진 분류
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=0)
lr.fit(train_tfidf,train_df['label'])

#로지스틱 회귀의 best 하이퍼파라미터 찾기
from sklearn.model_selection import GridSearchCV
params = {'C':[1,3,3.5,4,4.5,5]}
lr_grid_cv = GridSearchCV(lr, param_grid=params, cv=3, scoring='accuracy', verbose=1)

#최적 분석 모델로 훈련
lr_grid_cv.fit(train_tfidf, train_df['label'])
print(lr_grid_cv.best_params_, round(lr_grid_cv.best_score_,4))#0.8553훈련용 데이터를 통해 나온 정확도

with open('./머신러닝/lr_grid_cv.pickle','wb') as f:
    pickle.dump(lr_grid_cv, f)
#최적 파라미터의 best모델 저장
lr_best = lr_grid_cv.best_estimator_
with open('./머신러닝/lr_best.pickle','wb') as f:
    pickle.dump(lr_best, f)
#4) 분석 모델 평가
#4-1)평가용 데이터를 이용하여 감성 분석 모델 정확도
test_tfidf = tfidf.transform(test_df['document'])
test_predict = lr_best.predict(test_tfidf)

for i, val in enumerate(test_df['label']) :
    print(f"{i} 실제값 : {val}", end=', ')
    print(f"예측값 : {test_predict[i]}")

#감성분석 정확도
from sklearn.metrics import accuracy_score
print('감성분석 정확도 : ', round(accuracy_score(test_df['label'],test_predict),3))#테스트 데이터를 통해 나온 정확도

text = input('감성 분석할 문장 입력 >>')
## 입력 텍스트 데이터의 전저리 수행
text = re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]', " ", text)
#입력 데이터 피처 벡터화
text_tfidf = tfidf.transform([text])
print(text_tfidf)
#예측 값 출력하기
text_predict = lr_best.predict(text_tfidf)
if(text_predict==0):
    print(text, "--> 부정 감성")
else :
    print(text, "--> 긍정 감성")









