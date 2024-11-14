# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    level = scrapy.Field()
    description = scrapy.Field()
    published_date = scrapy.Field()
    scraping_date = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    link = scrapy.Field()
    pass
