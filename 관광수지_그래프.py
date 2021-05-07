##2010~2020 수입 지출 데이터 받아오고, 각 년도별로 그래프 만들기
import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family = font_name)##matplotlib에서 폰트 변경
matplotlib.rcParams['axes.unicode_minus']= False #-값 깨지는 경우

with open('./웹크롤링/api활용/관광수지.json','r',encoding='utf-8')as f:
    jsonData1 = json.load(f)

dateList = [data['날짜'] for data in jsonData1]
setDate = set([str(date)[0:4] for date in dateList])
setDateList = list(setDate)
setDateList.sort()


inDic={}
outDic={}
for year in setDateList :##연습 생각
    inDic[year] = 0
    outDic[year] = 0

for year in setDateList:
    for data in jsonData1:
        if year in str(data['날짜']) :
            inDic[year] += data['관광수입']
        if year in str(data['날짜']) :
            outDic[year] += data['관광지출']



indexList = [i for i in range(1,len(setDateList)+1)]

plt.plot(indexList,[inDic[year] for year in setDateList],'r',label=f'관광수입')
plt.plot(indexList,[outDic[year] for year in setDateList],'g',label=f'관광지출')
plt.xticks(indexList,setDateList,rotation=85)
plt.title(f'연도별 관광수지')
plt.xlabel('날짜')
plt.ylabel('원')
plt.legend()
plt.grid(True)
plt.show()