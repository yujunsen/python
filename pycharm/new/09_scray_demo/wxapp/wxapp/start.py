from scrapy import cmdline

#scrapy genspider -t crawl wxapp_spider

cmdline.execute('scrapy crawl wxapp_spider'.split())
#print('scrapy crawl qsbk_spider'.split())