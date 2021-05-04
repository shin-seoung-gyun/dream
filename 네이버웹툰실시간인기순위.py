from WebUtil import WebUtil
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
html = WebUtil.getRequestUrl(url)
soup = BeautifulSoup(html,'html.parser')

# atags = soup.select('ol#realTimeRankFavorite>li>a')##ol.asideBoxRank 는 클래스    ol#realTimeRankFavorite는 id
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)



atags = soup.select('div.list_area.daily_all > div > div > ul > li > a')##전체 만화 이름
itemList=[]
for tag in atags :
    itemList.append(str(tag.text).replace('\n','').replace('\t',''))
print(itemList)

# atags = soup.select('div.list_area.daily_all > div.col.col_selected > div > ul > li > a') 
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

# atags = soup.select('div.list_area.daily_all > div:nth-child(3) > div > ul > li > a')
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

# atags = soup.select('div.list_area.daily_all > div:nth-child(4) > div > ul > li > a')
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

# atags = soup.select('div.list_area.daily_all > div:nth-child(5) > div > ul > li > a')
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

# atags = soup.select('div.list_area.daily_all > div:nth-child(6) > div > ul > li > a')
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

# atags = soup.select('div.list_area.daily_all > div:nth-child(7) > div > ul > li > a')
# itemList=[]
# for tag in atags :
#     itemList.append(str(tag.text).replace('\n','').replace('\t',''))
# print(itemList)

rootTag = soup.find('div', attrs={'class':'list_area daily_all'})
colTags = rootTag.find_all("div",attrs={'class':'col_inner'})

webtoonDic={}
for i, colTag in enumerate(colTags):
    liTags = colTag.find_all("li")
    webtoonDic[i]=[]
    for liTag in liTags:
        webtoonDic[i] += [liTag.find_all('a')[1].text]
for key, val in webtoonDic.items():
    print(key, val)













