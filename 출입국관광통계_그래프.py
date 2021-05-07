import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name) #matplotlib에서 폰트 변경
matplotlib.rcParams['axes.unicode_minus'] = False #-값 깨지는 경우 사용

with open('./웹크롤링/API활용/출입국관광통계_중국_방한외래관광객_201501_202012.json', 'r', \
    encoding='utf-8') as f:
    jsonDataCN = json.load(f)

with open('./웹크롤링/API활용/출입국관광통계_일본_방한외래관광객_201501_202012.json', 'r', \
    encoding='utf-8') as f:
    jsonDataJP = json.load(f)

with open('./웹크롤링/API활용/출입국관광통계_한국_국민해외관광객_201501_202012.json', 'r', \
encoding='utf-8') as f:
    jsonDataKo = json.load(f)

#2015~2020년도 그래프

indexList = [i for i in range(1, len(jsonDataCN)+1)]
dateList = [data['날짜'] for data in jsonDataCN]
cnList = [data['관광객수'] for data in jsonDataCN]
jpList = [data['관광객수'] for data in jsonDataJP]
koList = [data['관광객수'] for data in jsonDataKo]

# plt.xticks(indexList, dateList, rotation=85)
# plt.plot(indexList, cnList, 'b', label="중국인 입국자수")
# plt.plot(indexList, jpList, 'r--', label="일본인 입국자수")
# plt.plot(indexList, koList, 'g', label="한국 출국자수")


# plt.title(f"출입국 관광객수")
# plt.xlabel("날짜")
# plt.ylabel("수")
# plt.legend()
# plt.grid(True)
# plt.show()



#년도별 합산 그래프
yearSet = set([str(date)[0:4] for date in dateList])
yearList = list(yearSet)
yearList.sort()
print(yearList)

koyearDic={}
jpyearDic={}
cnyearDic={}
for year in yearList :
    koyearDic[year] = 0
    jpyearDic[year] = 0
    cnyearDic[year] = 0

for year in yearList :
    for data in jsonDataKo :
        if year in str(data['날짜']) :
            koyearDic[year] += data['관광객수']
    for data in jsonDataJP :
        if year in str(data['날짜']) :
            jpyearDic[year] += data['관광객수']
    for data in jsonDataCN :
        if year in str(data['날짜']) :
            cnyearDic[year] += data['관광객수']


plt.plot(yearList, [cnyearDic[year] for year in yearList], 'b', label="중국인 입국자수")
plt.plot(yearList, [jpyearDic[year] for year in yearList], 'r--', label="일본인 입국자수")
plt.plot(yearList, [koyearDic[year] for year in yearList], 'g', label="한국 출국자수")


plt.title(f"출입국 관광객수")
plt.xlabel("날짜")
plt.ylabel("수")
plt.legend()
plt.grid(True)
plt.show()