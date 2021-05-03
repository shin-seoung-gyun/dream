import urllib.request #url을 통해서 웹 정보를 가져올수있는 모듈(REST API)
import datetime
import json


class WebUtil :
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