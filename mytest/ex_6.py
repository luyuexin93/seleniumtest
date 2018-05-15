from selenium import webdriver
#引入keys模块
from selenium.webdriver.common.keys import Keys
#keyboard example code

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
inp=driver.find_element_by_id("kw")

#输入框输入内容
inp.send_keys("seleniumm")

#删除多输入的一个m
inp.send_keys(Keys.BACK_SPACE)

#输入空格键+"教程"
inp.send_keys(Keys.SPACE)
inp.send_keys("教程")

#ctrl+a
inp.send_keys(Keys.CONTROL,'a')
#Enter
inp.send_keys(Keys.ENTER)

driver.quit()

