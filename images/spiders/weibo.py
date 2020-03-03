# -*- coding: utf-8 -*-
import scrapy
import re

from images.items import ImagesItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['*']
    num = 0

    def start_requests(self):
        cookies = self.settings['WEIBO_COOKIES']
        keyword = self.settings['KEYWORD']
        basic_url = "https://weibo.cn/find/user?keyword={keyword}&suser=2".format(keyword=keyword)
        yield scrapy.Request(basic_url,cookies=cookies,meta={'cookies':cookies,"keyword":keyword})


    def parse(self, response):
        #搜索结果第一条链接
        cookies=response.meta['cookies']
        keyword=response.meta['keyword']
        search_keyword_url = response.xpath('//table[1]//tr/td/a/@href').extract_first()
        user_weibo_id = search_keyword_url.split("/")[-1]
        photos_page_url = "https://weibo.cn/{}/photo?tf=6_008".format(user_weibo_id)
        yield scrapy.Request(photos_page_url,cookies=cookies,meta={'cookies':cookies,"keyword":keyword},callback=self.parse_photos)


    def parse_photos(self, response):
        cookies=response.meta['cookies']
        keyword=response.meta['keyword']
        photos_list = response.xpath('//div[@class="c"]//div[@class="c"]/a/@href').extract()
        for ul in photos_list:
            url = "https://weibo.cn"+ul
            yield scrapy.Request(url,cookies=cookies,callback=self.parse_item,meta={'cookies':cookies,"keyword":keyword})


    def parse_item(self,response):
        cookies=response.meta['cookies']
        keyword=response.meta['keyword']
        pages = self.settings['PAGE']
        self.num += 1
        item = ImagesItem()
        pic_urls = response.xpath('//div[@class="c"]/a/img/@src').extract()
        item['image_urls'] = [url.replace("wap180","large") for url in pic_urls]
        item['keyword'] = keyword
        yield item

        if self.num < pages:
            next_page_url = response.xpath('//div[@id="pagelist"]/form/div/a/@href').extract_first()
            if next_page_url:
                yield scrapy.Request(next_page_url,callback=self.parse_item,cookies=cookies,meta={'cookies':cookies,"keyword":keyword})



