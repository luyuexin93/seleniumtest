from selenium import  webdriver
from selenium.webdriver import ActionChains as AC
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#鼠标悬停至设置 链接
link = driver.find_element_by_id('u1').find_element_by_link_text("设置")
AC(driver).move_to_element(link).perform()
driver.find_element_by_link_text("搜索设置").click()

driver.find_element_by_link_text("保存设置").click()
time.sleep(2)
#点击警告框确认
driver.switch_to.alert.accept()

driver.quit()
