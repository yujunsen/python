from bs4 import BeautifulSoup
from pyecharts import Bar
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}
ALL_DATA = []
def parse_page(url):
    wb_data = requests.get(url, headers = headers)
    soup = BeautifulSoup(wb_data.content.decode('utf-8'), 'html5lib')
    conMidtab = soup.find('div', class_= 'conMidtab')
    tables = conMidtab.find_all('table')

    for table in tables:
        #print('=' * 80)
        #print(x)
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            # for city_td in tds:
            #     city = list(city_td.stripped_strings)[0]
            #     print(city)
            #     #print('==' * 30)
            #     #break
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            #print(city)
            temp_td = tds[-2]#list(tds[-2].stripped_strings)[0]
            min_temp = list(temp_td.stripped_strings)[0]
            #print(city)
           # print(min_temp)
            print({'city':city, 'min_temp':min_temp})
            ALL_DATA.append({'city':city, 'min_temp':min_temp})
            #break
       # break

    #print(wb_data.content.decode('utf-8'))

def data_sort():
    crites = []
    ALL_DATA.sort(key=lambda data:int(data['min_temp']))

    #print(ALL_DATA)
    # for x in ALL_DATA[0:10]:
    #     print(x)
    crites = list(map(lambda x:x['city'], ALL_DATA[0:10]))
    temps = list(map(lambda x:x['min_temp'], ALL_DATA[0:10]))
    chart = Bar('中国最低气温排行榜')
    chart.add('', crites, temps)
    chart.render('temperature.html')

if __name__ == '__main__':
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            'http://www.weather.com.cn/textFC/gat.shtml'
            ]
    for url in urls:
        parse_page(url)
        print('==' * 20)
    data_sort()
    #parse_page(urls[7])
    # for x in urls:
    #     print(x)