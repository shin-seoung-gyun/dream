#감성 분석 수행

# 파일 불러오기
import pickle
import pandas as pd
import re
import json
from konlpy.tag import Okt
okt = Okt()
def okt_tokenizer(text) :
    tokens = okt.morphs(text)
    return tokens



with open('./머신러닝/lr_best.pickle','rb')as f :
    lr_best = pickle.load(f)
with open('./머신러닝/tfidf.pickle','rb')as f :
    tfidf = pickle.load(f)

with open('./머신러닝/네이버 뉴스 삼성전자-1000건.json','r',encoding='utf-8') as f:
    data = json.load(f)

title_list = []
desc_list = []
for item in data :
    title_list.append(item['title'])
    desc_list.append(item['desc'])

print(title_list)
print(desc_list)

data_df = pd.DataFrame({"title": title_list,"desc":desc_list})

#(2) 데이터 전처리
data_df['title']=data_df['title'].apply(lambda x:re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ",x))
data_df['desc']=data_df['desc'].apply(lambda x:re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ",x))

data_df.head()

#(3) 감성 분석
#(3-1)피처 벡터화
data_title_tfidf = tfidf.transform(data_df['title'])
#(3-2) 최적 파라미터 학습 모델에 적용하여 감성 분석 예측
data_title_predict = lr_best.predict(data_title_tfidf)
#(3-3) 감성분석 결과 데이터 프레임에 저장
data_df['title_label']= data_title_predict

for i in range(20):
    print('title:',data_df['title'][i])
    print("감성결과 : ","긍정" if data_df['title_label'][i]==1 else'부정')


#desc 기준으로 감정분석

data_desc_tfidf = tfidf.transform(data_df['desc'])
#(3-2) 최적 파라미터 학습 모델에 적용하여 감성 분석 예측
data_desc_predict = lr_best.predict(data_desc_tfidf)
#(3-3) 감성분석 결과 데이터 프레임에 저장
data_df['desc_label']= data_desc_predict

for i in range(20):
    print('desc:',data_df['desc'][i])
    print("감성결과 : ","긍정" if data_df['desc_label'][i]==1 else'부정')


data_df.to_csv("./머신러닝/삼성전자_뉴스_감성분석결과.csv",encoding='utf-8')

print(data_df['title_label'].value_counts())
#title = 부정 -794  긍정 -206
  
print(data_df['desc_label'].value_counts())
#desc = 부정 -708  긍정 -292

#4) 결과 저장 - 긍정기사 부정기사 분리
columns_name = ['title', 'title_label', 'desc', 'desc_label']
neg_data_df = pd.DataFrame(columns = columns_name)
pos_data_df = pd.DataFrame(columns = columns_name)

for i , data in data_df.iterrows():
    title = data['title']
    desc = data['desc']
    t_label = data['title_label']
    d_label = data['desc_label']

    if d_label ==0: #부정기사일 경우 추출
        neg_data_df = neg_data_df.append(pd.DataFrame([[title,t_label,desc,d_label]],columns=columns_name),ignore_index=True)
    else :
        pos_data_df = pos_data_df.append(pd.DataFrame([[title,t_label,desc,d_label]],columns=columns_name),ignore_index=True)

neg_data_df.to_csv('./머신러닝/삼성전자 부정 뉴스.csv',encoding='utf-8')
pos_data_df.to_csv('./머신러닝/삼성전자 긍정 뉴스.csv',encoding='utf-8')
print("긍정기사 : ",len(pos_data_df))
print("부정기사 : ",len(neg_data_df))

# 감성 분석 결과 시각화 : 바 차트
#1) 명사만 추출하여 정리
#- 긍정 감성의 데이터에서 명사 추출

pos_desc = pos_data_df['desc']
pos_desc_noun_list = []
for text in pos_desc :
    pos_desc_noun_list += okt.nouns(text)

print(pos_desc_noun_list)

#글자 길이가 1인 명사만 추리기
pos_desc_noun_list = [noun for noun in pos_desc_noun_list if len(noun)>1]

from collections import Counter
posNCount = Counter(pos_desc_noun_list)
del posNCount['삼성']
del posNCount['전자']
print(posNCount)




#상위30개
top30List = posNCount.most_common(30)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

font_path = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc("font", family=font_name)
#히스토그램 그래프
plt.figure(figsize=(12,5))
plt.xlabel("키워드")
plt.ylabel("빈도수")
plt.grid(True)
plt.bar(range(len(top30List)),[v[1] for v in top30List], align= 'center')
plt.xticks(range(len(top30List)),[v[0] for v in top30List], rotation='75')
plt.show()

##워드클라우드로 시각화
wc = WordCloud(font_path, background_color='ivory',width=800,height=600)
cloud = wc.generate_from_frequencies(posNCount)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis("off")
plt.show()

##부정감성의 데이터로 시각화 하기################################
#1) 명사만 추출하여 정리
#- 긍정 감성의 데이터에서 명사 추출

neg_desc = neg_data_df['desc']
neg_desc_noun_list = []
for text in neg_desc :
    neg_desc_noun_list += okt.nouns(text)

print(neg_desc_noun_list)

#글자 길이가 1인 명사만 추리기
neg_desc_noun_list = [noun for noun in neg_desc_noun_list if len(noun)>1]

from collections import Counter
negNCount = Counter(neg_desc_noun_list)
del negNCount['삼성']
del negNCount['전자']
print(negNCount)




#상위30개
top30List2 = negNCount.most_common(30)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

font_path = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc("font", family=font_name)
#히스토그램 그래프
plt.figure(figsize=(12,5))
plt.xlabel("키워드")
plt.ylabel("빈도수")
plt.grid(True)
plt.bar(range(len(top30List2)),[v[1] for v in top30List2], align= 'center')
plt.xticks(range(len(top30List2)),[v[0] for v in top30List2], rotation='75')
plt.show()

##워드클라우드로 시각화
wc = WordCloud(font_path, background_color='ivory',width=800,height=600)
cloud = wc.generate_from_frequencies(negNCount)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis("off")
plt.show()





