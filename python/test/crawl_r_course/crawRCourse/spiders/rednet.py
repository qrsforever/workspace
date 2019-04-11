# -*- coding: utf-8 -*-
import scrapy

#  from scrapy.selector import Selector
from ..items import RCourseFileItem

class RednetSpider(scrapy.Spider):
    name = 'rednet'
    allowed_domains = ['www.bendixcarstensen.com/SDC/R-course/']
    start_urls = ['http://www.bendixcarstensen.com/SDC/R-course//']

    def parse(self, response):
        for href in response.css('ul li a::attr(href)'):
            item = RCourseFileItem()
            item['url'] = response.urljoin(href.get())
            yield item
