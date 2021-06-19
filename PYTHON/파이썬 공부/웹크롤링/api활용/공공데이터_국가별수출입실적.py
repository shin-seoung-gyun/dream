from WebUtil import WebUtil
import json

def getNationTradeList(startDate, nat):
    serviceKey = 'DH180Mg0%2BO42YEpNqMTGDKyG9oUxJRAphRgPK4EAYqG94t3dLqOUm9JEJh2nSXgN1lKXGyscJNl9cYAxDwPWLw%3D%3D'
    serviceUrl = 'http://openapi.customs.go.kr/openapi/service/newTradestatistics/getnationtradeList'
    param = '?_type=json&serviceKey='+serviceKey
    param += '&searchBgnDe='+startDate
    param += '&searchEndDe='+startDate
    param += '&searchStatCd='+nat
    param += '&numOfRows=10'
    param += '&pageNo=1'
    url = serviceUrl + param
    result = WebUtil.getRequestUrl(url)
    if result == None:
        return None
    else :
        return json.loads(result)


print('<< 국가 수출입 실적 데이터를 수집합니다. >>')
nat = input('국가 코드를 입력하세요. ex)미국:US,중국:CN,일본:JP >')
startYear = int(input('데이터를 몇 년 부터 수집할까요? >'))
endYear = int(input('데이터를 몇 년 까지 수집할까요? >'))

jsonResult = []
for year in range(startYear, endYear+1) :
    for mon in range(1, 13) :
        yyyymm= f"{year}{mon:0>2}"#201704
        jsonData = getNationTradeList(yyyymm, nat)
        print(jsonData)

        if jsonData['response']['header']['resultCode']=="00":
            item = jsonData['response']['body']['items']
            if item == '':
                break
            else :
                item = item['item']
                natTradeDic = {}
                natTradeDic['날짜']=item['year']
                natTradeDic['국가명']=item['statCdCntnKor1']
                natTradeDic['수출건수']=item['expCnt']
                natTradeDic['수출금액']=item['expDlr']
                natTradeDic['수입건수']=item['impCnt']
                natTradeDic['수입금액']=item['impDlr']
                natTradeDic['무역수지']=item['balPayments']
                jsonResult.append(natTradeDic)

with open(f'./웹크롤링/api활용/국가별수출입실적_{nat}.json','w',encoding='utf-8') as f:
    retJson = json.dumps(jsonResult, indent=4 , sort_keys=False,ensure_ascii=False)
    f.write(retJson)
print(f"./웹크롤링/api활용/국가별수출입실적_{nat}.json 저장완료")



















