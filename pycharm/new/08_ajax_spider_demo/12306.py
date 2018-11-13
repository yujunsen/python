from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Qianbiao(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.initmy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.passenger = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
    def _login(self):
        driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(self.login_url)
        #send_keys_to_element
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        username.send_keys('910387559@qq.com')
        password.send_keys('y13456165231')
        WebDriverWait(self.driver, 1000).until(
            EC.url_to_be(self.initmy_url)
        )
        print('登陆成功')

    def wait_input(self):
        # self.from_station = input('出发地：')
        # self.to_station = input('目的地：')
        # self.depart_time = input('出发日：')
        # self.passengers = input('乘客姓名（如有多个用英文逗号隔开）：').split(',')
        # self.trans = input('车次号（如有多个车次用英文逗号隔开）：').split(',')
        self.from_station = '成都'
        self.to_station = '达州'
        self.depart_time = '2018-08-13'
        # self.passengers = input('乘客姓名（如有多个用英文逗号隔开）：').split(',')
        self.passengers = '余俊森'.split(',')
        self.trans = 'K352,K998,K118,K530'.split(',')
        self.seat = '硬座'.split(',')


    def _order_ticker(self):
        self.driver.get(self.search_url)
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'),self.from_station))
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station))
        WebDriverWait(self.driver, 1000).until(
                    EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.depart_time))
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket')))
        searchBtn = self.driver.find_element_by_id('query_ticket')
        searchBtn.click()

        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//tbody[@id="queryLeftTable"]/tr')))

        tr_list = self.driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        for tr in tr_list:
            train_number = tr.find_element_by_class_name('number').text
            if train_number in self.trans:
                left_ticket = tr.find_element_by_xpath('./td[10]').text#//tbody[@id="queryLeftTable"]/tr[not(@datatran)]/td[10]
                if left_ticket == '有' or left_ticket.isdigit():
                    print(train_number + ' 有票')
                    orderBtn = tr.find_element_by_xpath('./td[13]/a')
                    if 'btn72' in orderBtn.get_attribute('class'):
                        print("可以预定")
                        orderBtn.click()
                        WebDriverWait(self.driver, 1000).until(
                            EC.url_to_be(self.passenger))
                        WebDriverWait(self.driver, 1000).until(
                            EC.presence_of_element_located((By.XPATH, '//ul[@id="normal_passenger_id"]/li')))
                        normal_passenger_id = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]/li')
                        for x in normal_passenger_id:
                            input = x.find_element_by_xpath('./input')
                            name = x.find_element_by_xpath('./label').text
                            if name in self.passengers:
                                input.click()
                                #print(name)
                        selects = self.driver.find_elements_by_xpath('//select[@id="seatType_1"]/option')
                        for index, x in enumerate(selects):
                            name = x.text.strip().split('（')[0]
                            if  name in self.seat:
                                selectTag = Select(self.driver.find_element_by_id('seatType_1'))
                                selectTag.select_by_index(index)
                                break
                            index += 1

                        submitTAG = self.driver.find_element_by_id('submitOrder_id')
                        submitTAG.click()
                        self.driver.implicitly_wait(4)
                        # WebDriverWait(self.driver, 1000).until(
                        #     #EC.presence_of_element_located((By.ID,'qr_submit_id'))
                        #     EC.text_to_be_present_in_element((By.XPATH, '//a[@id="qr_submit_id"]'), '确认')
                        # )

                        submitTAG = self.driver.find_elements_by_xpath('//a[@id="qr_submit_id"]')
                        submitTAG.click()
                        # selectTag = Select(self.driver.find_element_by_id('seatType_1'))
                        # selectTag.select_by_index(1)

                        break

            #print(train_number)
            #print('==' * 20)


    def run(self):
        self.wait_input()
        self._login()
        self._order_ticker()

        time.sleep(2)
        #self.driver.quit()

def test():
    url = 'https://kyfw.12306.cn/otn/leftTicket/init'
    driver_path = r'D:\Program Files (x86)\chromedriver\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    #from_station = driver.find_element_by_id('fromStationText')
    selectTag = Select(driver.find_element_by_id('fromStationText'))
    selectTag.select_by_visible_text('成都')


"""
 from selenium.webdriver.support.ui import Select
 # 选中这个标签，然后使用Select创建对象
 selectTag = Select(driver.find_element_by_name("jumpMenu"))
 # 根据索引选择
 selectTag.select_by_index(1)
 # 根据值选择
 selectTag.select_by_value("http://www.95yueba.com")
 # 根据可视的文本选择
 selectTag.select_by_visible_text("95秀客户端")
 # 取消选中所有选项
 selectTag.deselect_all()
 """
if __name__ == "__main__":
    spider = Qianbiao()
    spider.run()

    #test()


    # a = '1'
    # if a == '有' or a.isdigit():
    #     print(a)
    # if 'btn72' in 'btn72':
    #     print(2)
    # a = ['余俊森', '刘国庆', '夏华翠', '余大河', '余俊杰(学生)']
    # b = '余俊森,刘国庆,夏华翠,余大河,余俊杰(学生)'.split(',')
    # for x in b:
    #     if '余俊杰' in x:
    #         print(2)