#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获得百度搜索窗口句柄
search_windows = driver.current_window_handle
#此处直接用find_element_by_link_text("登录").click()报错所以使用二级定位
"""selenium.common.exceptions.ElementNotInteractableException: Message: Element <a class="lb" href="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5" name="tj_login"> 
could not be scrolled into view"""

driver.find_element_by_id("u1").find_element_by_link_text("登录").click()
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[4]/a").click()
#延迟2秒等待窗口打开 若不设置all_handles可能无法获取到注册窗口
time.sleep(2)
#获得当前所有打开窗口的句柄
all_handles = driver.window_handles

print(all_handles)
print(search_windows)
#进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys('username')
        driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys('password')
        time.sleep(3)
    time.sleep(1)

#回到搜索窗口
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window!')
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)
    time.sleep(1)

driver.quit()