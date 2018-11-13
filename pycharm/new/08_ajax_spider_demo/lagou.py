from selenium import webdriver
from lxml import etree
import time
import csv
import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions  as EC
# from selenium.webdriver.common.by import By
class spider():
    page_urls = []
    header  = ['title', 'money', 'city', 'claim', 'types', 'education', 'times', 'description']
    cvs_data =[]
    index = 0
    def __init__(self):
        driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=driver_path)
    def parese_url(self, url):
        #chromedriver的绝对路径

        self.driver.get(url)
        next_bt = self.driver.find_element_by_class_name('pager_next')
        #pager_next pager_next_disabled
        while self.index < 2:
            html = etree.HTML(self.driver.page_source)
            page_url = html.xpath('//a[@class="position_link"]/@href')
            self.page_urls.extend(page_url)
            #print(page_url)

            next_bt.click()
            print(self.index)
            next_bt = self.driver.find_element_by_class_name('pager_next')
            if "pager_next_disabled" in next_bt.get_attribute("class"):
                break
            self.index += 1
            time.sleep(1)
        print('ok')

    def parse_url(self):

        while len(self.page_urls) != 0:
            self.driver.execute_script("window.open('%s')" %(self.page_urls[0]))
            del self.page_urls[0]
            self.driver.switch_to_window(self.driver.window_handles[1])

            title = self.driver.find_element_by_class_name('name').text
            job_request = self.driver.find_element_by_class_name('job_request').text
            job_request = job_request.split('/')
            money = job_request[0]
            city = job_request[1]
            claim = job_request[2].split()
            education = job_request[3]
            types = job_request[4].split()
            times = self.driver.find_element_by_class_name('publish_time').text
            times = times.split()[0]
            job_bt = self.driver.find_element_by_class_name('job_bt').text
            #print(job_bt)

            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])
            #print(self.driver.current_url)
            move = {'title': title, 'money':money, 'city':city, 'claim':claim, 'types':types[0], 'education':education, 'times':times, 'description':job_bt}
            print(move)
            self.cvs_data.append(move)
            time.sleep(1)
    def write_csv(self):
        with open(r'lagou.csv', 'w',encoding='utf-8', newline='') as fp:
            witer = csv.DictWriter(fp,self.header)
            witer.writeheader()
            witer.writerows(self.cvs_data)
            self.cvs_data.clear()

    def run(self):
        self.parese_url('https://www.lagou.com/jobs/list_python')
        self.parse_url()
        self.write_csv()
        time.sleep(2)
        self.driver.close()

if __name__ == '__main__':
    t = spider()
    t.run()
    # a = [1,2,3,4]
    # b = [7,9]
    # b.extend(a)
    # b.sort()
    # print(b)
    # a = '7k-14k /成都 / 经验1-3年 / 大专及以上 / 全职'
    # b = a.split('/')
    # print(b)
    # a = r' 全职\nPython\n1天前  发布于拉勾网'
    # b =re.sub(r'\\n.*', '', a)
    # print(b)
    # a =  ' 全职\nPython\n1天前  发布于拉勾网'
    # #b =re.sub(r'\s', ' ', a)
    # #b = b.split()
    # b = a.split()
    # print(b)


    pass

