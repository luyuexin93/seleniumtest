from selenium import webdriver
from time import *
#模拟浏览器常见输入动作

driver=webdriver.Firefox()
driver.get("http://www.126.com")

sleep(3)
#进入iframe
driver.switch_to.frame("x-URS-iframe")

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
#可以用submit()方法来模拟搜索框的回车动作
sleep(3)
driver.quit()
