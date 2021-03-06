#텍스트 분석
#0.데이터 수집->1. 텍스트 전저리 -> 2. 특성벡터화 -> 3. 모델구축/훈련 -> 4. 평가및 결과 분석 -> 5.모델 활용
#
# 0. 데이터 수집
# (1) 웹크롤링, (2)API, (3) 다운로드, (4) 오프라인 수집, (5)DB
# 
# 1.텍스트 전처리
# (1) 토큰화(단어별로 파싱하는 작업) -nltk,konlpy
# (2) 정제 및 정규화(단어길이가 작은 것 제거, 한글이 아닌 특수문자 제거(정규표현식활용),대소문자 통합(영어))
# (3) 불용어 제거
# 영어권 : 라이브러리 제공 
# 한국어 : https://www.ranks.nl/stopwords/korean
# (4)표제어 추출 
# 형태소 분석기 -> 단어 원형
# 영어 : nltk
# 한국어 : konlpy 
# 
# 2. 특성 벡터화
# (1) bow방식 - 카운트 기반 (단어 빈도수, 단어 순서 상관없음)
# TF-IDF 벡터화
#  머신러닝 모델에 많이 사용됨
#
# (2) 워드 임베딩(딥러닝 모델) - http://w.elnn.kr/search/
# 유사한 단어끼리 유사한 가중치를 가질수 있도록 벡터화
# Word2Vec
# 단어-> 정수화(임의의 인덱스, 일반적으로 빈도수 높은 단어가 인덱스가 작다.) -> 워드 임베딩
# 순환신경망 모델(RNN,LSTM) 에 많이 사용됨
# 벡터 크기 지정 (원핫 인코딩 방식보다는 크기가 작다)
# 벡터의 값 실수.
#
# (3) 원핫 인코딩
# 단어 -> 정수화 -> 원핫인코딩
#  단점 - 차원이 너무 커지고, 의미가 없는 0으로 채워진다.
# 잘 사용 안함.
# 
# 3. 모델 구축/ 훈련
# (1)시계열 데이터 (RNN, LSTM) ->감정분석, 스팸메일 분류
# (2)문장간의 유사도를 얻고 싶을때 => 코사인 유사도 = 추천
# (3) 토픽 모델링 -> LSA(잘안쓰임), LDA = 문서요약
# 
# 4. 평가 및 결과 분석
# 시각화 - 워드 클라우드
# 
# 5. 모델 활용
# API 구축, 모델을 저장해서 JAVA에서 불러와 사용 - 라이브러리가 지원 해줘야 함.
#
# 텍스트 분석 고급
# 문서, 문장 번역, 챗봇
#

