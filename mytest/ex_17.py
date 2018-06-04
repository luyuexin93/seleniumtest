from selenium import webdriver
from time import sleep

#test selenium js function

driver=webdriver.Firefox()
driver.implicitly_wait(10)

baidu="http://www.baidu.com"
driver.get(baidu)

#set browser window size
driver.set_window_size(600,600)

#search
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

#通过javascript设置浏览器窗口的滚动条位置(底部，右侧)
js="window.scrollTo(400,350);"
driver.execute_script(js)
sleep(3)
#调用js输入文本框
#text = "input text"
#js = "var sum =document.getElementById('id'); sum.value='" +text +"';"
#driver.execute_script(js)

driver.quit()