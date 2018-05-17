from selenium import webdriver
import time ,os

driver=webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

#切换到iframe（‘id=if’）
driver.switch_to.frame("if")

#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_elements_by_id("su").click()
time.sleep(3)

#先通过xpath定位到iframe
#xf = driver.find_element_by_xpath('//*[@class="if"]')
#再将定位对象传给switch_to.frame()方法
#driver.switch_to.frame(xf)

driver.quit()
