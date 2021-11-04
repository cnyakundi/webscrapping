import scrapy
from ..items import QuotesItem


class QuotesSpiderSpider(scrapy.Spider):
    name = 'spider'
    page_number=2
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotesItem()
        quotes = response.css('div.quote')

        for quote in quotes:
            quote_text = quote.css("span.text::text").extract()
            quote_authors = quote.css(".author::text").extract()
            quote_tags = quote.css(".tag::text").extract()

            items['quote_text'] = quote_text
            items['quote_authors'] = quote_authors
            items['quote_tags'] = quote_tags

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
