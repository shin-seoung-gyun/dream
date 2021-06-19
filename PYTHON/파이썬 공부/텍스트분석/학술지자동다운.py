from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

wd = webdriver.Chrome("chromedriver.exe")

for i in range(0,1000,100):
    url = "http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=big+data&exQuery=language%3Aeng%E2%97%88&exQueryText=%EC%9E%91%EC%84%B1%EC%96%B8%EC%96%B4+%5B%EC%98%81%EC%96%B4%5D%40%40language%3Aeng%E2%97%88&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=big+data&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_over&colName=re_a_over&pageScale=100&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=big+data#redirect"
    param = "&iStartCount="+str(i)
    url = url + param
    wd.get(url)
    ##전체선택 클릭부분
    elem = wd.find_element_by_xpath('//*[@id="divContent"]/div[2]/div/div[3]/div[1]/div[1]/label/span')
    #elem.click() 안됨
    wd.execute_script("arguments[0].click();", elem)
    ##내보내기 클릭부분
    elem = wd.find_element_by_xpath('//*[@id="divContent"]/div[2]/div/div[3]/div[1]/div[1]/ul/li[1]/a')
    #wd.execute_script("arguments[0].click();", elem)
    elem.click()
    
    #새창 핸들링
    wd.switch_to_window(wd.window_handles[1])
    wd.get_window_position(wd.window_handles[1])

    ##새창 열릴때까지 대기 최대 10초,excel 저장
    elem = WebDriverWait(wd,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrap"]/form/div/div[2]/div[1]/div/ul/li[3]/label')))
    ##excel 클릭
    wd.execute_script("arguments[0].click();", elem)
    #내보내기 클릭
    elem = wd.find_element_by_xpath('//*[@id="riss_gubun"]/div[4]/a[1]')
    elem.click()
   
    ##본래창으로 돌아가기
    wd.switch_to_window(wd.window_handles[0])
    wd.get_window_position(wd.window_handles[0])





    

    









