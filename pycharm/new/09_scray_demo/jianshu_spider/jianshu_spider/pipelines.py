# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuSpiderPipeline(object):

    def __init__(self):

        dbparams = {
            'host': '192.168.1.150',
            'port': 3306,
            'user': 'root',
            'password':'y',
            'database':'jianshu',
            'charset':'utf8'
        }

        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def open_spider(self,spider):
        pass


    def process_item(self, item, spider):
        #return item
        self.cursor.execute(self.sql, (item['title'], item['context'], item['article_id'],
                                       item['author'], item['avator'], item['pub_time'], item['origin_url']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
             insert into article(id, title, context, article_id, author, avator, pub_time, origin_url) values(null, %s, %s,
             %s, %s, %s, %s, %s)
            """
            return self._sql
        return self._sql


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '192.168.1.150',
            'port': 3306,
            'user': 'root',
            'password': 'y',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
              insert into article(id, title, context, article_id, author, avator, pub_time, origin_url,
              read_count, comment_count, word_count, like_count, subjects) values(null, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['title'], item['context'], item['article_id'],
                                  item['author'], item['avator'], item['pub_time'], item['origin_url'],
                                  item['read_count'], item['comment_count'], item['word_count'], item['like_count'],
                                  item['subjects']))

    def handle_error(self, error, item, spider):
        print('='+ 'error' + '='*10)
        print(error)
        print('='+ 'error' + '='*10)

