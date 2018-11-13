# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem, EsfHouseItem

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['http://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            province_td = tds[0]
            province_text = province_td.xpath('.//text()').get()
            province_text = re.sub(r'\s', '', province_text)
            if province_text:
               province = province_text
            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()
                city_url = re.sub(r'(com/)$|(com$)', 'com/', city_url)
                #print('省份 %s 城市 %s 城市链接 %s' %(province, city, city_url))
                if province == '重庆':
                    if city != '重庆':
                        city_url = re.sub(r'cq', '', city_url)

                #构建新房链接
                if province == 	'其它':
                    break
                    # if city == '香港':
                    #     newhouse_url = None
                    #     esf_url = 'http://hk.esf.fang.com/'
                    # else:
                    #     newhouse_url = city_url + 'm1/'
                    #     esf_url = city_url + 'm2/'


                url_module = city_url.split('.')
                url_module.insert(1, 'newhouse')
                newhouse_url = '.'.join(url_module) + 'house/s/'

                #构建二手房链接

                url_module = city_url.split('.')
                url_module.insert(1, 'esf')
                esf_url = '.'.join(url_module)
                if city == '北京':
                    esf_url = 'http://esf.fang.com/'
                    newhouse_url = 'http://esf.fang.com/'
               # print(province, city, newhouse_url, esf_url)
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info":(province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esfhouse, meta={"info":(province, city)})






    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        #print(province + '==' +  city)

        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            if not name:
                continue
            name = re.sub(r'\s', '', name)
            house_type_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            house_type_list = list(map(lambda x:re.sub(r'\s', '', x), house_type_list))
            rooms = list(filter(lambda x : x.endswith('居'), house_type_list))
            area = ''.join(li.xpath('.//div[contains(@class, "house_type")]/text()').getall())
            area = re.sub(r'[\s/－]', '', area)

            district = li.xpath('.//div[@class="address"]/a//text()').getall()
           # district = list(map(lambda x:re.sub(r'[\s\[\]]', '', x), district))
            district = ''.join(district)
            district = re.search('\[(.+)\].*', district).group(1)
            address = li.xpath('.//div[@class="address"]/a/@title').get()
            sale = li.xpath('.//div[contains(@class, "fangyuan")]/span/text()').get()
            price = li.xpath('.//div[@class="nhouse_price"]//text()').getall()
            price = re.sub(r'\s|广告', '', ''.join(price))
            origin_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()


            item = NewHouseItem(city=city, name=name, price=price,rooms=rooms, area=area,
                               address=address, district=district, sale=sale, origin_url=origin_url)
            item['id'] = 1
            yield item

        next_url = response.xpath('//a[@class="next"]/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, meta={"info":(province, city)})

    def parse_esfhouse(self, response):
        province, city = response.meta.get('info')
        item = EsfHouseItem(province=province, city=city)
        #print(province + '==' +  city)
        #a = response.xpath('//div[contains(@class, "shop_list")]/dl//a/@title').get()
        #print(a)
        dls = response.xpath('//div[contains(@class, "shop_list")]/dl')
        for index, dl in enumerate(dls):
            name = dl.xpath('.//p[@class="add_shop"]/a/@title').get()
            if not name:
                continue
            item['name'] = name
            tel_shop = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            tel_shop = list(map(lambda x:re.sub(r'\s', '', x), tel_shop))
            for tel in tel_shop:
                if '厅' in tel:
                    item['rooms'] = tel
                elif '层' in tel:
                    item['floor'] = tel
                elif '㎡' in tel:
                    item['area'] = tel
                elif '向' in tel:
                    item['toward'] = tel
                elif '年' in tel:
                    item['year'] = tel.replace('年建', '')
            address = dl.xpath('.//p[@class="add_shop"]/span/text()').get()
            item['address'] = address
            # rooms = tel_shop[0]
            # area = tel_shop[1]
            # floor = tel_shop[2]
            # toward = tel_shop[3]
            # if '向' not in toward:
            #     toward = None
            #     tel_shop[4] = tel_shop[3]
            #year = tel_shop[4]
            price = dl.xpath('.//span[@class="red"]//text()').getall()
            unit = dl.xpath('.//dd/span[2]/text()').get()
            item['price'] = ''.join(price)
            item['unit'] = unit
            origin_url = dl.xpath('.//h4/a/@href').get()
            origin_url = response.urljoin(origin_url)
            item['origin_url'] = origin_url
            #print(origin_url)
            item['id'] = 2
            yield item
        next_name = response.xpath('//div[@class="page_al"]/p[last()-2]/a/text()').get()
        if next_name == '下一页':

            next_url = response.xpath('//div[@class="page_al"]/p[last()-2]/a/@href').get()
            next_url = response.urljoin(next_url)
            print(next_name, next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_esfhouse, meta={"info":(province, city)})
        """
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
        """


