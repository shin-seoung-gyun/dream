from WebUtil import WebUtil
from bs4 import BeautifulSoup
import pandas as pd

maxPage = 32
financeList = []
for i in range(1,maxPage+1):
    serviceUrl = "https://finance.naver.com/sise/sise_market_sum.nhn?"
    param = "&page="+ str(i)
    url = serviceUrl+param
    html = WebUtil.getRequestUrl(url,'euc-kr')
    soup = BeautifulSoup(html,'html.parser')

    # tbodyTags = soup.find('tbody')
    # trTags = tbodyTags.find_all('tr')

    # dataDic = {}#11
    # for trTag in trTags:
    #     tdTags = trTag.find_all('td')
    #     for i,tdTag in enumerate(tdTags):
    #         a = str(tdTag.text).replace('\n','').replace('\t','')
    #         if i==3 or i==4 or i ==0 or i==12:
    #             continue
            
    #         dataDic[i]=[]
    #         dataDic[i] += a
        
    # print(dataDic)

    colTags = soup.select("thead>tr>th")
    colList = [colTag.text for  colTag in colTags if not colTag.text in '등락률,전일비,토론실']


    tagTbody = soup.find('tbody')
    tagTrs = tagTbody.find_all('tr',attrs={'onmouseover':'mouseOver(this)'})

    
    for tagTr in tagTrs:
        tagTds = tagTr.find_all("td")
        financeDic = {}
        valueList = []
        for tagTd in tagTds:
            valueList.append(tagTd.text)
        valueList = [val for i, val in enumerate(valueList) if not (i==3 or i==4 or i==12)]
        for col, val in zip(colList,valueList):
            financeDic[col]=val
        financeList.append(financeDic)
            
for val in financeList:
    print(val)

finanDF = pd.DataFrame(financeList, columns=financeList[0].keys())
finanDF.to_csv("./웹크롤링/정적웹크롤링/코스피상장회사.csv",encoding='utf8',mode='w',index=False)

