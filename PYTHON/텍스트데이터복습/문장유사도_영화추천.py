import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#1.데이터 불러오기
data = pd.read_csv('./data/movies_metadata.csv')
data.head()
data.info()

#데이터 개수 2만개로 줄이기d
data = data.head(20000)

#결측치 확인
data['overview'].isnull().sum()#135
data.dropna(subset=['overview'], inplace=True)
data['title'].isnull().sum()
data.dropna(subset=['title'], inplace=True)
data.reset_index(drop=False, inplace=True)

#영화 줄거리 기반해서, 줄거리가 비숫한 영화 추천
#overview 데이터 tf-idf기반 벡터화
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
tfidf_matrix.shape

tfidf.vocabulary_.items()
tfidf_matrix.toarray()[0]


#줄거리 끼리 코사인 유사도 모두 구하기
from sklearn.metrics.pairwise import cosine_similarity
cos_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
cos_matrix.shape#(19863, 19863)
cos_matrix[0]#0번째 영화와 나머지 모든 영화 줄거리의 코사인 값
cos_matrix[1]#1번째 영화와 나머지 모든 영화 줄거리의 코사인 값

titleIndex = pd.Series(data.index, index=data['title'])
titleIndex.head()
titleIndex['Waiting to Exhale']

#코사인 값이 가장큰 영화 10개 찾기(코사인 값을 내림 차순 정렬해서 앞 10개)
def get_recommendation(title, cosMatix=cos_matrix):
    #검색한 영화의 인덱스 얻기
    idx = titleIndex[title]
    #해당 영화와 모든 영화의 코사인 값과 인덱스 값얻기
    sim_score = list(enumerate(cosMatix[idx]))
    #코사인 값에 따라 영화 정렬
    sim_score = sorted(sim_score, key=lambda x:x[1], reverse=True)
    #가장 유사한 영화 10개
    sim_score = sim_score[1:11]#자기 자신 제외
    #유사한 영화 인덱스 얻기
    movie_index = [x[0] for x in sim_score]
    #유사한 영화제목 리턴
    return data['title'].iloc[movie_index]
get_recommendation('Toy Story')
get_recommendation('The Dark Knight')











