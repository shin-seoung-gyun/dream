##2015~2020 12월 중국

from WebUtil import WebUtil
import json

def getEdrCntTourismStatsList(startDate, nat, ed):
    serviceKey = 'DH180Mg0%2BO42YEpNqMTGDKyG9oUxJRAphRgPK4EAYqG94t3dLqOUm9JEJh2nSXgN1lKXGyscJNl9cYAxDwPWLw%3D%3D'
    serviceUrl = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    param = '?_type=json&serviceKey='+serviceKey
    param += '&YM='+startDate
    param += '&NAT_CD='+ nat
    param += '&ED_CD='+ ed
    url = serviceUrl + param
    result = WebUtil.getRequestUrl(url)
    if result == None:
        return None
    else :
        return json.loads(result)


print('<< 출입국 관광 통계 데이터를 수집합니다. >>')
nat = input('국가 코드를 입력하세요. ex)미국:275,중국:112,일본:130 >')
startYear = int(input('데이터를 몇 년 부터 수집할까요? >'))
endYear = int(input('데이터를 몇 년 까지 수집할까요? >'))
ed = input('출국,출입을 선택하세요 ex) 출국:D 출입:E >')

jsonResult = []
for year in range(startYear, endYear+1) :
    for mon in range(1, 13) :
        yyyymm= f"{year}{mon:0>2}"#201704
        jsonData = getEdrCntTourismStatsList(yyyymm, nat, ed)
        print(jsonData)

        if jsonData['response']['header']['resultCode']=="0000":
            item = jsonData['response']['body']['items']
            if item == '':
                break
            else :
                item = item['item']
                natTradeDic = {}
                natTradeDic['날짜']=item['ym']
                natTradeDic['국가명']=item['natKorNm']
                natTradeDic['방한외래관광객수']=item['num']
                jsonResult.append(natTradeDic)
item=jsonResult[-1]
with open(f"./웹크롤링/api활용/출입국관광통계_{item['국가명']}.json",'w',encoding='utf-8') as f:
    retJson = json.dumps(jsonResult, indent=4 , sort_keys=False,ensure_ascii=False)
    f.write(retJson)
print(f"./웹크롤링/api활용/출입국관광통계_{item['국가명']}.json.json 저장완료")


































