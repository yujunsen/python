# coding:utf-8



from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import requests
import os
#from selenium import webdriver
#urls = 'http://m.mmjpg.com/mm/1418/'

path = r'D:\code\python\picture'
count = 1

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
    'Referer': 'http://m.mmjpg.com/mm/1418/1'
}
def get_picture(url, dir):
    global count

    r = requests.get(url, headers = headers)
    filename = dir + '\\' + str(count) + '.jpg'
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(filename)
def get_url(url, dir):
    wb_data = urllib.request.urlopen(url)
    soup = BeautifulSoup(wb_data.read(), 'lxml')
    imgs = soup.select('img')#('div.content > div > a > img')
    #print(imgs[0].get('src'))
    if len(imgs) == 0:
        print(dir + '套图完成')
        return 0
    else:
        get_picture(imgs[0].get('src'), dir)

    return 1
    #img = imgs[0].get('src')
    #get_picture(imgs[0].get('src'))
def get_page(urls, dir):
    global count
    is_page = 1
    while is_page == 1:
    #while count <= 45:
        url = urls + '/' + str(count)
        is_page = get_url(url, dir)
        #print(url)
        count += 1
    count = 1
    #print(get_url())

def get_mm():
    wb_data = urllib.request.urlopen('http://www.mmjpg.com/')
    soup = BeautifulSoup(wb_data.read(), 'lxml')
    imgs = soup.select('body > div.main > div.pic > ul > li > a > img')
    urls = soup.select('body > div.main > div.pic > ul > li > a')
    for tilte, url in zip(imgs, urls):
        dir = path + '\\' + tilte.get('alt')
        isExists = os.path.exists(dir)
        if not isExists:
           # print('创建文件夹 ' + dir)
            os.makedirs(dir)
        url = url.get('href')
        #print(url)
        get_page(url, dir)

#get_url('http://www.mmjpg.com/mm/1418/2', path)
#get_mm()
get_page('http://m.mmjpg.com/mm/1304', path)

""""

#获得系统的编码
type = sys.getfilesystemencoding()

url = 'http://m.mmjpg.com/mm/1418/1'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
#imgs = soup.select('div.content > div > a > img')

for i in wb_data:
    #print(i)
    #print(str(i.get('alt')))
    #s = i.decode(type)
    print(i.encoding )

"""
"""
import urllib.request
import sys

weburl="http://m.mmjpg.com/mm/1418"

req=urllib.request.Request(url=weburl)
response=urllib.request.urlopen(req)
content = response.read()
#获得系统的编码
type = sys.getfilesystemencoding()
#设置爬出内容的编码
content = content.decode(type)
file = open("c。txt",'w',10000)
file.write(str(content))
file.close()
print(content)
"""