# -*- coding: utf-8 -*-
import scrapy
import re

from images.items import ImagesItem


class VeerSpider(scrapy.Spider):
    name = 'veer'
    allowed_domains = ['*']

    def start_requests(self):
        keyword = self.settings['KEYWORD']
        pages = self.settings['PAGE']
        cookies = self.settings['VEER_COOKIES']
        basic_url = "https://www.veer.com/query/image/?phrase={keyword}&page={page}&perpage=100"
        for page in range(pages):
            url = basic_url.format(keyword=keyword, page=page)
            yield scrapy.Request(url, cookies=cookies, meta={"keyword": keyword})

    def parse(self, response):
        item = ImagesItem()
        img_urls_list = re.findall(r'src="(http.*?.jpg)"', response.text)  # 每页的图片链接列表
        item['image_urls'] = img_urls_list
        item['keyword'] = response.meta['keyword']
        yield item
