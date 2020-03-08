# -*- coding: utf-8 -*-
import re
from urllib.parse import quote
import time
import scrapy
from images.items import ImagesItem


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['*']

    def start_requests(self):
        keyword = self.settings['KEYWORD']
        pages = self.settings['PAGE']
        basic_url = "https://www.google.com/search?ei=qwukXMmKN8nKmAXfg7w4&hl=zh-CN&yv=3&tbm=isch&q={keyword}&vet=10ahUKEwiJjN-Y4rLhAhVJJaYKHd8BDwcQuT0INSgB.qwukXMmKN8nKmAXfg7w4.i&ved=0ahUKEwiJjN-Y4rLhAhVJJaYKHd8BDwcQuT0INSgB&ijn={page}&start={number}&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc"
        for page in range(pages):
            url = basic_url.format(keyword=keyword, page=page, number=page * 100)
            yield scrapy.Request(url, meta={"keyword": keyword})

    def parse(self, response):
        keyword = response.meta['keyword']
        item = ImagesItem()
        img_lists = re.findall('"ou":"(http.?://.*?)","ow":', response.text)
        for index, img_url in enumerate(img_lists):
            if "\\u003d" in img_url:
                img_lists[index] = img_lists[index].replace('\\u003d', '=')
            if "\\u0026" in img_url:
                img_lists[index] = img_lists[index].replace('\\u0026', '&')

        item['image_urls'] = img_lists
        item['keyword'] = keyword
        yield item
