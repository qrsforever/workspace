# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlstocksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StockCodeItem(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()

class StockInfoItem(scrapy.Item):
    name = scrapy.Field()            # 股票名称
    code = scrapy.Field()            # 股票代码
    report_date = scrapy.Field()     # 截止日期
    earning_ps = scrapy.Field()      # 每股收益（元）
    net_assets_ps = scrapy.Field()   # 每股净资产（元）
    net_profit = scrapy.Field()      # 净利润（亿元）
    net_asset = scrapy.Field()       # 净资产（亿元）
    gross_sales = scrapy.Field()     # 营业收入（亿元）
    ROE = scrapy.Field()             # 净资产收益率（%）
    PER = scrapy.Field()             # 市盈率
    PBR = scrapy.Field()             # 市净率
    cash_flow_ps = scrapy.Field()    # 每股现金流净额（元）
    gross_profit = scrapy.Field()    # 销售毛利率（%）
