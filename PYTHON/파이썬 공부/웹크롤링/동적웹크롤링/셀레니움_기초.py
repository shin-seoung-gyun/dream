from selenium import webdriver

# wd = webdriver.Chrome('chromedriver.exe')
# wd.get("https://naver.com")

# elem = wd.find_element_by_class_name("link_login")
# elem.click()

# wd.back()
# wd.forward()
# wd.refresh()
# wd.back()

# elem = wd.find_element_by_id('query')
from selenium.webdriver.common.keys import Keys
# elem.send_keys("피자")
# elem.send_keys(Keys.ENTER)

# elem = wd.find_elements_by_class_name("api_txt_lines.total_tit")
# for e in elem:
#     print(e.text)

# wd.get("https://www.google.co.kr/")
# html = wd.page_source
# print(html)

wd = webdriver.Chrome('chromedriver.exe')
wd.get("https://naver.com")
elem = wd.find_element_by_class_name("link_login")
elem.click()

wd.find_element_by_id("id").send_keys("tlstmdstmq")

wd.find_element_by_id("pw").send_keys("duapdlf")
# wd.find_element_by_id("log.login").click()

wd.find_element_by_id("id").send_keys("tlstmdstmq")
wd.find_element_by_id("id").clear()##해당 글자 지우기
wd.find_element_by_id("id").send_keys("tlstmdstmq")




a = input()