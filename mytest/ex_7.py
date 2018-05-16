from selenium import webdriver
import  time

driver=webdriver.Firefox()
driver.maximize_window()
driver.get('http://10.10.40.10:8080/psc110/')

print('Before login=============')
title=driver.title
print(title)
#print url
now_url=driver.current_url
print(now_url)

#username&password
usrname=driver.find_element_by_id('uname')
password=driver.find_element_by_id('password')
usrname.clear()
usrname.send_keys('057102')
password.clear()
password.send_keys('057102')
#login
driver.find_element_by_id('login').click()
driver.find_element_by_id('login').submit()

time.sleep(3)
print('After login==============')
#print title
title=driver.title
print(title)
#print url
now_url=driver.current_url
print(now_url)

driver.quit()

