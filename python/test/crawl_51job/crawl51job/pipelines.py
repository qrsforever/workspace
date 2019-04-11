# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Crawl51JobPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['duty'])
        print(item['location'])
        print(item['sallary'])
        print(item['time'])
        return item
