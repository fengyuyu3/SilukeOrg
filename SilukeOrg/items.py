# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import time
from SilukeOrg.settings import SQL_DATETIME_FORMAT

class SilukeorgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()

class SilukeMySqlItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    word_num = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        #插入知乎question表的sql语句
        insert_sql = """
            insert into story_list(name, author, word_num,create_time,url
              ) VALUES ( %s, %s, %s, %s, %s)
              ON DUPLICATE KEY UPDATE name=VALUES(name)
        """

        create_time = datetime.datetime.fromtimestamp(time.time()).strftime(SQL_DATETIME_FORMAT)
        params = (
            self["name"], self["author"], self["word_num"], create_time, self["url"]
        )

        return insert_sql, params