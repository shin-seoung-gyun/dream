#1. 데이터 수집
# 기상자료개방 포털 -> 기후통계분석 -> 기온분석
#수원지역 1910-01-01~2020-12-31

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/수원_1910~2020.csv',encoding='cp949')
df.head()
#2. 데이터 탐색 및 전처리
df.info()
#칼럼명 변경
df.columns = ['date', 'local', 'temp_avg', 'temp_min', 'temp_max']
df.head()
#결측치 확인
df[df['temp_min'].isnull()]
df.loc[1144,['temp_min','temp_max']]
df.loc[1146,['temp_min','temp_max']]
#결측치 처리 - 평균값 대체
df.loc[1145,['temp_min','temp_max']]=(df.loc[1144,['temp_min','temp_max']]+df.loc[1146,['temp_min','temp_max']])/2
df.loc[1145,['temp_min','temp_max']]

#오늘 날짜의 기온의 기초통계
import datetime
now = datetime.datetime.now()
nowDate = now.strftime('%m-%d')
nowDate
data=df[df['date'].str[5:]==nowDate]
data.describe()

#3.시각화
#(1)박스플롯
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
ax.boxplot(data['temp_avg'],labels=['temp_avg'])
plt.show()

fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
plt.style.use('ggplot')
ax.boxplot(data[['temp_min','temp_avg','temp_max']],labels=['temp_min','temp_avg','temp_max'])
plt.show()

#꺾은선 그래프 출력

fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
x = data['date'].str[:4]
ax.plot(x,data['temp_avg'],label='avg',color='g')
ax.plot(x,data['temp_min'],label='min',color='b')
ax.plot(x,data['temp_max'],label='max',color='r')
ax.legend()
plt.title(f'{nowDate} Temp Changes')
plt.xticks(rotation='75')
plt.show()

#히스토그램 출력
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
freq,cls,_=ax.hist(round(data['temp_avg'],0), bins=100, range=(-50,50),density=True)
# freq
# cls
#누적상대도수 그래프 추가
cum_rel_freq = np.cumsum(freq)
class_value = [i for i in range(-50, 50)]
ax2 = ax.twinx()
ax2.plot(class_value, cum_rel_freq, ls='--', marker='o', color='gray')
##
ax.set_xlabel('temp')
ax.set_ylabel('relative freq')
minTemp=int(round(data['temp_avg'].min(),0))
maxTemp=int(round(data['temp_avg'].max(),0))
ax.set_xticks(np.linspace(minTemp,maxTemp,maxTemp-minTemp+1))
ax.set_xlim([minTemp, maxTemp])
plt.show()

##(1)06월의 데이터 기초통계 가져오기
data=df[df['date'].str[5:7]=='06']
# data
data.describe()
##(2)06월의 기온데이터 히스토그램
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
freq,cls,_=ax.hist(round(data['temp_avg'],0), bins=100, range=(-50,50),density=True)
#누적상대도수 그래프 추가
cum_rel_freq = np.cumsum(freq)
class_value = [i for i in range(-50, 50)]
ax2 = ax.twinx()
ax2.plot(class_value, cum_rel_freq, ls='--', marker='o', color='gray')
##
ax.set_xlabel('temp')
ax.set_ylabel('relative freq')
minTemp=int(round(data['temp_avg'].min(),0))
maxTemp=int(round(data['temp_avg'].max(),0))
ax.set_xticks(np.linspace(minTemp,maxTemp,maxTemp-minTemp+1))
ax.set_xlim([minTemp, maxTemp])
plt.show()

#06월 일별 boxplot그리기
dayAvgTempList = []
for i in range(30):
    day=f"06-{i+1:02}"
    dayAvgTempList.append(list(df[df['date'].str[5:]==day]['temp_avg']))
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
ax.boxplot(dayAvgTempList,labels=[i+1 for i in range(30)])
plt.show()

#08월의 평균 및 min, max 기온 그래프 시각화
df['year']= df['date'].str[:4]
df['mon']= df['date'].str[5:7]
df.head()
data = df.groupby(['year','mon'], as_index=False).mean()
data= data[data['mon']=='08']
data
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
x = data['year']
ax.plot(x,data['temp_avg'],label='avg',color='g')
ax.plot(x,data['temp_min'],label='min',color='b')
ax.plot(x,data['temp_max'],label='max',color='r')
ax.legend()
plt.title('8mon Temp Changes')
plt.xticks(rotation='75')
plt.show()





















