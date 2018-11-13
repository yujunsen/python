# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
# from  scrapy.http.response.html import HtmlResponse
# from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    def parse(self, response):
        print('==' * 30)

        duanzidivs = response.xpath('//div[@id="content-left"]/div')

        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath('.//h2/text()').get().strip()
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()
            content = ''.join(content).strip()
            #print(content)
            #dusnzi = {'author':author, 'content':content}
            item = QsbkItem(author=author, content=content)
            yield item
            #print('--'*30)
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if not next_url:
            print('结束')
            return
        else:
            yield scrapy.Request( 'https://www.qiushibaike.com' + next_url, callback=self.parse)
        print('==' * 30)
"""
response     scrapy.http.response.html.HtmlResponse
contenLeft  scrapy.selector.unified.SelectorList
"""