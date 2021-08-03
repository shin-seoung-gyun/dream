import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#1.데이터 불러오기
data = pd.read_csv('./data/운동방법.csv')
data.head()
data.info()


#한글 이외의 데이터 삭제
data['운동방법']=data['운동방법'].str.replace("[^가-힣]+", " ")
data['운동방법'].head()

#문장 토큰화
from konlpy.tag import Okt
okt = Okt()
data['운동방법'] = data['운동방법'].apply(lambda x:okt.morphs(x, stem=True))
data['운동방법'].head()

#불용어 제거
stopwords = ['이','저','먼저','또는','하다','에서와','린','취하','를','는','있','하','것','들','그','되','수','사람','등','때','년','한','지','그렇','때문','그것','다','을','은','로','정','고','에','지']
data['운동방법'] = data['운동방법'].apply(lambda x:[word for word in x if word not in stopwords])
data['운동방법'].head(10)

#다시 단어 합치기
data['운동방법_join'] = data['운동방법'].apply(lambda x:" ".join(x))
data['운동방법_join'].head()


#overview 데이터 tf-idf기반 벡터화
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['운동방법_join'])
tfidf_matrix.shape

tfidf.vocabulary_.items()
tfidf_matrix.toarray()[0]


#운동방법 끼리 코사인 유사도 모두 구하기
from sklearn.metrics.pairwise import cosine_similarity
cos_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
cos_matrix.shape#(19863, 19863)
cos_matrix[0]#0번째 운동방법과 나머지 모든 운동방법의 코사인 값
cos_matrix[1]#1번째 운동방법과 나머지 모든 운동방법의 코사인 값

titleIndex = pd.Series(data.index, index=data['운동명'])
titleIndex.head()
# titleIndex['Waiting to Exhale']

#코사인 값이 가장큰 운동 3개 찾기(코사인 값을 내림 차순 정렬해서 앞 10개)
def get_recommendation(운동명, cosMatix=cos_matrix):
    #검색한 운동의 인덱스 얻기
    idx = titleIndex[운동명]
    #해당 운동과 모든 운동의 코사인 값과 인덱스 값얻기
    sim_score = list(enumerate(cosMatix[idx]))
    #코사인 값에 따라 운동 정렬
    sim_score = sorted(sim_score, key=lambda x:x[1], reverse=True)
    #가장 유사한 운동 3개
    sim_score = sim_score[1:4]#자기 자신 제외
    #유사한 운동 인덱스 얻기
    exercise_index = [x[0] for x in sim_score]
    #유사한 운동명 리턴
    return data['운동명'].iloc[exercise_index]
get_recommendation('덤벨 컬')
get_recommendation('스쿼트')

data['운동방법_join'].loc[titleIndex['덤벨 컬']]
# '긴장 풀 덤벨 듭니 어깨 내리다 팔꿈치 몸통 옆구리 밀착 듯이 붙이다 줍다 사실 몸통 너무 붙이다 도 좋다 않다 어찌 되어다 팔꿈치 쓰다 않다 최대한 두 근 만 쓰기 위 덤벨 들다 
# 올리다 옆구리 팔꿈치 붙이다 고립 좋다 두근 으로만 들어오다 린다 생각 천천히 덤벨 들다 올리다 덤벨 들다 올리다 에는 손목 도 신경 써주다 좋다 대다수 가 무겁다 무게 의 덤벨 
# 선택 운동 손목 꺾다 올리다 가능성 크다 고로 제발 덤벨 컬 에는 중량 칠 생각 말다 중량 반복 이두 가 자라다 희망이 현저 히 낮다 싶다 해도 되다 무조건 처음 엔 중량 반복 효과 
# 적 이다 들다 올리다 동작 에서 도 이상 으로 올리다 에는 손 안쪽 으로 비 틀다 두근 힘 주다 아주 쥐다 짜다 느낌 으로 들어오다 리 면 운동 효과 가 더 좋다 왠만하다 처음 부터  
# 도 이상 으로 들다 올리다 비추다'

data['운동방법_join'].loc[titleIndex['스쿼트']]
# '차렷 자세 에서 양 발 어깨 너비 벌린다 양 손 깍지 끼다 앞 으로 나란 이를 양 발 끝 바깥쪽 으로 도 도 정도 벌리다 주다 상체 그대로 꼿꼿이 유지 천천히 엉덩이 뒤 빼다 와 동시
#  천천히 무릎 굽히다 의자 앉다 앉다 옆 에서 보다 허벅지 가 바닥 과 평행 되다 정도 까지 앉다 엉덩이 뒤 빼다 앉다 무릎 발끝 넘어가다 건 괜찮다 그리고 다시 준비 자세 돌아오다
#  호흡 편하다 숨 쉬다 괜찮다 내려가다 말다 올라오다 뱉다 좋다'

cos_matrix[titleIndex['덤벨 컬']][titleIndex['사이드 레터럴 레이즈']]
cos_matrix[titleIndex['스쿼트']][titleIndex['리버스 크런치']]

