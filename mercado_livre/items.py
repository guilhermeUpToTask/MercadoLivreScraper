# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoLivreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
          
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    rating_number = scrapy.Field()
    rating_amount = scrapy.Field()
    pass
