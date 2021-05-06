from WebUtil import WebUtil 
import urllib.request
import json
import datetime
import pandas as pd
import dload
import os
import re
webutil = WebUtil()

print("------------네이버 이미지 정보를 검색합니다.------------")
srcTxt = input("검색어를 입력하세요")

imgList = []

jsonResponse = webutil.getNaverImageSearch(srcTxt,1,100,'large')

idx = 0

while(jsonResponse != None) and jsonResponse['display'] != 0 :
    for item in jsonResponse['items'] :
        idx += 1
        newsDic = {}
        newsDic["idx"]=idx
        newsDic["title"]=item['title']
        newsDic["link"]=item['link']
        
        imgList.append(newsDic)

    start = jsonResponse['start']+jsonResponse['display']
    jsonResponse = webutil.getNaverImageSearch(srcTxt, start, 100,'large')
print(f"가져온 결과 건수 {idx}")
print(imgList)

imgDt = pd.DataFrame(imgList, columns= imgList[0].keys())
imgDt.to_csv(f'./웹크롤링/api활용/네이버 이미지 {srcTxt}-{idx}건.csv',encoding = 'utf-8',mode='w',index=False)

with open(f'./웹크롤링/api활용/네이버 이미지 {len(imgList)}.json','w', encoding='utf-8') as f:
    retJson = json.dumps(imgList, indent =4 , sort_keys = False, ensure_ascii=False)
    f.write(retJson)

path = './image'
if not os.path.exists(path):
    os.mkdir(path)

path = path +f"/{srcTxt}"
if not os.path.exists(path):
    os.mkdir(path)


for image in imgList :
    idx = image['idx']
    title = image['title']
    link = image['link']
    
    mList = re.findall(r'[\w가-힣 ]+',title)
    fileName = str(idx)+'_'+''.join(mList).strip()


    m = re.search(r'\.([\w+?])$',link)
    if m :##삼항연산자로 바꿀수 있음
        fileType = m.group(1)
    else :
        fileType = 'jpg'
    dload.save(link, f"./image/{srcTxt}/{fileName}.{fileType}")

    # urllib.request.urlretrieve(link, './image/%d.jpg' % (idx)) 성능이 좋지 않음.확장자가 다르면 받아오지 못함.

    print(f"{fileName}.{fileType} 다운로드완료")



##파일 읽기
# imgDt = pd.read_csv("./웹크롤링/API활용/네이버 이미지 고양이-1000건.csv")
# print(imgDt)

# with open(f'./웹크롤링/API활용/네이버 이미지 고양이-1000건.json','r', encoding='utf-8') as f :
#     retJson = json.load(f)
# print(retJson)


