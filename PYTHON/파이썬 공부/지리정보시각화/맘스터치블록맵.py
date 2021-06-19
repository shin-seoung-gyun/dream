import pandas as pd
import numpy as np

data = pd.read_csv('./지리정보시각화/맘스터치매장.csv',encoding='utf-8',engine='python')
print(data.head())

#주소에서 시도, 군구 정보 분리
addr = pd.DataFrame(data['address'].apply(lambda v: v.split()[:2]).tolist(),columns=('시도','군구'))

print(addr['시도'].unique())
addr['시도'].replace("경기","경기도",inplace=True)
addr['시도'].replace("대전시","대전광역시",inplace=True)
addr['시도'].replace("경남","경상남도",inplace=True)
addr['시도'].replace("경북","경상북도",inplace=True)
addr['시도'].replace("충북","충청북도",inplace=True)
addr['시도'].replace("서울시","서울특별시",inplace=True)
addr['시도'].replace("충남","충청남도",inplace=True)
addr['시도'].replace("전남","전라남도",inplace=True)
addr['시도'].replace("전북","전라북도",inplace=True)
addr['시도'].replace("서울","서울특별시",inplace=True)
addr['시도'].replace("강원","강원도",inplace=True)
addr['시도'].replace("광주","광주시",inplace=True)
addr['시도'].replace("부산","부산광역시",inplace=True)
addr['시도'].replace("부산시","부산광역시",inplace=True)
addr['시도'].replace("울산","울산시",inplace=True)
addr['시도'].replace("제주","제주특별자치도",inplace=True)
addr['시도'].replace("제주시","제주특별자치도",inplace=True)
addr['시도'].replace("경기도안산시","안산시",inplace=True)
addr['시도'].replace("세종시","세종특별자치시",inplace=True)
addr['시도'].replace("세종","세종특별자치시",inplace=True)
addr['시도'].replace("선릉로64길","서울특별시",inplace=True)
addr['시도'].replace("부산해운대구해운대로","부산광역시",inplace=True)
addr['시도'].replace("전주시덕진구","전주시",inplace=True)
addr['시도'].replace("인천","인천광역시",inplace=True)
addr['시도'].replace("대구","대구광역시",inplace=True)
addr['시도'].replace("대구시","대구광역시",inplace=True)
addr['시도'].replace("대전","대전광역시",inplace=True)

print(addr['시도'].unique())
print(addr['군구'].unique())
addr['군구'].replace("나성북로","나성동",inplace=True)
addr['군구'].replace("서초중앙로22길","서초구",inplace=True)
addr['군구'].replace("세병로137","전주시",inplace=True)
addr['군구'].replace("시청대로","소담동",inplace=True)
addr['군구'].replace("새롬중앙로","새롬동",inplace=True)
addr['군구'].replace("보듬3로","아름동",inplace=True)
addr['군구'].replace("남세종로","소담동",inplace=True)
addr['군구'].replace("마음로","고운동",inplace=True)
addr['군구'].replace("절재로","아름동",inplace=True)
addr['군구'].replace("도움1로","종촌동",inplace=True)
addr['군구'].replace("한라대학로","노형동",inplace=True)
addr['군구'].replace("연삼로","이도이동",inplace=True)
addr['군구'].replace("누리로","한솔동",inplace=True)
addr.iloc[224]=['서울특별시','강남구']
addr.iloc[996]=['부산광역시','해운대구']
addr.iloc[127]=['제주특별자치도','제주시']

# addr.iloc[75]=['제주특별자치도','제주시']

#######################################################################################################


addr['시도군구']= addr.apply(lambda r:r['시도']+' '+r['군구'],axis=1)#칼럼 기준 axis=0은 인덱스 기준
print(addr.head())
addr['count']=0
print(addr.head())

addr_group = pd.DataFrame(addr.groupby(['시도','군구','시도군구'],as_index=False).count())
print(addr_group.head())

addr_group = addr_group.set_index("시도군구")
print(addr_group.head())

population = pd.read_excel('./지리정보시각화/행정구역_시군구_별__성별_인구수.xlsx')

print(population.head())
#칼럼명 바꾸기
population = population.rename(columns={'행정구역(시군구)별(1)':'시도','행정구역(시군구)별(2)':'군구'})
print(population.head())

