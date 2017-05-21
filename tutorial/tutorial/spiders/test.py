from scrapy import Selector
from scrapy.http import HtmlResponse
import scrapy


class Test(scrapy.Item):
    name = scrapy.Field(default='test', type=str, required=True)