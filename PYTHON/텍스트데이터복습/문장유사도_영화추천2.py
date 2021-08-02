import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#1.데이터 불러오기
data = pd.read_csv('./data/movies04293.csv')
data.head()
data.info()



#결측치 확인
# data['title'].isnull().sum()
# data.dropna(subset=['title'], inplace=True)
# data.reset_index(drop=False, inplace=True)

#장르와 줄거리를 결합
data['content'] = data['genre']+" "+data['plot']
data['content'].head()

#한글 이외의 데이터 삭제
data['content']=data['content'].str.replace("[^가-힣]+", " ")
data['content'].head()

#문장 토큰화
from konlpy.tag import Okt
okt = Okt()
data['content'] = data['content'].apply(lambda x:okt.morphs(x, stem=True))
data['content'].head()

#불용어 제거
stopwords = ['인','을','에게','제','의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

data['content'] = data['content'].apply(lambda x:[word for word in x if word not in stopwords])
data['content'].head()

#다시 단어 합치기
data['content_join'] = data['content'].apply(lambda x:" ".join(x))
data['content_join'].head()



#영화 줄거리 기반해서, 줄거리가 비숫한 영화 추천
#overview 데이터 tf-idf기반 벡터화
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['content_join'])
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
# titleIndex['Waiting to Exhale']

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
get_recommendation('라스트 나잇')
get_recommendation('돼지의 왕')

data['content_join'].loc[titleIndex['돼지의 왕']]
# '애니메이션 스릴러 회사 부도 후 충 동 적 아내 살인 경민 목소리 오정세 자신 분노 감추다 중학교 동창 이다 종석 목소리 양익준 찾다 나서다 
# 소설가 되다 못 자서전 대필작가 로 근근히 먹다 살다 종석 년 만에 찾아오다 경민 방문 당황 경민 무시 당 하고 짓 밟다 지우다 싶다 중학교 시 
# 절 자신 우상 이다 철 목소리 김혜나 이야기 종석 꺼내다 그리고 경민 학창시절 교정 종석 이끌다 년 전 그날 충격 적 진실 밝히다

data['content_join'].loc[titleIndex['도어락']]
# '스릴러 오피스텔 혼자 살 고 있다 평범하다 직장인 경민 공효진 퇴근 후 집 돌아오다 경민 원룸 도어 락 덮개 열리다 것 발견 불안하다 마음 도
# 어 락 비밀번호 변경 해보다 그날 밤 잠들다 전 문 밖 에서 들리다 소리 삐 삐 삐 삐 잘못 누르다 공포 감 휩싸이다 경민 경찰 신고 하지만 그 경
# 민 잦다 신고 귀찮다 뿐 대수롭다 않다 여기다 그리고 얼마 뒤 경민 원룸 에서 낯선 사람 침입 흔적 함께 의문 살인 사건 발생 하고 자신 안전하 
# 다 않다

data['content_join'].loc[titleIndex['네모난원']]
# '드라마 때 민주화 요구 들끓다 년대 고지식하다 모범생 경민 순수하다 학구 열 불타 학생운동 중심 선 써클 가입 거기 서 동갑 내기 수정 만난 
# 경민 눈 그녀 반하다 이미 운동권 중심 활약 중인 용호 이론 적 사사건건 부딪치다 열 혈 투사 로 변신 가다 수정과 점점 가까워지다 경민 지켜보
# 다 용호 시선 차갑다 어느 날 교내 사복 경찰 들이다 닥치다 소식 용호 미처 전해 듣다 못 경민 경찰 체포 되어다 강제 입대 되다 제대 후 경민  
# 반기다 것 수정과 용호 애인 사이 돼다 사실 뿐 이후 경민 용호 다른 노선 걷다 되다 주사파 실세 되다 대학가 유명인사 되다 그러나 내부 고발  
# 의하다 다시 체포 되다 경민 결국 교도소 수감 되다 년 초반 돼다 서다 풀다 나다 그 사이 용호 수정 결혼 경민 세상 모든 것 허무 느끼다 그동안
#  이상향 생각 해오다 북한 직접 가다 모든 것 자기 눈 확인 해보다 사실 알 게 되다 용호 수정 역시 경민 따르다 북한 함께 잠입 하고 그 곳 에서
#  용호 북한 기관 에서 일 해보다 않다 제의 받다 당혹하다 경민 수정 결국 경민 만이 남한 내려오다 용호 수정 북 남다 때 부터 엇갈리다 세 사람
#  가혹하다 운명 시작 되다'

cos_matrix[titleIndex['돼지의 왕']][titleIndex['도어락']]
cos_matrix[titleIndex['돼지의 왕']][titleIndex['네모난원']]

