# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    iname = scrapy.Field()
    iprice = scrapy.Field()
    # i_info = scrapy.Field()
    ireview = scrapy.Field()
    # i_data = scrapy.Field()
