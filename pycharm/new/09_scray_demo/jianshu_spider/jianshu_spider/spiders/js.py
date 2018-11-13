# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').get()
        author = response.xpath('//div[@class="info"]/span//text()').get()
        avator = response.xpath('//div[@class="author"]//img/@src').get().split('?')[0]
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace('*','')
        context = response.xpath(' //div[@class="show-content-free"]').get()
        origin_url = response.url
        read_count = response.xpath('//span[@class="views-count"]/text()').get().split()[1]
        comment_count = response.xpath('//span[@class="comments-count"]/text()').get().split()[1]
        word_count = response.xpath('//span[@class="wordage"]/text()').get().split()[1]
        like_count = response.xpath('//span[@class="likes-count"]/text()').get().split()[1]
        subjects = ','.join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())
        url = response.url
        url = url.split("?")[0]
        article_id = url.split('/')[-1]
        item = JianshuSpiderItem(origin_url = origin_url,
                                 title=title, author=author,
                                 avator=avator, pub_time=pub_time,
                                 context=context,article_id=article_id,
                                 read_count=read_count, comment_count=comment_count,
                                 word_count=word_count, like_count=like_count, subjects=subjects)

        yield item

