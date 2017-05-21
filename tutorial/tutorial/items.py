# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FootballItem(scrapy.Item):
    title = scrapy.Field()
    sapo = scrapy.Field()
    content = scrapy.Field(required=False,)
    date = scrapy.Field()