##2010~2020 수입 지출 데이터 받아오고, 각 년도별로 그래프 만들기

from WebUtil import WebUtil
import json

def getTourismBalcList(startDate):
    serviceKey = 'DH180Mg0%2BO42YEpNqMTGDKyG9oUxJRAphRgPK4EAYqG94t3dLqOUm9JEJh2nSXgN1lKXGyscJNl9cYAxDwPWLw%3D%3D'
    serviceUrl = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getTourismBalcList'
    param = '?_type=json&serviceKey='+serviceKey
    param += '&YM='+startDate
    url = serviceUrl + param
    result = WebUtil.getRequestUrl(url)
    if result == None:
        return None
    else :
        return json.loads(result)


print('<< 관광수지 데이터를 수집합니다. >>')
startYear = int(input('데이터를 몇 년 부터 수집할까요? >'))
endYear = int(input('데이터를 몇 년 까지 수집할까요? >'))

jsonResult = []
for year in range(startYear, endYear+1) :
    for mon in range(1, 13) :
        yyyymm= f"{year}{mon:0>2}"#201704
        jsonData = getTourismBalcList(yyyymm)
        
        if jsonData['response']['header']['resultCode']=="0000":
            item = jsonData['response']['body']['items']
            if item == '':
                break
            else :
                item = item['item']
                natTradeDic = {}
                natTradeDic['날짜']=item['ym']
                natTradeDic['관광수입']=item['tr']
                natTradeDic['관광지출']=item['te']
                jsonResult.append(natTradeDic)
item=jsonResult[-1]
with open(f"./웹크롤링/api활용/관광수지.json",'w',encoding='utf-8') as f:
    retJson = json.dumps(jsonResult, indent=4 , sort_keys=False,ensure_ascii=False)
    f.write(retJson)
print(f"./웹크롤링/api활용/관광수지.json 저장완료")