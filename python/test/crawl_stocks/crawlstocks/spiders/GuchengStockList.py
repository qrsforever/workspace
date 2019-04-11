# -*- coding: utf-8 -*-
import scrapy
import re

from crawlstocks.items import StockCodeItem

re_name_code = re.compile(r'(?P<name>.+)\((?P<code>[0369]\d{5})\)')

class GuchengstocklistSpider(scrapy.Spider):
    name = 'GuchengStockList'
    allowed_domains = ['hq.gucheng.com']
    start_urls = ['https://hq.gucheng.com/gpdmylb.html']

    custom_settings = {
            'ITEM_PIPELINES' : {'crawlstocks.pipelines.CrawlListPipeline':200}
            }

    def parse(self, response):
        item = StockCodeItem()
        for stock in response.xpath('//section[has-class("stockTable")]/a/text()').getall():
            res = re_name_code.search(stock)
            if res is None:
                continue
            # 股票名称 并去除名字中空格
            item['name'] = re.sub(r'\s+', '', res.groupdict()['name'])
            # 股票代码
            item['code'] = res.groupdict()['code']
            yield item
