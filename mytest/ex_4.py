from selenium import webdriver
from time import *
#webElement 接口提供获取页面元素属性方法

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获得输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

#返回百度页面底部的备案信息
text = driver.find_element_by_id('cp').text
print(text)

#返回元素的属性值，可以是id、name、type或其他任意属性
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#返回元素的结果是否可观、返回结果为True或False
result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()