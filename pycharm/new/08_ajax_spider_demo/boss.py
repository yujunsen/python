from selenium import webdriver
from lxml import etree
import time
import csv
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.by import By

class boss_data():
    index = 0
    data_url = []
    job_data = []
    header ={'title', 'money', 'city', 'time', 'experience','education', 'description', 'team', 'company'}

    def __init__(self):
        driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def pasre_url(self):

        self.driver.get('https://www.zhipin.com/job_detail/?query=python')

        while self.index < 3:
            self.index += 1
            urls = self.driver.find_elements_by_xpath('//div[@class="info-primary"]/h3/a')

            for x in urls:
                #print(x.get_attribute('href'))
                self.data_url.append(x.get_attribute('href'))

            break
            next_td = self.driver.find_element_by_class_('next')
            if 'disabled' in next_td.get_attribute('class'):
                break
            next_td.click()
            time.sleep(1)


    def write_csv(self):
        with open(r'boss.csv', 'w',encoding='utf-8', newline='') as fp:
            witer = csv.DictWriter(fp,self.header)
            witer.writeheader()
            witer.writerows(self.job_data)
            self.job_data.clear()

    def pase_url(self):
        # url = self.data_url[0]
        # del  self.data_url[0]

        for url in self.data_url:
            self.driver.execute_script("window.open('%s')" % (url))
            self.driver.switch_to_window(self.driver.window_handles[1])

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'info-primary')))
            name = self.driver.find_element_by_class_name('info-primary').text

            name = name.split()
            #print(name.split())
            times = name[0].replace('发布于', '') + ' ' + name[1]
            title = name[2]
            money = self.driver.find_element_by_class_name('badge').text
            name = self.driver.find_element_by_xpath('//div[@class="info-primary"]/p').text
            name = name.replace('城市：', '').replace('经验：', ' ').replace('学历：', ' ').split()
            city = name[0]
            experience = name[1]
            education = name[2]
            name = self.driver.find_element_by_xpath('//div[@class="detail-content"]/div[1]').text
            description =name
            name = self.driver.find_element_by_xpath('//div[@class="detail-content"]/div[2]').text
            team = name
            name = self.driver.find_element_by_xpath('//div[@class="detail-content"]/div[3]').text.replace('...查看全部', '')
            company =name
            move = {'title':title, 'money':money, 'city': city, 'time':times, 'experience':experience,
                    'education':education, 'description':description, 'team':team, 'company':company}
            self.job_data.append(move)
            print(move)
            time.sleep(1)
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])
           # break
            time.sleep(1)
            a = 'dsad'



    def run(self):
        self.pasre_url()
        self.pase_url()
        self.write_csv()
        time.sleep(2)
        self.driver.close()

if __name__ == '__main__':
    t = boss_data()
    t.run()

