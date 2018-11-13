from bs4 import BeautifulSoup
import requests
import pymongo


url1 = 'https://cd.lianjia.com/zufang/pg1'
urls = ['https://cd.lianjia.com/zufang/pg{}'.format(str(i)) for i in range(1, 5, 1)]
client = pymongo.MongoClient('localhost', 27017)
homework = client['homework']
lianjia = homework['lianjia']
list = []

headers={
    'User-Agent'    : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}



def get_data(url):
    wb_data = requests.get(url, timeout=30)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('div.title > h1')
    price = soup.select('div.price > span.total ')
    area  = soup.select('div.zf-room > p:nth-of-type(1)')
    house = soup.select('div.zf-room > p:nth-of-type(2)')
    floor = soup.select('div.zf-room > p:nth-of-type(3)')
    ori = soup.select('div.zf-room > p:nth-of-type(5)')
    com = soup.select('div.zf-room > p:nth-of-type(6)')
    posit = soup.select('div.zf-room > p:nth-of-type(7)')
    time = soup.select('div.zf-room > p:nth-of-type(8)')

    info = {
        "title"        :  title[0].get_text(),
        "价格"        :  price[0].get_text() + '元',
        "面积"        :  area[0].get_text().replace('面积：', ''),
        "房屋户型"     :  house[0].get_text().replace('房屋户型：', ''),
        "楼层"        :  floor[0].get_text().replace('楼层：', ''),
        "地铁"        :  ori[0].get_text().replace('地铁：', ''),
        "小区"        :  com[0].get_text().replace('小区：', '').replace('\n', '').replace('            -', ''),
        "位置"        :  posit[0].get_text().replace('位置：', ''),
        "时间"        :  time[0].get_text().replace('时间：', '')
    }
    list.append(info)
    lianjia.insert_one(info)
    print(info)
    # with open(r'D:\code\python\day01\aa.txt', "a+") as f:
    #     print('   ' + a + ':' + b)
    #     print('\n')
    # print('\n')
    #time.sleep(1)

#body > div:nth-child(7) > div.overview > div.content.zf-content > div.zf-room > p:nth-child(1)
#nth-of-type
def get_attractions(url):
    wb_data = requests.get(url1, timeout=30)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    url = soup.select(' div.info-panel > h2 > a')

    for i in url:
        get_data(i.get('href'))

if __name__ == "__main__":
    for i in urls:
        get_attractions(i)
    #print('ok')
    #for data in list:
    #    print(data)
    #client.close()
    print("over")

