from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains

#chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)

# 请求网页
#driver.get('https://www.douban.com/')


driver.get('https://www.baidu.com')
inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

submitTag.click()
actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submitTag)
actions.click(submitTag)
actions.perform()   #开始执行

'''
click_and_hold(element)：点击但不松开鼠标。
context_click(element)：右键点击。
double_click(element)：双击。 更多方法请参考：http://selenium-python.readthedocs.io/api.html
'''

