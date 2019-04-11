# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline

class CrawrcoursePipeline(FilesPipeline):

    def open_spider(self, spider):
        spider.log("open_spider")
        pass

    def close_spider(self, spider):
        spider.log("close_spider")
        pass

    def file_path(self, request, response=None, info=None):
        filename = request.url.split('/')[-1]
        return '%s' % (filename)

    def process_item(self, item, spider):
        spider.log("process_item:")
        return item
