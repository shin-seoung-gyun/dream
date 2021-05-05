##네이버 웹툰 인기급상승 텝의 인기순위 10개 가져오기
from WebUtil import WebUtil
from bs4 import BeautifulSoup
import pandas
#select 문으로 가져오기
url = "https://comic.naver.com/index.nhn"
html = WebUtil.getRequestUrl(url)

data = BeautifulSoup(html,'html.parser')
rank = data.select("#realTimeRankFavorite > li > a")

strList = []
for i in rank:
    string = ''
    List = []
    List += i.text
    string = ''.join(List)
    strList.append(string)
    
print(strList)








































