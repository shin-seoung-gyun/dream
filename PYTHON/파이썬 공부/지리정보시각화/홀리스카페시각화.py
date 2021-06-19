from typing import NoReturn

from folium.map import Icon
from WebUtil import WebUtil
import urllib.request
import json
import pandas as pd
import folium

# def getPosFromAddress(addr) :
#     address = addr
#     serviceKey = "755DF465-6AEF-3F75-AC47-F1E5E045236A"
#     serviceUrl = "http://api.vworld.kr/req/address?"
#     param = "service=address&request=getcoord&version=2.0&crs=epsg:4326"
#     param += "&address=" + urllib.parse.quote(address)
#     param += "&refine=true&simple=false&format=json&type=road"
#     param += "&key=" + serviceKey
#     url = serviceUrl + param
#     result = WebUtil.getRequestUrl(url)

#     if result != None :
#         retJson = json.loads(result)
#     else :
#         retJson = None
#     return retJson


# hollys = pd.read_csv("./지리정보시각화/홀리스카페매장.csv")
# hollys['위도'] = 0
# hollys['경도'] = 0
# print(hollys.head())

# for i,store in hollys.iterrows() :
#     try :
#         retJson = getPosFromAddress(store['address'])
#         xPos = retJson['response']['result']['point']['x']
#         yPos = retJson['response']['result']['point']['y']
#         print(xPos, yPos)
#         hollys.loc[i, '위도'] = yPos
#         hollys.loc[i, '경도'] = xPos
#     except :
#         continue

# hollys.to_csv("./지리정보시각화/hollys위도경도.csv",\
#      encoding='utf-8', mode='w')

from folium.plugins import MarkerCluster


hollys2 = pd.read_csv("./지리정보시각화/hollys위도경도.csv")
m = folium.Map(location=[37.55998,126.97537], zoom_start=15)
m_cluster = MarkerCluster().add_to(m)

for i, store in hollys2.iterrows() :
    if store['위도'] == 0 :
        continue
    folium.Marker(
        location=[store['위도'], store['경도']],
        popup=store['name'],
        icon=folium.Icon(color='red', icon='star')
    ).add_to(m_cluster)
m.save("./지리정보시각화/hollys_map.html")

    

