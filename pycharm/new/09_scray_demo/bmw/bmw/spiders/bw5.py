# -*- coding: utf-8 -*-
import scrapy

from bmw.items import BmwItem

class Bw5Spider(scrapy.Spider):
    name = 'bw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            category = uibox.xpath('./div[@class="uibox-title"]/a/text()').get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            #urls = list(map(lambda url:'https:'+url, urls))
            urls = list(map(lambda url : response.urljoin(url), urls))
            #print(urls)
            item = BmwItem(category=category, image_urls=urls)
            yield item
            # for url in urls:
            #     #url = 'https:'+url
            #     url = response.urljoin(url)
            #     print(url)

