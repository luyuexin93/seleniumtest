from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#显示等待 超时消息

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#WebDriverWait(对象，最长超时时间，检测的间隔)
#WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_excpetions=None)
#ignored_exceptions:超时后的异常信息，默认情况下抛NoSuchElementException
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.ID,"kw"))
#until(method,message='') presence_of_element_located 判断元素是否存在
element.send_keys('selenium')

driver.quit()