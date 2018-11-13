# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101270100/h_101270100/?query=pyhon&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=pyhon&page=\d'), follow=False),
        Rule(LinkExtractor(allow=r'.+?job_detail/.+\.html'), callback='parse_data', follow=False),
    )

    def parse_page(self, response):
        #print(response.url)
        pass




    def parse_data(self, response):

        title = response.xpath('//div[@class="name"]/h1/text()').get()
        salary = response.xpath('//span[@class="badge"]/text()').get().strip()
        job_info = response.xpath('//div[@class="job-primary detail-box"]/div[2]/p/text()').getall()
        company = response.xpath('//h3[@class="name"]//text()').get()
        city = job_info[0].split('：')[1]
        work_year = job_info[1].split('：')[1]
        education = job_info[2].split('：')[1]
        item = BossItem(title=title, salary=salary, company=company, city=city, work_year=work_year,
                        education=education)
        yield item
