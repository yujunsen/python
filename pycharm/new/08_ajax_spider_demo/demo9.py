from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions  as EC
# from selenium.webdriver.common.by import By

#chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))
print(submitBtn.get_attribute('type'))
driver.save_screenshot('baidu.png') #截图