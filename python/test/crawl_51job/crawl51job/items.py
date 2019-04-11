# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawl51JobItem(scrapy.Item):
    name = scrapy.Field()     # 公司名称
    duty = scrapy.Field()     # 工作的标题
    location = scrapy.Field() # 公司地址
    sallary = scrapy.Field()  # 薪水
    time = scrapy.Field()     # 时间
