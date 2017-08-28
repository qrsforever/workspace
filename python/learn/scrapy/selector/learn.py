#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scrapy.selector import Selector

body = '<html><body><span>good</span></body></html>'
txt = Selector(text=body).xpath('//span/text()').extract()
print(txt)
