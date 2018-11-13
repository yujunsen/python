# -*- coding: utf-8 -*-
import scrapy
import json

class HttpipSpider(scrapy.Spider):
    name = 'httpip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        print(origin)
