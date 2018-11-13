from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains

#chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

for x in driver.get_cookies():
    print(x)
print('--' * 30)

print(driver.get_cookie('BAIDUID'))
print('--' * 30)
driver.delete_cookie('BAIDUID')

for x in driver.get_cookies():
    print(x)
print('--' * 30)