from WebUtil import WebUtil
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
html = WebUtil.getRequestUrl(url)

#BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

#객체에 저장된 html 내용확인
print(soup.prettify())

# with open("./웹크롤링/정적웹크롤링/네이버홈페이지.html",'w',encoding='utf8') as f:
#     f.write(soup.prettify())

##클래스 검색
aTag = soup.select("a.nav")

for a in aTag :
    print(a.text)

aTag_News = soup.find("a",attrs={'class':'nav','data-clk':'svc.news'})
print(aTag_News)
#태그내의 값을 얻을때
print(aTag_News.text)
#태그의 속성값 얻을때는 키값으로 넣어주면 된다.
print(aTag_News["class"])

print(aTag_News["href"])


##(1)뉴스 스탠드 최상위 태그 가져오기
newTag = soup.select("div.thumb_area>div>a>img")##select로 찾기

for val in newTag :
    print(val['alt'])


##(2) 뉴스 스탠드 검색
newTag = soup.find('div',attrs={'class':'thumb_area'})##find로 찾기 
divTag = newTag.find_all('div',attrs={'class':'thumb_box'})
for tag in divTag :
    imgTag = tag.find('img')
    print(imgTag['alt'])
##두방법 모두 알아야함 














