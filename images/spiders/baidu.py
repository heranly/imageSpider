# -*- coding: utf-8 -*-
import re
from urllib.parse import quote
import time
import scrapy
from images.items import ImagesItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['*']

    def start_requests(self):
        keyword = self.settings['KEYWORD']
        pages = self.settings['PAGE']
        basic_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&word={keyword}&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&step_word={keyword}&pn={page}&rn=100&{timestamp}"
        for i in range(pages):
            timestamp = int(time.time() * 1000)
            url = basic_url.format(keyword=keyword, page=i * 30, timestamp=timestamp)
            yield scrapy.Request(url, meta={"keyword": keyword})

    def parse(self, response):
        item = ImagesItem()
        img_list = re.findall('"thumbURL":"(https?://.*?.jpe?g)"', response.text)  # 每页的图片链接列表
        item['image_urls'] = img_list
        item['keyword'] = response.meta['keyword']
        yield item
