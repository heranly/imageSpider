# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class ImagesItem(Item):
    # define the fields for your item here like:
    keyword = Field()
    image_urls = Field()
    images = Field()
    image_paths = Field()

    def __repr__(self):
        return "==========ImagesItem storing==========="

