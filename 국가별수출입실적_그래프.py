import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family = font_name)##matplotlib에서 폰트 변경
matplotlib.rcParams['axes.unicode_minus']= False #-값 깨지는 경우

with open('./웹크롤링/api활용/국가별수출입실적_CN.json','r',encoding='utf-8')as f:
    jsonData1 = json.load(f)

with open('./웹크롤링/api활용/국가별수출입실적_US.json','r',encoding='utf-8')as f:
    jsonData2 = json.load(f)

with open('./웹크롤링/api활용/국가별수출입실적_JP.json','r',encoding='utf-8')as f:
    jsonData3 = json.load(f)


nat = jsonData1[0]['국가명']

dateList = [data['날짜'] for data in jsonData1]
importList = [data['수입금액'] for data in jsonData1]
exportList = [data['수출금액'] for data in jsonData1]
tdList = [data['무역수지'] for data in jsonData1]

nat2 = jsonData2[0]['국가명']
tdList2 = [data['무역수지'] for data in jsonData2]

nat3 = jsonData3[0]['국가명']
tdList3 = [data['무역수지'] for data in jsonData3]

indexList = [i for i in range(1,len(jsonData1)+1)]
indexList2 = [i for i in range(1,len(jsonData2)+1)]
indexList3 = [i for i in range(1,len(jsonData3)+1)]

# plt.plot(indexList,importList,'b',label='수입금액')
# plt.plot(indexList,exportList,'r--',label='수출금액')
# plt.plot(indexList,tdList,'g',label='무역수지')
# plt.xticks(indexList,dateList,rotation=85)
# plt.title(f'{nat} 수출입실적')
# plt.xlabel('날짜')
# plt.ylabel('원')
# plt.legend()
# plt.grid(True)
# plt.show()

##세국가의 무역수지 값만 겹쳐서 그래프만들기

plt.plot(indexList,tdList,'r',label=f'{nat}무역수지')
plt.plot(indexList2,tdList2,'g',label=f'{nat2}무역수지')
plt.plot(indexList3,tdList3,'b',label=f'{nat3}무역수지')
plt.xticks(indexList,dateList,rotation=85)
plt.title(f'국가별 무역수지실적')
plt.xlabel('날짜')
plt.ylabel('원')
plt.legend()
plt.grid(True)
plt.show()









