# -*- coding: utf-8 -*-
import re
from urllib.parse import quote
import time
import scrapy
from images.items import ImagesItem


class VcgSpider(scrapy.Spider):
    name = 'vcg'
    allowed_domains = ['*']

    def start_requests(self):
        keyword = self.settings['KEYWORD']
        pages = self.settings['PAGE']
        basic_url = "https://www.vcg.com/api/common/searchImage?assetFamily=2&page={page}&phrase={keyword}&keyword={keyword}&utm_source=baidu&utm_medium=cpc&utm_campaign=%E5%9B%BE%E7%89%87-PC&utm_content=%E5%9B%BE%E7%89%8710&utm_term=%E7%BD%91%E7%AB%99%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87"
        for page in range(pages):
            url = basic_url.format(keyword=keyword, page=page)
            yield scrapy.Request(url, meta={"keyword": keyword})

    def parse(self, response):
        item = ImagesItem()
        img_urls = re.findall('"url800":"(//.*?.jpg)"', response.text)  # 每一页的所有图片链接
        image_urls = ["https:" + url for url in img_urls]
        item['image_urls'] = image_urls
        item['keyword'] = response.meta['keyword']
        yield item
