# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsspiderItem(scrapy.Item):
    title = scrapy.Field()          
    time = scrapy.Field()      
    origin = scrapy.Field()  
    origin_url = scrapy.Field() 
    detail = scrapy.Field()
    url = scrapy.Field()
#    abstract = scrapy.Field()

class NewsAbsspiderItem(scrapy.Item):
    title = scrapy.Field()
    source= scrapy.Field() 
    time2 = scrapy.Field() 
    abstract = scrapy.Field()
    url = scrapy.Field()
    
     
