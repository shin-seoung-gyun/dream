from WebUtil import WebUtil 
import urllib.request
import json
import datetime
import pandas as pd
webutil = WebUtil()

print("------------네이버 뉴스 정보를 검색합니다.------------")
srcTxt = input("검색어를 입력하세요")

newsList = []

jsonResponse = webutil.getNaverSearch(srcTxt,1,100)

idx = 0
while(jsonResponse != None) and jsonResponse['display'] != 0 :
    for item in jsonResponse['items'] :
        idx += 1
        newsDic = {}
        newsDic["idx"]=idx
        newsDic["title"]=item['title']
        newsDic["desc"]=item['description']
        newsDic["line"]=item['link']
        pDate = datetime.datetime.strptime(item["pubDate"],'%a, %d %b %Y %H:%M:%S +0900')
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
        newsDic["date"]=pDate
        newsList.append(newsDic)

    start = jsonResponse['start']+jsonResponse['display']
    jsonResponse = webutil.getNaverSearch(srcTxt, start, 100)
print(f"가져온 결과 건수 {idx}")
print(newsList)

newsDt = pd.DataFrame(newsList, columns= newsList[0].keys())
newsDt.to_csv(f'./웹크롤링/api활용/네이버 뉴스 {srcTxt}-{idx}건.csv',encoding = 'utf-8',mode='w',index=False)

with open(f'./웹크롤링/api활용/네이버 뉴스 {len(newsList)}.json','w', encoding='utf-8') as f:
    retJson = json.dumps(newsList, indent =4 , sort_keys = False, ensure_ascii=False)
    f.write(retJson)
