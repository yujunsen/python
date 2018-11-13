from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://110.73.8.173:8123")
driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get('http://httpbin.org/ip')