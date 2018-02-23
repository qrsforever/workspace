# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

    # This method is called when the spider is opened.
    def open_spider(self, spider):
        pass

    # This method is called when the spider is closed.
    def close_spider(self, spider):
        pass
