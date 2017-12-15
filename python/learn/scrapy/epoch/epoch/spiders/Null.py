# -*- coding: utf-8 -*-
import scrapy


class NullSpider(scrapy.Spider):
    name = 'Null'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost/']

    def parse(self, response):
        pass
