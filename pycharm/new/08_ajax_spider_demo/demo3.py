from selenium import webdriver


# chromedriver的绝对路径
# driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
#
# driver  = webdriver.Chrome(executable_path=driver_path)
#
# # 请求网页
# driver.get('https://www.douban.com/')
# #inputTag = driver.find_element_by_id('kw')
# #inputTag.send_keys('python')
# #inputTag.clear()
# inputTag = driver.find_element_by_name('remember')
# inputTag.click()

driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get('https://www.baidu.com')
inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')
inputTag.send_keys('python')
submitTag.click()