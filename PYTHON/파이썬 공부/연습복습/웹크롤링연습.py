import json
from WebUtil import WebUtil
from bs4 import BeautifulSoup

##한국경제 뉴스 웹크롤링

url = "https://www.hankyung.com/all-news?page=2"
html = WebUtil.getRequestUrl(url)
soup = BeautifulSoup(html,"html.parser")

liTags = soup.select('div.day_article>ul>li')


newsList = []
for liTag in liTags:
    newsDic = {}
    title = liTag.find('h3').text
    newsDic['title'] = [title]
    desc = liTag.find('p',attrs={'class':'read'}).text
    newsDic['desc'] = [desc]
    k = liTag.find('h3')
    j = k.find('a')
    link = j['href']
    newsDic['link'] = [link]
    newsList.append(newsDic)
print(newsList)   

    
    







