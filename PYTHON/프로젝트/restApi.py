 
#라우팅
from 운동추천 import get_recommendation
from flask import Flask
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask (__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/exercise/<exName>') # URL뒤에 <>을 이용해 가변 경로를 적는다
def hello_user2(exName):

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
        print(sim_score)
        print(exercise_index)
        return data['운동명'].iloc[exercise_index]

    namelist = []
    for name in get_recommendation(exName):
        addname = {"name":name}
        namelist.append(addname)
    print(namelist)
    print(json.dumps(namelist,ensure_ascii=False))
    return json.dumps(namelist,ensure_ascii=False)



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8082) # host주소와 port number 선언