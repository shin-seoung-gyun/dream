##스크롤을 내리면서 데이터 가져오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://play.google.com/store/movies/top"
wd = webdriver.Chrome('chromedriver.exe')
##창 최대화
wd.maximize_window()
wd.get(url)
# ## 화면 높이 만큼 스크롤 내리기
# wd.execute_script("window.scrollTo(0,1080)")
# ##브라우저 높이만큼 스크롤 내리기
# wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
interval = 2##2초에 한번 스크롤 내리기
prev_h = wd.execute_script("return document.body.scrollHeight")
while True:
    #스크롤 가장 아래로 내림
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #대기
    time.sleep(interval)
    #스크롤 내린후 문서 높이
    cur_h = wd.execute_script("return document.body.scrollHeight")

    #페이지가 다 내려간 경우
    if cur_h == prev_h:
        break
    prev_h=cur_h
print("스크롤 완료")

html = wd.page_source
soup = BeautifulSoup(html,'html.parser')
movies = soup.find_all("div",attrs={'class':'Vpfmgd'})
print("영화갯수 : ", len(movies))

##영화제목
##영화가격
##영화장르
##별점정보
##링크정보
movieList = []

for movie in movies:
    movieDic={}
    title = movie.find('div',attrs={'class':'WsMG1c nnK0zc'})
    movieDic['title']=[title.text]
    price = movie.find('span',attrs={'class':'VfPpfd ZdBevf i5DZme'})
    movieDic['price']=[price.text]
    Genre = movie.find('div',attrs={'class':'KoLSrc'})##자료변경해보기
    Genre = "" if None == Genre else Genre.text
    movieDic['Genre']=[Genre]
    Rank1 = movie.find('div',attrs={'role':'img'})
    Rank= "" if None == Rank1 else Rank1['aria-label']
    movieDic['Rank']=[Rank]##자료 변경해보기
    Link1 = movie.find('div',attrs={'class':'b8cIId ReQCgd Q9MA7b'})
    Link2 = Link1.find('a')
    Link = Link2['href']
    movieDic['Link']=[Link]
    movieList.append(movieDic)

print(movieList)

a = input()



