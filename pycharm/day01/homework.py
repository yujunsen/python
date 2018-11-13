
from bs4 import BeautifulSoup
import requests
#import urllib
#https://weheartit.com/inspirations/taylorswift?page=3&before=316439023&scrolling=true
url = 'https://weheartit.com/inspirations/taylorswift'
path = r'D:\code\python\pycharm\day01\picture'
url_pict = 'https://weheartit.com/'
count = 1

def get_picture(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('div.col.span-content > div > div > div > div > div > a')

    global  count;
    for img in imgs:
        pict_url =  url_pict + img.get('href')
        filename = path + '\\' + str(count) + '.jpg'
        r = requests.get(pict_url)
        soup = BeautifulSoup(r.text, 'lxml')
        pict = soup.select('div.cel.span-content.span-sm-12 > div > div > a > img')
        #print(pict[0].get('src'))
        r = requests.get(pict[0].get('src'))
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(count)
        count += 1
        if count >= 21:
            break

    """
    for i in imgs:
        a = url_pict + i.get('href')
        print(a)
      """
get_picture(url)


#urlretrieve(url, [filename=None, [reporthook=None, [data=None]]])