import folium

#지도의 처음 시각화부분

m = folium.Map(location=[37.250332, 127.022828],zoom_start=15)##처음시작위치tiles='Stamen Terrain'

folium.Marker(location = [37.250332, 127.022828],popup = '(주)엠아이티능력개발원', icon=folium.Icon(icon='star',color='red')).add_to(m)##마커만들기

folium.CircleMarker(location = [37.250332, 127.022828],radius=100,color='#ffffgg',fill_color ='#ffffgg',popup = '(주)엠아이티능력개발원').add_to(m)


m.save('./지리정보시각화/엠아이티.html')


latlon =[[37.31355679999999, 127.08034150000003],
[37.35959300000016, 127.105316],
[37.388204699999996, 126.66208460000007],
[37.19821445962207, 127.07333060688757],
[37.3862876275833, 126.96253325015414],
[37.31864776315991, 127.08885641049494],
[37.56661020000001, 126.97838810000007]]

from folium.plugins import MarkerCluster
m_cluster = MarkerCluster().add_to(m)

for i in range(len(latlon)):
    folium.Marker(location=latlon[i],popup=str(i),icon= folium.Icon(color='darkblue',icon='info-sign')).add_to(m_cluster)
m.save('./지리정보시각화/엠아이티.html')

import json
with open('./지리정보시각화/seoul_muncipalities_geo.json','r',encoding='utf-8')as f :
    geo = json.loads(f.read())
folium.GeoJson(geo,name ="서울특별시").add_to(m)
m.save('./지리정보시각화/엠아이티.html')


with open('./지리정보시각화/TL_SCCO_CTPRVN.json','r',encoding='utf-8')as f :
    geo = json.loads(f.read())
folium.GeoJson(geo).add_to(m)
m.save('./지리정보시각화/엠아이티.html')







