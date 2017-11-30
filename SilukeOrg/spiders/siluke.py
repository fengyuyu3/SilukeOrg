# -*- coding: utf-8 -*-
import scrapy
import redis
from SilukeOrg.items import SilukeMySqlItem

class SilukeSpider(scrapy.Spider):
    name = 'siluke'
    allowed_domains = ['www.siluke.org']
    # start_urls = ['http://www.siluke.org/top/lastupdate_1.html']
    start_urls = ['http://www.siluke.org/top/lastupdate_3479.html']
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    # r = redis.Redis(connection_pool=pool)

    def parse(self, response):
        item = SilukeMySqlItem()
        contents = response.xpath('//tr[@bgcolor="#FFFFFF"]')
        for content in contents:
            text = content.xpath("./td/a/@href").extract()[0]
            item["name"] = content.xpath("./td/a/text()").extract()[0]
            item["author"] = content.xpath('./td[@class="C"]/text()').extract()[0]
            item["word_num"] = content.xpath('./td[@class="R"]/text()').extract()[0]
            url = text+"index.html"
            item["url"] = url
            # self.r.lpush("siluke_detail", url)
            yield item
        page_next = len(response.xpath('//div[@class="pagelink"]/a[@class="next"]/@href').extract())
        if page_next == 1:
            page_next_url = response.xpath('//div[@class="pagelink"]/a[@class="next"]/@href').extract()[0]
            yield scrapy.Request(page_next_url, callback=self.parse)
        # yield scrapy.Request(url, callback=self.parse)
        # print(contents)
