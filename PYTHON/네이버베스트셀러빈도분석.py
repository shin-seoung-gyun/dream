# from konlpy.tag import Okt #Twitter
# okt = Okt()

#형태소 분석
# print(okt.morphs("단독입찰보다 복수입찰의 경우"))

#명사 분석
# print(okt.nouns("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))

#구(Phrase) 분석
# print(okt.phrases("날카로운 분석과 신뢰감 있는 진행으로"))

#형태소 분석 품사태깅
# print(okt.pos("안녕하세요. 홍길동입니다. ㅋㅋㅋㅋㅎㅎ12"))


# from konlpy.tag import Komoran
# komoran = Komoran()
# print(komoran.morphs("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))
# print(komoran.nouns("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))
# print(komoran.pos("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))
# print()
# print(okt.morphs("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))
# print(okt.nouns("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))
# print(okt.pos("유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는"))

from konlpy.tag import Okt
import json
import re
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

#형태소 분석기 객체생성
okt = Okt()
#(1) 데이터 불러오기
data = json.loads(open("./텍스트분석/네이버베스트셀서.json",'r',encoding="utf-8").read())
print(data)

desc = ""
title = ""
for item in data :
    if "desc" in item.keys():
        desc += re.sub(r'[^ㄱ-ㅎ가-힣ㅏ-ㅣ],'," ", item['desc'])
    if "title" in item.keys():
        title += re.sub(r'[^ㄱ-ㅎ가-힣ㅏ-ㅣ],'," ", item['title'])    
news = title + " " + desc
news_noun = okt.nouns(news)
print(news_noun)


#글자 길이가 1인 항목 삭제
for i, noun in enumerate(news_noun):
    if len(noun)<2 :
        del news_noun[i]
#단어수 세기
newsCount = Counter(news_noun)
print(newsCount)
#
#히스토 그램으로 표현
font_path = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc("font",family=font_name)
plt.figure(figsize=(12,5))
plt.xlabel("키워드")
plt.ylabel("빈도수")
plt.grid(True)
print(newsCount.most_common(30))
top30List = newsCount.most_common(30)
plt.bar(range(len(top30List)),[v[1] for v in top30List],align="center")
plt.xticks(range(len(top30List)),[v[0] for v in top30List],rotation="75")
plt.show()

wordDic ={}
for word, cnt in top30List:
    wordDic[word]=cnt

wc = WordCloud(font_path, background_color='ivory',width=800,height=600)
cloud = wc.generate_from_frequencies(newsCount)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis("off")
plt.show()



