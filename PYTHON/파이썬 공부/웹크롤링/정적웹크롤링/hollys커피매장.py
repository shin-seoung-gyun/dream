from WebUtil import WebUtil
from bs4 import BeautifulSoup

storeList = []
maxPage = 3
import csv
import pandas as pd

for i in range(1,maxPage+1):
    serviceUrl ="https://www.hollys.co.kr/store/korea/korStore2.do?"
    param ='pageNo=' + str(i)
    url = serviceUrl+param

    html = WebUtil.getRequestUrl(url)
    soup = BeautifulSoup(html,'html.parser')
    tagTbody = soup.find('tbody')
    tagTr = tagTbody.find_all('tr')

    for tag in tagTr:
        tagTd = tag.find_all('td')
        storeDic = {}
        storeDic['region']=tagTd[0].text#지역정보
        storeDic['name']=tagTd[1].text#매장이름
        storeDic['address']=tagTd[3].text#주소
        storeDic['phone']=tagTd[5].text#전화번호
        storeList.append(storeDic)

print("매장개수 : ",len(storeList))        
# for store in storeList:
#     print(store['address'])

# with open('./웹크롤링/정적웹크롤링/할리스매장.csv','w',encoding='utf8') as f:
#     writer = csv.writer(f)
#     writer.writerow(storeList[0].keys())
#     for store in storeList :
#         writer.writerow(store.values())


storeDF = pd.DataFrame(storeList, columns=storeList[0].keys())
storeDF.to_csv("./웹크롤링/정적웹크롤링/홀리스카페매장.csv",encoding='utf8',mode='w',index=True)