#데이터 공백제거
for i in range(len(population)):
    population.loc[i,'시도'] = population['시도'][i].strip()
    population.loc[i,'군구'] = population['군구'][i].strip()

population['시도군구']=population.apply(lambda v:v['시도']+" "+v['군구'],axis=1)
print(population.head())

#소계부분 제외

population = population[population['군구']!='소계']
population = population.set_index("시도군구")
print(population.head())


#공공보건의 addr_group과 population 데이터 병합
addr_popul_merge = pd.merge(addr_group,population, how = 'inner', left_index=True,right_index=True)##inner방식으로하면 다른값은 무시하고 인덱스값으로 병합한다
print(addr_popul_merge.head())

local_MC_popul = addr_popul_merge[['시도_x','군구_x','count','총인구수 (명)']]
print(local_MC_popul.head())

#십만명 인구수 당 공공보건의료수 비율계산후 칼럼에 넣기
mc_cnt = local_MC_popul['count']
local_MC_popul['mc_ratio']= mc_cnt.div(local_MC_popul['총인구수 (명)'], axis=0)*100000#같은 행계산axis=0

local_MC_popul = local_MC_popul.rename(columns={'시도_x':'시도','군구_x':'군구','총인구수 (명)':'인구수'})
print(local_MC_popul.head())

##막대 그래프로 시각화
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rcParams, style
from matplotlib import font_manager, rc

#그래프 테마 바꾸기
style.use('ggplot')
font_path = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font',family = font_name)

# mc_ratio = local_MC_popul[['mc_ratio']]
# mc_ratio = mc_ratio.sort_values('mc_ratio',ascending=False)
# plt.rcParams['figure.figsize']=(25,5)
# mc_ratio.plot(kind='bar',rot=90)
# plt.show()

# print(mc_ratio.mean())
#
#블록맵으로 행정구역별
#블록맵 행정구역 경계선 x,y 데이터
BORDER_LINES = [
    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
     (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
    [(9, 12), (9, 10), (8, 10)], # 강원도
    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
     (13, 4), (14, 4), (14, 2)], # 충청남도
    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
     (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
    [(14, 4), (15, 4), (15, 6)], # 대전시
    [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도
    [(14, 8), (16, 8), (16, 10), (15, 10),
     (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
    [(15, 11), (16, 11), (16, 13)], # 울산시
    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
    [(18, 5), (20, 5), (20, 6)], # 전라남도
    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
]

#블록맵의 블록에 데이터 매핑 후 색을 표시하여 블록맵 그리는 함수
def draw_blockMap(blockedMap, targetData, title, color ):
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])

    datalabel = targetData

    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    
    plt.figure(figsize=(8, 13))
    plt.title(title)
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=color, edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'

        if row.isna()[0] :
            continue
        dispname = row['shortName']
        """
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. (중구, 서구)
        if row['광역시도'].endswith('시') and not row['광역시도'].startswith('세종'):
            dispname = '{}\n{}'.format(row['광역시도'][:2], row['행정구역'][:-1])
            if len(row['행정구역']) <= 2:
                dispname += row['행정구역'][-1]
        else:
            dispname = row['행정구역'][:-1]
        """       
        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 7.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                      fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)
    
    # 시도 경계 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=4)

    plt.gca().invert_yaxis()
    #plt.gca().set_aspect(1)
    plt.axis('off')
    
    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.savefig('./지리정보시각화/' + 'blockMap_' + targetData + '.png')
    plt.show()

data_draw_korea = pd.read_csv('./지리정보시각화/data_draw_korea.csv',index_col=0,encoding='utf-8',engine='python')
print(data_draw_korea.head())

data_draw_korea['시도군구'] = data_draw_korea.apply(lambda v:v['광역시도']+" "+v['행정구역'],axis=1)
data_draw_korea = data_draw_korea.set_index('시도군구')
print(data_draw_korea.head())

# 데이터 외부 병합 - 값이 없는 경우 Nan이 됨
data_all = pd.merge(data_draw_korea,local_MC_popul,how='outer',left_index=True,right_index=True)
print(data_all.head())

# data_all= data_all[data_all['x'].notnull]
data_all.dropna(subset=['x'],inplace=True)

# draw_blockMap(data_all, 'count','행정구역별 맘스터치 수', 'Blues')

draw_blockMap(data_all, 'mc_ratio','행정구역별 인구수 대비 맘스터치 비율', 'Reds')

