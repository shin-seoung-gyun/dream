from WebUtil import WebUtil
from bs4 import BeautifulSoup
import pandas as pd
import json

maxPage = 10
newsList=[]
for i in range(1,maxPage+1):

    url = 'https://www.hankyung.com/all-news/it?page='+str(i)
    html = WebUtil.getRequestUrl(url)

    soup = BeautifulSoup(html,'html.parser')

    divTags = soup.find('div', attrs={'class':'daily_article'})
    divTags2 = divTags.find_all('div', attrs={'class':'day_article'})

    newsDic = {}
   
    for divTag2 in divTags2:
        ulTags = divTag2.find_all('ul',attrs={'class':'article_list'})
        for ulTag in ulTags:
            liTags = ulTag.find_all('li')
            for  liTag in ulTags :
                for i,liTag in enumerate(liTags):
                    newsDic[i]=[]
                    title = liTag.find('h3')
                    a1 = title.text
                    desc = liTag.find('p',attrs={'class':'read'})
                    b1 = desc.text
                    url = liTag.find('a')['href']##태그 내의 속성값 가져오는법
                    c1 = url
                    newsDic[i]=[a1,b1,c1]
                    newsList.append(newsDic[i])

print("뉴스개수 : " + str(len(newsList)))   

with open(f'한국경제 IT뉴스 {len(newsList)}.json','w', encoding='utf-8') as f:
    retJson = json.dumps(newsList, indent =4 , sort_keys = True, ensure_ascii=False)
    f.write(retJson)



