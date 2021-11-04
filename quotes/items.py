# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:

    quote_text=scrapy.Field()
    quote_authors=scrapy.Field()
    quote_tags=scrapy.Field()


