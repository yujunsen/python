import requests
from lxml import etree
from urllib import request
import os
import re
from  queue import  Queue
import threading

class Procuder(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/'
    }
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):

        repsonse = requests.get(url, headers=self.headers)
        #print(repsonse.text)
        html = etree.HTML(repsonse.text)
        imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for img in imgs:
            img_url = img.get('data-original')
            #print(img_url)
            alt = img.get('alt')
            alt = re.sub(r'[\?\.。！，!\ *]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            print(filename)
            self.img_queue.put((img_url, filename))

class Consumer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/'
    }
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, 'img/' + filename)
            print(filename)

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%s'  %x
        page_queue.put(url)
    # print(page_queue.qsize())
    for x in range(5):
        t = Procuder(page_queue, img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()

if __name__ == '__main__':
    main()