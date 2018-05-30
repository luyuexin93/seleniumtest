from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

cookie = driver.get_cookies()
name =driver.get_cookie('value')
driver.add_cookie({'name'})
print(name)
print(cookie)

driver.quit()


