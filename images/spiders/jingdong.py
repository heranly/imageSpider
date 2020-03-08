# -*- coding: utf-8 -*-
import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['*']
    start_urls = ['http://*/']

    def parse(self, response):
        print("京东渠道待续")
        pass
