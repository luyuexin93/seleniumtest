from selenium import webdriver
import time
driver=webdriver.Firefox()

#访问百度首页
first_url='https://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
time.sleep(3)

#访问新闻页面
second_url='https://news.baidu.com'
print("now access %s "%(second_url))
driver.get(second_url)
time.sleep(3)

#返回（后退）到百度页面
print("back to %s" %(first_url))
driver.back()
time.sleep(3)

#前进到新闻页
print("forward to %s" %(second_url))
driver.forward()
time.sleep(3)

driver.close()