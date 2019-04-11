# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuchengstockinfoSpider(CrawlSpider):
    name = 'GuchengStockInfo'
    allowed_domains = ['hq.gucheng.com']
    start_urls = ['https://hq.gucheng.com/gpdmylb.html']

    custom_settings = {
            'ITEM_PIPELINES' : {'crawlstocks.pipelines.CrawlInfoPipeline':200}
            }

    # 提取需要请求的链接 (SZ SH)
    rules = (
        Rule(LinkExtractor(
            allow=('hq.gucheng.com/[sS][hzHZ]90092\d{1}/'),
            restrict_xpaths=('//section[@class="stockTable"]'),
            ),
            callback='parse_item',
            process_links='deal_links',
            process_request='deal_request',
            follow=True),
    )

    def deal_request(self, request):
        return request

    def deal_links(self, links):
        # 链接追加财务分析项
        for each in links:
           each.url = os.path.join(each.url, "caiwufenxi")
        return links
        

    def parse_item(self, response):
        self.logger.info(response.url)

