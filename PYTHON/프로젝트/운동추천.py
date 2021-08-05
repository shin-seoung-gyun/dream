import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import json
#1.데이터 불러오기
data = pd.read_csv('./data/운동방법 ver2.1.csv')
data.head()
data.info()


#한글 이외의 데이터 삭제
data['개요']=data['개요'].str.replace("[^가-힣]+", " ")
data['개요'].head()

#문장 토큰화
from konlpy.tag import Okt
okt = Okt()
data['개요'] = data['개요'].apply(lambda x:okt.morphs(x, stem=True))
data['개요'].head()

#불용어 제거
stopwords = ['장점','높다','범용','발달','키우다','사이즈','잡히다','아령','덤벨','바벨','으로','조금','보다','좋다','두다','에서도','있다','힘주다','나오다','오다','유리하다','성의','라면','쓰이다','이다','운동','의','않기','거의','쪽','합니다','와','을','저','먼저','또는','하다','에서와','린','취하','를','는','있','하','것','들','그','되','수','사람','등','때','년','한','지','그렇','때문','그것','다','을','은','로','정','고','에','지']
data['개요'] = data['개요'].apply(lambda x:[word for word in x if word not in stopwords])
data['개요'].head(10)

#다시 단어 합치기
data['개요_join'] = data['개요'].apply(lambda x:" ".join(x))
data['개요_join'].head()


#overview 데이터 tf-idf기반 벡터화
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['개요_join'])
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
get_recommendation('푸쉬업')

namelist = {}
for name in get_recommendation('푸쉬업'):
    addname = {"name":name}
    namelist['name']=addname
print(namelist)


print(json.dumps(namelist,ensure_ascii=False))



get_recommendation('풀오버')

data['개요_join'].loc[titleIndex['풀오버']]
# '아령 덤벨 들다 팔 굽히다 주 타격 부위 두 근 며 보조 삼각근 전면 과 전완 근 바벨 컬 사이즈 키우다 더 덤벨 컬 양쪽 두 근 균형 잡히다 발달
#  과 높다 범용 장점'

data['개요_join'].loc[titleIndex['푸쉬업']]
# '차렷 자세 에서 양 발 어깨 너비 벌린다 양 손 깍지 끼다 앞 으로 나란 이를 양 발 끝 바깥쪽 으로 도 도 정도 벌리다 주다 상체 그대로 꼿꼿이 유지 천천히 엉덩이 뒤 빼다 와 동시
#  천천히 무릎 굽히다 의자 앉다 앉다 옆 에서 보다 허벅지 가 바닥 과 평행 되다 정도 까지 앉다 엉덩이 뒤 빼다 앉다 무릎 발끝 넘어가다 건 괜찮다 그리고 다시 준비 자세 돌아오다
#  호흡 편하다 숨 쉬다 괜찮다 내려가다 말다 올라오다 뱉다 좋다'

cos_matrix[titleIndex['덤벨 컬']][titleIndex['버터플라이']]
cos_matrix[titleIndex['스쿼트']][titleIndex['레그 컬']]

