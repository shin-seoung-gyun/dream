import urllib.request #url을 통해서 웹 정보를 가져올수있는 모듈(REST API)
import datetime
import json

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try :
        reponse = urllib.request.urlopen(url)
        if reponse.getcode()==200: #정상응답(http 프로토콜 기준에 나오는 응답)
            print(f"[{datetime.datetime.now()}] Url Request Success")
            return reponse.read().decode('utf-8')
    except Exception as e :
        print(e)
        print(f"[{datetime.datetime.now()}] Error for Url")


print("<<네이버 연관검색어>>")
searchText = input("검색어를 입력하세요> ")

serviceUrl = "https://ac.search.naver.com/nx/ac?"
param = "q="+ urllib.parse.quote(searchText)
param+= "&r_format=json&r_enc=UTF-8&st=100"

url = serviceUrl+param

html = getRequestUrl(url)
jsonResult = json.loads(html)
# print(jsonResult)
print(jsonResult['query'][0])
print(jsonResult['items'][0][1][0])

for item in jsonResult['items'][0]:##복잡하드아
    print(item[0])













