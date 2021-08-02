#LDA는 가장 대표적인 토픽 모델링 알고리즘
#LDA(Latent Dirichlet Aloocation) - 잠재 디리클레 할당
#문서들은 토픽들의 혼합으로 구성되어져 있으며, 토픽들은 확률 분포에
#기반하여 단어들을 생성한다고 가정. 
#데이터가 주어지면, LDA는 문서가 생성되던 과정을 역추적한다.

import pandas as pd
import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/franciscadias/data/master/abcnews-date-text.csv", 
                filename='abcNewsData.csv')

#error_bad_lines=False 오류가 발생한 줄을 빼고 처리한다. 
data = pd.read_csv("abcNewsData.csv", error_bad_lines=False)
data.head()
data.info() #1082168

document = data[['headline_text']]
document.head(5)

#2.데이터 전처리
#1) 토큰화
import nltk
#데이터 개수 줄이기
document = document.head(10000)
#nltk.download('punkt')
document['headline_text'] = document['headline_text'].\
    apply(lambda row:nltk.word_tokenize(row))
document['headline_text'].head()

#2)불용어 제거
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
document['headline_text'] = document['headline_text'].\
    apply(lambda x : [word for word in x if word not in stop_words])
document['headline_text'].head()

#3) 표제어 추출
#동사들의 원형, (과거, 과거분사 -> 일반동사)
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
document['headline_text'] = document['headline_text'].\
    apply(lambda x : \
        [WordNetLemmatizer().lemmatize(word, pos='v') for word in x])
document['headline_text'].head()

#4) 길이가 3이하인 단어 제거
document['headline_text'] = document['headline_text'].\
    apply(lambda x : \
        [word for word in x if len(word) > 3])
document['headline_text'].head()

#5) 리스트 문자열합치기
document['headline_text'] = document['headline_text'].\
    apply(lambda x : ' '.join(x))
document['headline_text'].head()

#6) TF-idf 벡터화
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=1000, 
            smooth_idf=True)
X = tfidf.fit_transform(document['headline_text'])
X.shape #(10000, 1000)

#3. 토픽모델링
from sklearn.decomposition import LatentDirichletAllocation
#n_components 토픽수
lda_model = LatentDirichletAllocation(n_components=10, learning_method='online', random_state=77, max_iter=10)
lda_topic = lda_model.fit_transform(X)
lda_topic.shape#(10000, 10) #각 기사별로 10개의 토픽 비중

lda_model.components_
lda_model.components_.shape#(10, 1000) #각 토픽에 따른 단어 비중

terms = tfidf.get_feature_names()#1000개 단어 이름
terms
for idx, topic in enumerate(lda_model.components_):
    sortList = [(terms[i], topic[i].round(5)) for i in topic.argsort()]
    print(f"Topic {idx}:", sortList[:-6:-1])#-1,-2,-3,-4,-5
    
lda_topic[0]
lda_topic[1]















