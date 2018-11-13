import requests
from lxml import etree
#from bs4 import BeautifulSoup
import os
import re
import csv
import threading
from queue import Queue
from urllib import request

data_url = []

class Procuder(threading.Thread):
    def __init__(self, page_queue, img_queue, data_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
        self.data_queue = data_queue
    def run(self):
        while True:
            if self.page_queue.empty():
                print('%s break' %threading.current_thread())
                break
            self.parse_url(self.page_queue.get())


    def parse_url(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        imgs = html.xpath('//div[@class="j-r-list-c-img"]//@data-original')
        alts = html.xpath('//div[@class="j-r-list-c-img"]//@alt')
        for img, alt in zip(imgs, alts):
            suffix = os.path.splitext(img)[1]
            alt = re.sub(r'[\?\.。！，!\ *😊【】《》/]', '', alt)
            filename = alt + suffix
           # movie = {'filename': filename, 'img': img}
            self.img_queue.put((filename, img))
            self.data_queue.put((filename, img))
            #print(movie)

class Consumer(threading.Thread):

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                print('%s break' %threading.current_thread())
                break
            filename, img = self.img_queue.get()
            request.urlretrieve(img, 'img/' + filename)
            #print(filename)

class Consumer1(threading.Thread):
    header = ['filename', 'img']
    def __init__(self, page_queue, data_queue, gLock, *args, **kwargs):
        super(Consumer1, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.gLock = gLock
    def run(self):
        while True:
            if self.page_queue.empty() and self.data_queue.empty():
                print('%s break' % threading.current_thread())
                break
            #print(1)
            filename, img = self.data_queue.get(timeout=40)
            #print(joke_info)
            value = [{'filename':filename, 'img':img}]
            self.gLock.acquire()
            with open('demo10.csv', 'a', encoding='utf-8', newline='') as fp:
                writer = csv.DictWriter(fp, self.header)
                #writer.writeheader()
                writer.writerows(value)
            self.gLock.release()
            print('保存一条')


def write_cvs():
    header = ['filename', 'img']
    with open('demo10.csv', 'w', encoding='utf-8',  newline='') as fp:
        writer = csv.DictWriter(fp, header)
        writer.writeheader()


def main():
    page_queue = Queue(10)
    img_queue = Queue(500)
    data_queue = Queue(500)
    gLock = threading.Lock()
    base_url = 'http://www.budejie.com/'
    pase_url = []
    for x in range(1, 11):
        page_queue.put(base_url + str(x))
       # pase_url.append(base_url + str(x))
    # for x in pase_url:
    #     # print(x)
    #     parse_url(x)
    #     print(str(x) + '====' * 30)
    #     # break
    # for x in range(page_queue.qsize()):
    #     print(page_queue.get())
    write_cvs()
    for x in range(5):
        t = Procuder(page_queue, img_queue, data_queue, name=str(x) + 'Procuder')
        t.start()
    # for x in range(5):
    #     t = Consumer(page_queue, img_queue, name=str(x) + 'Consumer')
    #     t.start()
    for x in range(2):
        t = Consumer1(page_queue, img_queue, gLock, name=str(x) + 'Consumer1')
        t.start()

if __name__ == '__main__':
    main()
