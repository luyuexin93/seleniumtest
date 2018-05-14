from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#引入webdriver中鼠标动作封装类

driver = webdriver.Firefox()
#wait for webdriver initialize
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.baidu.com")
"""
#这里搜索设置 定位方式用classname'pf'报错selenium.common.exceptions.WebDriverException: Message: TypeError: rect is undefined
#above = driver.find_element_by_class_name('pf')
"""
above = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[8]')

print(above.get_attribute('name'))
#perform()执行ActionChains中存储的行为 可理解为整个操作的提交

action = ActionChains(driver)
action.move_to_element(above).perform()

s=driver.find_element_by_link_text("搜索设置")
s.click()

'''
other methods
action.drag_and_drop(source,target)
action.context_click()
action.click_and_hold()
'''
