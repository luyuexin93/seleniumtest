from selenium import webdriver
import os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('upfile.html')
driver.get(file_path)

#定位上传按钮，添加本地文件 用send_keys实现上传文件
driver.find_element_by_name("file").send_keys('/home/lyx/testfile/upload_file.txt')
#另一种方法是使用windows窗口自动化工具AUTOIT,缺点python调用第三方exe执行过程时长或报错均无法感知
# os.system("D:\\upfile.exe")
driver.quit()