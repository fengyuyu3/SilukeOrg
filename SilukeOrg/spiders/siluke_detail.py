# -*- coding: utf-8 -*-
import scrapy


class SilukeDetailSpider(scrapy.Spider):
    name = 'siluke_detail'
    allowed_domains = ['www.siluke.org']
    start_urls = ['http://www.siluke.org/']

    def parse(self, response):
        pass
    def parse_details(self, response):
        # item = SilukeorgItem()
        # item["type"] = response.xpath('//dt/a/text()').extract()[1]
        # item["name"] = response.xpath('//dt/a/text()').extract()[2]
        # base_url = response.xpath('//dt/a/@href').extract()[2]
        # contents = response.xpath('//td[@class="L"]/a/@href').extract()
        # for content in contents:
        #     item["url"] = base_url+content
        #     # print(item["url"])
        #     # self.r.lpush("siluke_detail", item["url"])
        #     yield item

        pass