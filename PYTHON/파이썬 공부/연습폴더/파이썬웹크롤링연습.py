from WebUtil import WebUtil
from bs4 import BeautifulSoup
##요일별 웹툰 가져오기 (find 사용)
url = "https://comic.naver.com/webtoon/weekday.nhn"
html = WebUtil.getRequestUrl(url)
soup = BeautifulSoup(html,'html.parser')

allTags = soup.find("div",attrs={'class':'list_area daily_all'})
colTags = allTags.find_all("div",attrs={'class':'col_inner'})

webtoonDic={}
for i, colTag in enumerate(colTags):
    liTags = colTag.find_all('li')
    webtoonDic[i]=[]
    for liTag in liTags:
        adata = liTag.find('a','title')
        name = str(adata.text).replace('\n', '').replace('\t', '')

        webtoonDic[i]+=[name]
print(webtoonDic)   


    
        
        



























