from bs4 import BeautifulSoup
import requests


url1 = 'https://cd.lianjia.com/zufang/pg1'
urls = ['https://cd.lianjia.com/zufang/pg{}'.format(str(i)) for i in range(1, 101, 1)]

headers={
    'User-Agent'    : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}

list = []

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
    print(info)
    with open(r'D:\code\python\day01\aa.txt', "a+") as f:
        for a, b in zip(info.keys(), info.values()):
            f.write('   ' + a + ':' + b)
            f.write('\n')
        f.write('\n')
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
    #get_data('https://cd.lianjia.com/zufang/106101336156.html')
    #get_attractions(url1)
    #for i in list:
    #   print(i)
    for i in urls:
        get_attractions(i)


"""
def get_attractions(url, data=None):
    wb_data = requests.get(url1, timeout = 30)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tiltes = soup.select(' div.info-panel > h2 > a')
    imgs   = soup.select(' div.pic-panel > a > img')
    prices = soup.select(' div.price > span')
    panels = soup.select(' div.info-panel > div.col-1 > div.where ')
    cons   = soup.select(' div.other > div')
    haskeys = soup.select(' span.haskey-ex > span')
    if data == None:
        for tilte, img, price, panel, con, haskey in zip(tiltes, imgs, prices, panels, cons, haskeys):
            data = {
                'tilte' : tilte.get_text(),
                'img'   : img.get('data-img'),
                'price' : price.get_text(),
                'panel' : ''.join(panel.get_text().split()),
                'con'   : con.get_text(),
                'haskey': haskey.get_text(),
                'url'   : tilte.get('href')
            }
            print(data)

#temp = tiltes
#for i in temp:
    #print(i.get('href'))
   # print(i.get_text())
    #print(i.get('href'))
    #print(i.get('data-img'))
    #print(i.stripped_strings)


#list(cate.stripped_strings)
if __name__ == "__main__":
    for i in urls:
        get_attractions(i)
"""