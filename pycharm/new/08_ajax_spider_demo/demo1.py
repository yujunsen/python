from selenium import webdriver


# chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get('https://www.baidu.com')

# 通过page_source获取网页源代码
print(driver.page_source)

#driver.close()
driver.quit()
# driver.close()：关闭当前页面。
# driver.quit()：退出整个浏览器。