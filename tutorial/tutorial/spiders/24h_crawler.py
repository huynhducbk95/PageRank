import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Compose
from scrapy.loader import ItemLoader
from tutorial.items import FootballItem
import re
import json


def add_str(str):
    return str + '____'


class FootballLoader(ItemLoader):
    default_item_class = FootballItem
    default_output_processor = Join()
    title_in = MapCompose(unicode.strip, unicode.upper, add_str)
    sapo_in = MapCompose(unicode.strip, unicode.upper, add_str)
    content_in = MapCompose(unicode.strip, unicode.upper, add_str)
    date_in = MapCompose(unicode.strip, unicode.upper, add_str)


class FootballSpider(scrapy.Spider):
    name = 'football'
    # allowed_domains = ['http://www.24h.com.vn']
    start_urls = [
        'http://www.24h.com.vn/'
    ]

    linkPatterns = re.compile("/bong-da/")
    crawled_links = []

    def parse(self, response):
        all_links = response.xpath('//a/@href').extract()
        for link in all_links:
            if self.linkPatterns.match(link) and not link in self.crawled_links:
                self.crawled_links.append(link)
                url = response.urljoin(link)
                yield scrapy.Request(url=url, callback=self.parse_football)

    def parse_football(self, response):
        loader = FootballLoader(response=response)
        # content_loader = loader.nested_xpath('//div[@class="div-baiviet"]')
        loader.add_xpath('title', '//div[@class="div-baiviet"]/h1[@class="baiviet-title"]/text()')
        loader.add_xpath('sapo', '//div[@class="div-baiviet"]/p[@class="baiviet-sapo"]/text()')
        loader.add_xpath('date', '//div[@class="div-baiviet"]/div[@class="baiviet-ngay"]/text()')
        yield loader.load_item()
        all_links = response.xpath('//a/@href').extract()
        for link in all_links:
            if self.linkPatterns.match(link) and not link in self.crawled_links:
                self.crawled_links.append(link)
                url = response.urljoin(link)
                yield scrapy.Request(url=url, callback=self.parse_football)
