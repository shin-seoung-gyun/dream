##스크롤을 내리면서 데이터 가져오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://book.naver.com/bestsell/bestseller_list.nhn"
wd = webdriver.Chrome('chromedriver.exe')

##창 최대화
wd.maximize_window()
wd.get(url)

bookList = []

cnt2 = 1
interval = 2##2초에 한번 스크롤 내리기
while True:
    cnt =1
    while True:
        time.sleep(interval)
        html = wd.page_source##웹페이지 정보 모두 가져오기
        soup = BeautifulSoup(html,'html.parser')
        books = soup.find("ol",attrs={'class':'basic'})

        ##책제목
        dtTags = books.find_all('dt')
        for dtTag in dtTags:
            title = str(dtTag.text).replace('\n','')
            bookList.append(f'title: {title}')
        
        if cnt != 6:
            elem = wd.find_element_by_css_selector(f'#section_bestseller > div.paginate > a:nth-child({cnt+2})')
            elem.click()
            cnt += 1 
        else:
            break

    if cnt2 != 10:
            elem = wd.find_element_by_css_selector(f'#bestSellerDateUI > a.goUnit.goPrevMonth.on.N\=a\:srt\.calprev')
            elem.click()
            cnt2 += 1 
    else:
        break




print(bookList)

stay = input()