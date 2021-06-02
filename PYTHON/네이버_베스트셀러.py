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
while True:
    cnt =1
    while True:
        ########################################################################################
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
        ########################################################################################
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