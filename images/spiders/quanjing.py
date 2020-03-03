# -*- coding: utf-8 -*-
import time
import re
import scrapy

from images.items import ImagesItem


class QuanjingSpider(scrapy.Spider):
    name = 'quanjing'
    allowed_domains = ['*']

    def start_requests(self):
        keyword = self.settings['KEYWORD']
        pages = self.settings['PAGE']
        headers = self.settings['QUANJING_HEADERS']
        basic_url = "https://www.quanjing.com/Handler/SearchUrl.ashx?t=2151&callback=searchresult&q={keyword}&stype=1&pagesize=100&pagenum={page}&imageType=2&imageColor=&brand=&imageSType=&fr=1&sortFlag=1&imageUType=&btype=&authid=&_={timestamp}"

        headers["Referer"] = "https://www.quanjing.com/search.aspx?q={keyword}".format(keyword=keyword)

        for page in range(1,pages+1):
            timestamp = int(time.time()*1000)
            url = basic_url.format(keyword=keyword,page=page,timestamp=timestamp)
            yield scrapy.Request(url,headers=headers,meta={"keyword":keyword})

    def parse(self, response):
        item = ImagesItem()
        img_urls_list = re.findall(r'"imgurl":"(.*?)"',response.text)  # 每页的图片链接列表
        item['image_urls'] = img_urls_list
        item['keyword'] = response.meta['keyword']
        yield item



