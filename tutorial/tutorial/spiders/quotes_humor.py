import scrapy


class QuotesHumor(scrapy.Spider):
    name = 'quotes_humor'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        if self.tag is not None:
            url = url + 'tag/' + self.tag + '/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        quotes = response.css('div.quote .author + a::attr(href)').extract()
        for quote in quotes:
            url = response.urljoin(quote)
            yield scrapy.Request(url, callback=self.author_parse)
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)

    def author_parse(self, response):
        yield {
            'author_title': response.css('h3.author-title::text').extract_first(),
            'author_born_date': response.css('span.author-born-date::text').extract_first(),
            'author_born_location': response.css('span.author-born-location::text').extract_first()
        }