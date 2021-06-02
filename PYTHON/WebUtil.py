import urllib.request #url을 통해서 웹 정보를 가져올수있는 모듈(REST API)
import datetime
import json


class WebUtil :
    def getRequestUrl(url, decoding='utf-8'):
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        req = urllib.request.Request(url, headers=header)   
        try :
            reponse = urllib.request.urlopen(req)
            if reponse.getcode()==200: #정상응답(http 프로토콜 기준에 나오는 응답)
                print(f"[{datetime.datetime.now()}] Url Request Success")
                return reponse.read().decode(decoding)
        except Exception as e :
            print(e)
            print(f"[{datetime.datetime.now()}] Error for Url")


