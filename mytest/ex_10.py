from selenium import webdriver
import os,time

driver = webdriver.Firefox()
#本地文件形式的url 以file:///开头 os.path.abspath()用于将相对路径转换为绝对路径
file_path='file:///'+ os.path.abspath('./checkbox.html')
driver.get(file_path)

#选择页面上所有tag name 为input的元素 此处为elements
inputs = driver.find_elements_by_tag_name('input')
#通过XPath和CSS找到type为checkbox的元素
#checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
#checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')

#然后从中过滤出type 为checkbox的元素，单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        time.sleep(1)
print(inputs)
#从获得的元素组中 去掉最后一个checkbox的勾
inputs.pop().click()

driver.quit()



