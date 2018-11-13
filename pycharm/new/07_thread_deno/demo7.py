import requests
from lxml import etree
from urllib import request
import os
import re

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/'
    }
    repsonse = requests.get(url, headers=headers)
    #print(repsonse.text)
    html = etree.HTML(repsonse.text)
    imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in imgs:
        img_url = img.get('data-original')
        #print(img_url)
        alt = img.get('alt')
        alt = re.sub(r'[\?\.。！，!]', '', alt)
        #print(alt)
        suffix = os.path.splitext(img_url)[1]
        #print(suffix)
        filename = alt + suffix
        print(filename)
        request.urlretrieve(img_url, 'img/' + filename)


def main():
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%s'  %x
       # print(url)
        parse_page(url)
        break


if __name__ == '__main__':
    main()