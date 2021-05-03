from WebUtil import WebUtil
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
html = WebUtil.getRequestUrl(url)
soup = BeautifulSoup(html,'html.parser')

atags = soup.select('ol#realTimeRankFavorite>li>a')##ol.asideBoxRank 는 클래스    ol#realTimeRankFavorite는 id
itemList=[]
for tag in atags :
    itemList.append(str(tag.text).replace('\n','').replace('\t',''))
print(itemList)



atags = soup.select('h4.tue>')##집가서 하기
itemList=[]
for tag in atags :
    itemList.append(str(tag.text).replace('\n','').replace('\t',''))
print(itemList)




