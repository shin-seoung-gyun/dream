import urllib.request
import json
import datetime

class WebUtil:
    def getRequestUrl(url,decoding = 'utf-8'):
        req = urllib.request.Request(url)
        try :
            reponse = urllib.request.urlopen(url)
            if reponse.getcode()==200:
                print(f"[{datetime.datetime.now()}] Url Request Success")
                return reponse.read().decode(decoding)
        except Exception as e:
            print(e)
            print(f"[{datetime.datetime.now()}] Error for Url")
