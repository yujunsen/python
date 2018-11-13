from selenium import webdriver
from selenium.webdriver.common.by import By

# chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
#driver.close()
#driver.quit()
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
#inputTag = driver.find_element_by_id('kw')
#inputTag = driver.find_element_by_name('wd')
#inputTag = driver.find_element_by_class_name('s_ipt')
#inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
#inputTag = driver.find_element_by_css_selector('.quickdelete-wrap > input')
inputTag = driver.find_element(By.CSS_SELECTOR, '.quickdelete-wrap > input')

inputTag.send_keys('python')