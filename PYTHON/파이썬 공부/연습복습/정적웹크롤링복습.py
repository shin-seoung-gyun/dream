import urllib.request #url을 통해서 웹정보를 가져올수있는 모듈(rest api)
import datetime #시간 정보 가져오는 모듈
import json #제이슨 포멧 모듈

##url정보로 웹페이지 정보 가져오는 함수만들기

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        reponse = urllib.request.urlopen(url)
        if reponse.getcode()==200:#정상응답
            print(f"[{datetime.datetime.now()}] \
                Url Request Success")
            return reponse.read().decode('utf-8')
    except Exception as e :
        print(e)
        print(f"[{datetime.datetime.now()}] \
                Error for Url")

print("네이버 연관검색어")
searchText = input("검색어 입력>")

serviceUrl = "https://ac.search.naver.com/nx/ac?"
param = "q="+ urllib.parse.quote(searchText)
param += "&r_format=json&r_enc=UTF-8&st=100"

url = serviceUrl+param

html = getRequestUrl(url)
jsonResult = json.loads(html)
# print(jsonResult)
print(jsonResult['query'][0])
print(jsonResult['items'][0][1][0])

for item in jsonResult['items'][0]:
    print(item[0])

