from WebUtil import WebUtil
from bs4 import BeautifulSoup
import json

url = 'https://www.hankyung.com/all-news/it?page=2'
html = WebUtil.getRequestUrl(url)
soup = BeautifulSoup(html,'html.parser')

divTags = soup.select('div.day_article>ul>li')
newsDic = {}
newsList = []
for divTag in divTags:
    title = divTag.find('h3')
    newsDic['title']=[title.text]
    desc = divTag.find('p',attrs={'class':'read'})
    newsDic['desc']=[desc.text]
    y= divTag.find('h3')
    j = y.find('a')
    link = j['href']
    newsDic['link']=[link]
    newsList.append(newsDic)
print(newsList)













