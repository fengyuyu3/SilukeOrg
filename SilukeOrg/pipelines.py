# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
import copy

class SilukeorgPipeline(object):
    def process_item(self, item, spider):
        # file_dir = os.path.dirname(os.path.abspath(__file__))+"\\"+item["type"]
        # if not os.path.exists(file_dir):
        #     os.makedirs(file_dir)
        file_dir = os.path.dirname(os.path.abspath(__file__))
        filename = item["name"]+".txt"
        f = open(file_dir+"\\"+filename, "ab")
        content = str(item["content"])
        f.write(content.encode("utf-8"))
        f.close()
        return item

class SilukeorgMySqlPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        asynItem = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self.do_insert, asynItem)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
