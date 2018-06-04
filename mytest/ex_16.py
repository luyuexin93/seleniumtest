from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

sleep(3)
#获取所有cookie信息
cookie = driver.get_cookies()
name =driver.get_cookie('value')
#添加浏览器cookie
driver.add_cookie({'name':'key-aaa','value':'value-bb'})
print(name)
print(cookie)

for cookie in driver.get_cookies():
    print ("%s -> %s" %(cookie['name'],cookie['value']))

driver.quit()


