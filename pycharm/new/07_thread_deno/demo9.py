import requests
from lxml import etree
#from bs4 import BeautifulSoup
import os
import re
import csv



data_url = []

def parse_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    html = etree.HTML(response.text)
    # parse = etree.HTMLParser(encoding='utf-8')
    # html = etree.parse(response.text, parser=parse)
    imgs = html.xpath('//div[@class="j-r-list-c-img"]//@data-original')
    alts = html.xpath('//div[@class="j-r-list-c-img"]//@alt')
    #
    # #print(suffix)
    for img, alt in zip(imgs, alts):
        suffix = os.path.splitext(img)[1]
        alt = re.sub(r'[\?\.。！，!\ *]', '', alt)
        filename = alt + suffix
        movie = {'filename': filename, 'img': img}
        data_url.append(movie)
        print(movie)

def parse_page(url):
    base_url = 'http://www.budejie.com/'
    pase_url = []
    for x in range(1, 11):
        pase_url.append(base_url + str(x))
    for x in pase_url:
        #print(x)
        parse_url(x)
        print( str(x) + '====' * 30)
        #break

def write_cvs():
    header = ['filename', 'img']
    with open('demo9.csv', 'w', encoding='utf-8',  newline='') as fp:
        writer = csv.DictWriter(fp, header)
        writer.writeheader()
        writer.writerows(data_url)

def main():
    parse_page('http://www.budejie.com')
    write_cvs()

if __name__ == '__main__':
    main()
