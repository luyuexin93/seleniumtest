# coding=utf-8

from selenium import webdriver
from time import *

#driver=webdriver.Firefox()
driver=webdriver.Chrome()


driver.get("http://www.baidu.com")
sleep(2)

driver.find_element_by_id("kw").send_keys("Selenum3")
driver.find_element_by_id("su").click()
driver.find_element_by_link_text("新闻").click()
#driver.find_element_by_class_name("bg s_btn")
#driver.find_element_by_tag_name()
driver.find_element_by_xpath("//*[@id='s_tab']/a[1]").click() #Xpath 元素属性值

sleep(5)
driver.quit()