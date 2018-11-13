from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.by import By

#chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com')
#driver.implicitly_wait(10)
# try:
#     driver.find_element_by_id('dasdas')
# except:
#     print('a')

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'sad'))
    )
except:
    print('a')
    driver.quit()

