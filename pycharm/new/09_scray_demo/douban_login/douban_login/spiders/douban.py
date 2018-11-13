# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image

#data = {"email": "970138074@qq.com", "password": "pythonspider"}

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url = 'https://accounts.douban.com/login'

    def parse(self, response):
        formdata = {
            #'source': 'index_nav',
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form_email': '970138074@qq.com',
            'form_password': 'pythonspider',
            # 'captcha-solution': 'dirty',
            # 'captcha-id': 'zCagtRswxrhu37K85KhYYYOQ:en'
            'remember': 'on',
            'login': '登录'
        }
        captcha_img = response.css('img#captcha_image::attr(src)').get()
        captcha_id = response.xpath('//div[@class="captcha_block"]/input/@value').get()

        if  captcha_img:
            captcha = self.regonize_captcha(captcha_img)
            formdata['captcha-solution'] = captcha
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url,formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            print('登陆成功')
            profile_url = 'https://www.douban.com/people/97956064/'
            yield scrapy.FormRequest(url=profile_url, callback=self.parse_profile)
        else:
            print('登陆失败')

    def parse_profile(self, response):
        if response.url == 'https://www.douban.com/people/97956064/':
            print('进入个人中心')
            ck = response.xpath("//input[@name='ck']/@value").get()
            signature = '有没有'
            formdata = {
                'ck':ck,
                'signature':signature
            }
            yield  scrapy.FormRequest('https://www.douban.com/j/people/97956064/edit_signature', formdata=formdata)
        else:
            print('没有进入个人中心')
    def regonize_captcha(self, img_url):
        request.urlretrieve(img_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input("请输入验证码:")
        #image.close()
        #print(captcha)

        return  captcha
"""
ck: ywMr
signature: saddsa
"""