import glob #여러파일들 다룰때 쓰는 라이브러리
import pandas as pd
import numpy as np
import nltk
from numpy import sort_complex
from nltk.tokenize import word_tokenize#토큰화 작업
from nltk.corpus import stopwords#불용어 정보 제공
from nltk.stem import WordNetLemmatizer #표제어 추출
from collections import Counter #리스트 내 데이터 개수
from wordcloud import STOPWORDS, WordCloud
import re
#2차원 리스트 1차원 리스트로 줄일때
from functools import reduce
from matplotlib import pyplot as plt



# nltk.download('stopwords') #불용어 데이터 다운
# nltk.download('punkt') #토크나이저 처리 다운
# nltk.download('wordnet') #표제어 데이터 다운

#영어 논문 데이터 가져오기
all_files = glob.glob('./텍스트분석/영어논문데이터/myCabinetExcelData*.xls')#*을 붙여서 해당하는 모든 데이터 가져옴
all_file_data =[]
for file in all_files :
    df = pd.read_excel(file)
    all_file_data.append(df)
# print(all_file_data)

#가로축 기준 (인덱스 기준) 데이터 병합
all_file_data_con = pd.concat(all_file_data, axis=0, ignore_index=True)
# print(all_file_data_con)

#데이터 전처리 작업
all_title = all_file_data_con['제목']
# print(all_title)

#(1)불용어 데이터 생성
stopwordsData = set(stopwords.words("english"))
#(2)표제어 추출 하는 객체 생성
lemma = WordNetLemmatizer()
word=[]
for title in all_title :
    #정규식 : 영어가 아닌 글자 공백으로 치환
    enWords = re.sub(r'[^a-zA-Z]', " ", str(title))
    print(enWords)
    #모든 단어를 소문자로 정규화
    enWordsToken = word_tokenize(enWords.lower())
    # print(enWordsToken)
    #불용어 제거
    enWordsStop = [w for w in enWordsToken if w not in stopwordsData]
    #표제어 추출
    enWordsStopLemma = [lemma.lemmatize(w) for w in enWordsStop]
    # word.append(enWordsStopLemma)
    word += enWordsStopLemma

# print(word)
#2차원 리스트 1차원 리스트화
# word2 = list(reduce(lambda x,y:x+y, word))
# print(word2)


# Counter 모듈 단어 빈도 횟수 얻기
countWord = Counter(word)
# print(countWord)
del countWord['big']
del countWord['data']

# 상위 50개 단어 얻기
print(countWord.most_common(50))
countWordDic={}
for word, count in countWord.most_common(50):
    if(len(word)>1):
        countWordDic[word]= count
        print(f"{word}:{count}")

#데이터 탐색 - 히스토그램 그래프

# plt.bar(range(len(countWordDic)),countWordDic.values(),align='center')
# plt.xticks(range(len(countWordDic)),countWordDic.keys(),rotation='85')
# plt.show()


#연도별 학술문서 수 그래프 그리기
# print(sorted(all_file_data_con['출판일'].unique(),reverse=True))
all_file_data_con['doc_count']=0
summary_year = all_file_data_con.groupby('출판일',as_index="False")['doc_count'].count()
# print(summary_year)
# plt.figure(figsize=(12,5))
# plt.xlabel("year")
# plt.ylabel("doc_count")
# plt.grid(True)
# plt.plot(summary_year.index,summary_year.values)
# plt.show()

stopwords = set(STOPWORDS)
wc = WordCloud(background_color='ivory', stopwords= stopwords,width=800,height=600)
cloud = wc.generate_from_frequencies(countWordDic)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()









