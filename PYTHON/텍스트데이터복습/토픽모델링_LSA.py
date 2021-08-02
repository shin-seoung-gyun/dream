#LSA(Latent Semantic Analysis) - 잠재의미분석
#토픽 모델링을 위한 최적화 알고리즘은 아님
#이 분야에 아이디어를 제공한 알고리즘.

#선형 대수학의 특이값 분해를 통해서, TF-IDF 행렬의 차원을 축소 시키고
#단어들의 잠재적인 의미를 이끌어 낸다.

from nltk import tokenize
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
dataSet = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers','footers','quotes'))
document = dataSet.data
len(document)

#뉴스 내용 첫번째
document[1]

#뉴스 그룹이름
dataSet.target_names

#2. 데이터 전처리
#2-1) 영어가 아닌 단어 제거
news_df = pd.DataFrame({'document':document})
news_df['clean_doc'] = news_df['document'].str.replace("[^a-zA-Z]+", " ")
news_df['clean_doc'].head()

#2-2) 길이가 3이하인 단어 제거
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: [ w for w in x.split() if len(w)>3 ])
news_df['clean_doc'].head()
#문자열 결합
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: " ".join(x))
news_df['clean_doc'].head()

#2-3) 소문자로 변환
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())
news_df['clean_doc'].head()

#2-4) 불용어 제거
#pip install nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words
#토큰화
tokenize_doc = news_df['clean_doc'].apply(lambda x:x.split())
tokenize_doc.head()
tokenize_doc.apply(lambda x : [ word for word in x if  word not in stop_words])
tokenize_doc.head()

#문자열 결합
tokenize_doc = tokenize_doc.apply(lambda x: " ".join(x))
tokenize_doc.head()

#2-5) tf-idf 벡터화
news_df['clean_doc'] = tokenize_doc
news_df['clean_doc'].head()

#상위 1000개의 단어
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=1000, 
                        max_df=0.5, smooth_idf=True)
X = tfidf.fit_transform(news_df['clean_doc'])
news_df['clean_doc'].shape#(11314,)
X.shape #(11314, 1000)

#3. 모델생성 (토픽 모델링)
from sklearn.decomposition import TruncatedSVD
#n_components 토픽의 개수 (하이퍼 파라미터)
svd_model = TruncatedSVD(n_components=20, n_iter=100, random_state=33)
svd_model.fit(X)
svd_model.components_
len(svd_model.components_)

import numpy as np
np.shape(svd_model.components_)#(20, 1000)
#토픽 개수 *단어의 수

terms = tfidf.get_feature_names()
terms
svd_model.components_#각 토픽마다 1000개의 단어들의 가중치가 있다.
#각 토픽에 기여하는 상위 5개의 단어들 만 표시

for idx, topic in enumerate(svd_model.components_):
    sortList = [(terms[i], topic[i].round(5)) for i in topic.argsort()]
    print(f"Topic {idx}:", sortList[:-6:-1])#-1,-2,-3,-4,-5
dataSet.target_names

#기사마다 토픽 기여도 확인
doc_idx = 10
news_df['clean_doc'].head()
news_df['clean_doc'].iloc[0]

from sklearn.metrics.pairwise import cosine_similarity
cos_matrix = cosine_similarity(X, svd_model.components_)
X.shape#(11314, 1000)
np.shape(svd_model.components_)#(20, 1000)

sim_score = list(enumerate(cos_matrix[doc_idx]))
sim_score #doc_idx의 문서의 각 토픽마다의 유사도
sim_score = sorted(sim_score, key=lambda x:x[1], reverse=True)
sim_score

#LSA 모델의 장단점
#LSA모델은 쉽고 빠르게 구현하고 단어의 잠재적인 의미를 이끌어 내서
#좋은 성능을 보여주는 장점을 갖는다.
#단점으로는 새로운 데이터가 추가되면 처음부터 다시 계산해야함.


