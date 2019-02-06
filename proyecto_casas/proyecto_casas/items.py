# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemCasa(scrapy.Item):
    lugar = scrapy.Field()
    precio = scrapy.Field()
    unidades = scrapy.Field()
    pass
