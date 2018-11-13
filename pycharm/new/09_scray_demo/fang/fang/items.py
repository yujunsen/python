# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()   #省份
    city = scrapy.Field()       #城市
    name = scrapy.Field()       #小区名字
    price = scrapy.Field()      #价格
    rooms = scrapy.Field()      #几居
    area = scrapy.Field()      #面积
    address = scrapy.Field()      #地址
    district = scrapy.Field()      #行政区
    sale = scrapy.Field()      #死否出售
    origin_url = scrapy.Field() #房天下详情url
    id = scrapy.Field()

class EsfHouseItem(scrapy.Item):
    province = scrapy.Field()   #省份
    city = scrapy.Field()       #城市
    name = scrapy.Field()       #小区名字
    price = scrapy.Field()      #总价
    unit = scrapy.Field()       #单价
    rooms = scrapy.Field()      #几室几厅
    floor = scrapy.Field()      #层
    toward = scrapy.Field()     #朝向
    year= scrapy.Field()        #年代
    area = scrapy.Field()      #面积
    address = scrapy.Field()      #地址
    origin_url = scrapy.Field() #房天下详情url
    id = scrapy.Field()
    # district = scrapy.Field()      #行政区
    # sale = scrapy.Field()      #死否出售
