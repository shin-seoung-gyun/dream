from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

url = "https://www.coffeebeankorea.com/store/store.asp"
wd = webdriver.Chrome("chromedriver.exe")

resultList=[]
wd.get(url)
for i in range(1,100) : #매장 번호
    time.sleep(1) 
    try :
        wd.execute_script("storePop2('%d')" %i)
    except :
        continue
html = wd.page_source
soup = BeautifulSoup(html, 'html.parser')
stores = soup.find_all("div", attrs={"class":"store_popup"})
print("매장개수 : ", len(stores))

for store in stores :
    store_name = store.find("div", attrs={"class" : "store_txt"}).text
    store_info = store.select("div.store_txt > table.store_table > tbody > tr > td")
    store_address_list = list(store_info[2])
    store_address = store_address_list[0]
    store_phone = store_info[3].string

    storeDic = {}
    storeDic['name'] = store_name
    storeDic['address'] = store_address
    storeDic['phone'] = store_phone
    resultList.append(storeDic)

with open(f"./웹크롤링/동적웹크롤링/Coffebean.json", "w", encoding="utf8") as outfile :
    retJson = json.dumps(resultList, indent=4, \
        sort_keys=False, ensure_ascii=False)
    outfile.write(retJson)











































