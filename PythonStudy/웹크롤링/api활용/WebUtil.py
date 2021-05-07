import urllib.request #url을 통해서 웹 정보를 가져올수있는 모듈(REST API)
import datetime
import json


class WebUtil :
    Naver_Client_ID = 'kiVr5Wks0d0L7g1HBWOv'
    Naver_Client_SECRET = 'GTv_PdIAW4'

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

    def getNaverRequestUrl(self,url, decoding='utf-8'):
        header = {'X-Naver-Client-ID':self.Naver_Client_ID,'X-Naver-Client-Secret':self.Naver_Client_SECRET}
        req = urllib.request.Request(url, headers=header)   
        try :
            reponse = urllib.request.urlopen(req)
            if reponse.getcode()==200: #정상응답(http 프로토콜 기준에 나오는 응답)
                print(f"[{datetime.datetime.now()}] Url Request Success")
                return reponse.read().decode(decoding)
        except Exception as e :
            print(e)
            print(f"[{datetime.datetime.now()}] Error for Url")

    def getNaverSearch(self,searchText, start, display):
        serviceUrl = "https://openapi.naver.com/v1/search/news.json"
        param = "?query=" + urllib.parse.quote(searchText)
        param += f"&display={display}&start={start}"
        url = serviceUrl + param

        result = self.getNaverRequestUrl(url)

        if result != None:
            return json.loads(result)
        else :
            return None

    def getNaverImageSearch(self,searchText, start, display,large):
        serviceUrl = "https://openapi.naver.com/v1/search/image"
        param = "?query=" + urllib.parse.quote(searchText)
        param += f"&display={display}&start={start}&filler={large}"
        url = serviceUrl + param

        result = self.getNaverRequestUrl(url)

        if result != None:
            return json.loads(result)
        else :
            return None

    def getNaverMapSearch(self,searchText, start, display):
        serviceUrl = "https://openapi.naver.com/v1/search/local.json"
        param = "?query=" + urllib.parse.quote(searchText)
        param += f"&display={display}&start={start}"
        url = serviceUrl + param

        result = self.getNaverRequestUrl(url)

        if result != None:
            return json.loads(result)
        else :
            return None
    