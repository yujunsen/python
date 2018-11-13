# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    title = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    work_year = scrapy.Field()
    education = scrapy.Field()

