# -*- coding: utf-8 -*-
import scrapy
from SilukeOrg.items import SilukeorgItem
from scrapy_redis.spiders import RedisSpider

class SilukeDetailSpider(RedisSpider):
    name = 'siluke_detail'
    allowed_domains = ['www.siluke.org']
    redis_key = "siluke_detail:start_urls"
    # start_urls = ['http://www.siluke.org/book/83682/index.html']

    def parse(self, response):
        self.item = SilukeorgItem()
        self.item["type"] = response.xpath('//dt/a/text()').extract()[1]
        self.item["name"] = response.xpath('//dt/a/text()').extract()[2]
        base_url = response.xpath('//dt/a/@href').extract()[2]
        url = base_url+response.xpath('//td[@class="L"]/a/@href').extract()[0]
        yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        text = ""
        title = response.xpath('//dd/h1/text()').extract()[0]+"/n"
        contents = response.xpath('//dd[@id="contents"]/text()').extract()
        for content in contents:
            text = text + content
        self.item["content"] = title+text
        yield self.item
        next_url = response.xpath('//dd[@id="footlink"]/a/@href').extract()[2]
        base_url = response.xpath('//dd[@id="footlink"]/a/@href').extract()[1]
        if next_url != base_url:
            yield scrapy.Request(next_url, callback=self.parse_details)


