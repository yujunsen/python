from selenium import webdriver

#chromedriver的绝对路径
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'

driver  = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com')

driver.execute_script("window.open('https://www.baidu.com')")

driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)

driver.quit()