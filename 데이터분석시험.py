from WebUtil import WebUtil
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

dataList=[]
maxPage = 30
for i in range(1,maxPage+1):
    seviceUrl = 'https://movie.naver.com/movie/point/af/list.nhn?'
    param = '&page='+str(i)
    url = seviceUrl+param
    html = WebUtil.getRequestUrl(url,'cp949')
    soup = BeautifulSoup(html,'html.parser')

    tdTitles = soup.find_all('td',attrs={'class':'title'})

    
    for tdTitle in tdTitles:
        dataDic={}
        dataDic['title']=[]
        dataDic['review']=[]
        dataDic['rank']=[]
        dataDic['mind']=[]
        title = tdTitle.find('a',attrs={'class':'movie color_b'})
        title = title.text
        dataDic['title']=[title]
        review1 = tdTitle.find('a',attrs={'class':'report'})
        review2 = review1['onclick']
        review = re.sub(r'[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+'," ",review2)
        dataDic['review']=[review]
        rank = tdTitle.find('em')
        dataDic['rank']=[rank.text]
        if 8<=int(rank.text)<=10 :
            mind = '긍정'
        elif 0<=int(rank.text)<=3:
            mind = '부정'
        else :
            mind = ''
        dataDic['mind']=[mind]
        dataList.append(dataDic)
print(dataList)

with open('./웹크롤링/정적웹크롤링/시험파일.json','w',encoding='utf-8')as f:
    retJson = json.dumps(dataList, indent =4 , sort_keys = True, ensure_ascii=False)
    f.write(retJson)














