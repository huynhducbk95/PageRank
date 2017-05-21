import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/']
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1',
    #         'http://quotes.toscrape.com/page/2',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        divs = response.css("div.quote")
        for div in divs:
            yield {
                'text': div.css('span.text::text').extract_first(),
                'author': div.css('small.author::text').extract_first(),
                'tags': div.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)