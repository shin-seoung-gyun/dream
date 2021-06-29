import pandas as pd
#1)데이터 불러오기
data = pd.read_csv('./data/survey.csv')
data.head()
data.info()

#2)데이터 탐색 및 전처리
#2-1) 결측치 제거
data.isna().sum()
data.dropna(inplace=True)
data.isna().sum()

#2-2)한글 이외의 문자는 제거
data['comment']=data['comment'].str.replace('[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ ]+'," ")
data.head()

#2-3) 문장별 글자길이 탐색
data['length'] = data['comment'].str.len()
data.head()

import matplotlib.pyplot as plt
plt.hist(data['length'])
plt.show()

#2-4) 형태소 분석기 토큰화
from konlpy.tag import Okt
okt = Okt()
text = "형태소분석기로 문장을 분해해보자"
tagging = okt.pos(text)
tagging[0][0]

#토큰(단어)만 가져오기
words = okt.pos(text)
word_arr = []
for tagging in words :
    word_arr.append(tagging[0])
word_arr

#형태소 분석기로 문장에서 동사, 명사만 추출하기
parts = ['Noun', 'Verv']
words = okt.pos(text)
word_arr = []
for tagging in words :
    word = tagging[0]
    part = tagging[1]
    if part in parts :
        word_arr.append(tagging[0])
word_arr

#명사만 추출해서 빈도 얻기
parts = ['Noun']
all_words=[]
for i in range(len(data)) :
    text = data['comment'].iloc[i]
    taggings = okt.pos(text)
    for tagging in taggings:
        word = tagging[0]
        part = tagging[1]
        if part in parts :
            all_words.append(word)
all_words

all_words_df = pd.DataFrame({'words':all_words})
all_words_df['count']=1
all_words_df.head()
all_words_df = all_words_df.groupby('words').sum()
all_words_df.sort_values('count', ascending=False).head()


#불용어 제거
stop_words = ['더','수','걸','좀']

parts = ['Noun']
all_words=[]
for i in range(len(data)) :
    text = data['comment'].iloc[i]
    taggings = okt.pos(text)
    for tagging in taggings:
        word = tagging[0]
        part = tagging[1]
        if word in stop_words:
            continue
        if part in parts :
            all_words.append(word)
all_words

all_words_df = pd.DataFrame({'words':all_words})
all_words_df['count']=1
all_words_df.head()
all_words_df = all_words_df.groupby('words').sum()
all_words_df.sort_values('count', ascending=False).head()


#
stop_words = ['더','수','걸','좀']
satisfaction=[]
parts = ['Noun']
all_words=[]
for i in range(len(data)) :
    text = data['comment'].iloc[i]
    taggings = okt.pos(text)
    for tagging in taggings:
        word = tagging[0]
        part = tagging[1]
        if word in stop_words:
            continue
        if part in parts :
            all_words.append(word)
            satisfaction.append(data['satisfaction'].iloc[i])
all_words
satisfaction

all_words_df = pd.DataFrame({'words':all_words})
all_words_df['count']=1
all_words_df['satisfaction']=satisfaction
all_words_df.head()
words_satisfaction = all_words_df.groupby('words').mean()['satisfaction']
words_satisfaction.head()
word_count = all_words_df.groupby('words').count()['count']
word_count.head()

words_df = pd.concat([words_satisfaction, word_count], axis=1)
words_df

#자주나오는 단어들의 고객 만족도
words_df = words_df.loc[words_df['count']>=3]
words_df.sort_values('satisfaction', ascending=False).head(20)
words_df.sort_values('satisfaction', ascending=True).head(20)

#비슷한 문장을 찾기
#방법 : 코사인 유사도
#문장을 벡터화하고, 두 벡터간의 방향이 같은지 비교
from numpy import dot
from numpy.linalg import norm
import numpy as np

#ex) 두 벡터간의 내적과 크기, 코사인값
a =(2,0)
b = (0,1)
#벡터의 크기
norm(a), norm(b)
dot(a,b)

#cos() = dot(a,b)/(|a|*|b|)

def cos_sim(a,b) :
    return dot(a,b)/(norm(a)*norm(b))

cos_sim(a,b)
cos_sim(a,a)
cos_sim(b,b)
a=(1,0)
b=(2,0.1)
cos_sim(a,b)
for i in range(10):
    a = (1,0)
    b = (1,i*0.1)
    cos_sim(a,b)

data['comment'].head()
target_text = data['comment'].iloc[2]
target_text

#---------------------------------------------------------------------------------------------------------------------------------------
#comment ->벡터화(문장 벡터화)
data.head()
parts = ['Noun']
all_words_df = pd.DataFrame()
satisfaction = []
for i in range(len(data)):
    text = data['comment'].iloc[i]
    taggings = okt.pos(text)
    words_df = pd.DataFrame()
    for tag in taggings :
        word = tag[0]
        part = tag[1]
        if part in parts :
            words_df[word] = [1]
    all_words_df = pd.concat([all_words_df, words_df],ignore_index=True)
all_words_df

#null값 0으로 치환
all_words_df.fillna(0, inplace=True)
all_words_df.head()

target_vect = all_words_df.iloc[83]
cos_sim_list=[]
for i in range(len(all_words_df)) :
    temp_vec = all_words_df.iloc[i]
    cos = cos_sim(target_vect, temp_vec)
    cos_sim_list.append(cos)
cos_sim_list

all_words_df['cos_sim']=cos_sim_list
all_words_df.sort_values('cos_sim',ascending=False).head()

data['comment'].iloc[83]
data['comment'].iloc[38]
data['comment'].iloc[46]
data['comment'].iloc[4]



