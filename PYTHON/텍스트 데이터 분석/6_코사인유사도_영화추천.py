#6_코사인유사도_영화추천.py
#--------------------------------------
#텍스트 마이닝 : 비정형 텍스트 데이터로부터 패턴을 찾아내어
#의미 있는 정보를 추출하는 분석 과정

#텍스트 마이닝 과정
#텍스트 전처리 -> 특성 벡터화 -> 모델 구축/훈련 -> 평가 및 결과분석

#텍스트 전처리 : 토큰화, 불용어 제거, 표제어 추출, 형태소 분석 등의
#작업이 포함됨

#특성벡터화 : 텍스트를 구성하는 단어를 추출하고 이를 숫자형 값인
#벡터 값으로 표현한다.
#특성 벡터화의 대표적인 방법 Bow(Bag of Words)와 Word Embedding이있음.

#1.Bow는 문서가 가지고 있는 모든 단어에 대해 순서는 무시한 채
#빈도만 고려하여 단어가 얼마나 자주 등장하는 지로 특성 벡터를 만든다.
#알고리즘 종류 : 카운트 기반 벡터화, TF-IDF
#(1) 카운트 기반 벡터화 : 단어가 전체 문서에 등장하는 횟수,
#빈도수를 부여하는 벡터화 방식(정수값으로 할당)
#단어 출현 빈도가 높을수록 중요한 단어로 다루어진다.
text = ['I go to my home my home is very large', 
    'I went out my home I go to the market', 
    'I bought a yellow lemon I go back to home']
from numpy.core.numeric import indices
from sklearn.feature_extraction.text import CountVectorizer
vector = CountVectorizer()
vector.fit_transform(text).toarray()
vector.vocabulary_.items()
sorted(vector.vocabulary_.items())

#(2) TF-IDF 기반 벡터화 : 빈도가 높은 단어가 문서에서 많이 사용된
#중요한 단어일 수도 있지만 단지 문장 구성상 많이 사용하는 단어 일
#수도 있음. 이런 문제를 보완하기 위해 특정 문서에 많이 나타나는
#단어는 해당 문서의 단어 벡터에 가중치를 높이고, 모든 문서에
#많이 나타나는 단어는 문장을 구성하는 범용적인 단어로 취급하여
#가중치를 낮추는 방식
text = ['I go to my home my home is very large', 
    'I went out my home I go to the market', 
    'I bought a yellow lemon I go back to home']
from sklearn.feature_extraction.text import TfidfVectorizer
vector = TfidfVectorizer()
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())

#min_df (Df : document frequency) : 단어의 최소 빈도값을 설정하는
#파라미터. DF는 특정 단어가 나타나는 '문서의 수'를 의미한다.
#EX) 'home' 단어의 빈도는 4이지만 DF는 3문장에서 나왔기에 3이다.
vector = TfidfVectorizer(min_df=3)
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())
#max_df : 최대 몇개 문서에 걸쳐 포함된 단어까지 학습단어로 사용할것인지
#[0.0, 1.0] 실수 범위로 문서의 비율을 설정할수있음
vector = TfidfVectorizer(max_df=0.9)
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())

#n-gram : 단어의 묶음 범위 설정
#ngram_range = (1,1)이라면 단어의 묶음을 1개부터 1개까지 설정 
#ngram_range = (1,2)이라면 단어의 묶음을 1개부터 2개까지 설정
vector = TfidfVectorizer(ngram_range=(1,1))
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())

vector = TfidfVectorizer(ngram_range=(1,2))
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())

#max_feature는 tf-idf vector의 최대 피쳐 개수를 설정해주는 파라미터
vector = TfidfVectorizer(max_features=5)
vector.fit_transform(text).toarray()
sorted(vector.vocabulary_.items())
#문서의 양이 많을 경우 일반적으로 TF-IDF 방식의 벡터를 사용한다.

#2.Word Embedding
#단어를 벡터로 표현한것. 워드 임베딩은 그 자체로 딥러닝 기술이다.
#워드 임데딩은 비슷한 의미의 단어가 비슷한 위치에 매핑되게 함으로써
#유사도를 잘 반영한 벡터 표현.
#단순 토큰화에 비해 단어간의 유사성과 관계의 표현이 가능하다.

#알고리즘 : Word2Vec, Glove
#(1) Word2Vec
#같은 문장에 나타난 인접한 단어들 간의 의미가 비슷할 것이라 가정하여
#비슷한 의미의 단어들을 가깝게 매핑
#ex) the cat hunts mice 문장이 있을 때, 같은 단어인 cat을 기준으로
#앞 뒤의 단어들이 cat과 연관이 있다고 가정

#따라서 한 단어가 주변에 등장하느 단어들을 통해 의미를 알 수 있다고
#생각한다. 

#Word2vec 모형
#CBOW : 주변 단어를 통해 중심 단어를 에측 
#Skip-gram : 중심 단어를 통해 주변 단어를 예측
#ex) i am going to school
#CBOW는 I, AM, TO, SCHOOL을 통해 GOING을 예측
#Skip-gram은 Going으로 나머지 단어들을 예측
#-------------------------------------------------------
from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(a,b) :
    return dot(a,b)/(norm(a)*norm(b))

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('./data/movies_metadata.csv', low_memory=False)
data.head()
data.info()

#샘플 개수 2만개로 줄이기
data = data.head(20000)

#결측치 확인
data['overview'].isnull().sum() #135
data.dropna(subset=['overview'], inplace=True)
data['overview'].isnull().sum() 

data['title'].isnull().sum() #2
data.dropna(subset=['title'], inplace=True)
data['title'].isnull().sum() 
data.reset_index(drop=False, inplace=True)

#overview 데이터 tf-idf 벡터화
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
tfidf_matrix.shape #(19863, 47487)

#overview끼리 코사인 유사도 구하기
from sklearn.metrics.pairwise import linear_kernel
cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cos_sim.shape
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
indices.head()

idx = indices['Toy Story']
idx

#코사인 유사도를 이용해서 overview가장 비슷한 10개의 영화를 찾는 함수
#만들기

def get_recommendations(title, cos_sim=cos_sim) :
    #해당 영화 인덱스 번호 얻기
    idx = indices[title]

    #해당 영화와 모든 영화와 유사도 구하기
    sim_scores = list(enumerate(cos_sim[idx]))

    #유사도에 따라 영화 정렬
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)

    #가장 유사한 영화 10개 가져오기
    sim_scores = sim_scores[1:11]

    #가장 유사한 10개 영화 인덱스 가져오기
    movie_indices = [x[0] for x in sim_scores]

    #가장 유사한 10개의 영화 제목 리턴
    return data['title'].iloc[movie_indices]

get_recommendations('Toy Story')
get_recommendations('The Dark Knight Rises')



