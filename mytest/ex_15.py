from selenium import webdriver
import os
from time import  sleep
#可以设置浏览器的默认配置，如修改默认下载位置
fp = webdriver.FirefoxProfile()

#0设置下载浏览器默认路径
fp.set_preference("browser.download.folderList", 2)
#是否显示开始
fp.set_preference("browser.download.manger.showWhenStarting", False)
#指定下载目录，os.getcwd()返回当前工作目录
fp.set_preference("browser.download.dir", os.getcwd())

fp.set_preference("browser.helperApps.nerverAsk.saveToDisk", "application/octet-stream")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://pypi.org/project/selenium/")
driver.find_element_by_id('files-tab').click()
sleep(2)
driver.find_element_by_link_text("selenium-3.12.0.tar.gz").click()
driver.back()