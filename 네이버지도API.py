from WebUtil import WebUtil 
import urllib.request
import json
import datetime
import pandas as pd
import dload
import os
import re
webutil = WebUtil()

print("------------네이버 지도 정보를 검색합니다.------------")
srcTxt = input("검색어를 입력하세요")

mapList = []

jsonResponse = webutil.getNaverMapSearch(srcTxt,1,5)




for item in jsonResponse['items'] :
        
    newsDic = {}
        
    newsDic["title"]=item['title']
    newsDic["category"]=item['category']
    newsDic["desc"]=item['description']
    newsDic["phone"]=item['telephone']
    newsDic["address"]=item['address']
    newsDic["raddress"]=item['roadAddress']
    newsDic["mapx"]=item['mapx']
    newsDic["mapy"]=item['mapy']
    newsDic["link"]=item['link']
    mapList.append(newsDic)

print(mapList)

mapDt = pd.DataFrame(mapList, columns= mapList[0].keys())
mapDt.to_csv(f'./웹크롤링/api활용/네이버 지도 {srcTxt}.csv',encoding = 'utf-8',mode='w',index=False)

with open(f'./웹크롤링/api활용/네이버 지도 {len(mapList)}.json','w', encoding='utf-8') as f:
    retJson = json.dumps(mapList, indent =4 , sort_keys = False, ensure_ascii=False)
    f.write(retJson)

