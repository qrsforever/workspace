# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class CrawlListPipeline(object):
    def __init__(self, filepath):
        self.filepath = filepath

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('STOCK_LIST_FILE'))

    def process_item(self, item, spider):
        try:
            self.file.write('{0:^10}\t{1:^10}\n'.format(item['name'], item['code'], chr(12288)))
        except Exception as e:
             spider.logger.info("write error:", e)
        return item

    def open_spider(self, spider):
        try:
            self.file = open(self.filepath, "w+", encoding='utf-8')
            self.file.write('{0:^10}\t{1:^10}\n'.format('股票名', '股票码', chr(12288)))
        except Exception as e:
            spider.logger.info("open error:", e)

    def close_spider(self, spider):
        try:
            self.file.close()
        except:
            spider.logger.info("close error")


class CrawlInfoPipeline(object):
    def __init__(self, filepath):
        self.filepath = filepath

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('STOCK_INFO_FILE'))

    def process_item(self, item, spider):
        try:
            self.file.write('{0:^10}\t{1:^10}\n'.format(item['name'], item['code'], chr(12288)))
        except Exception as e:
            print("write error:", e)
        return item

    def open_spider(self, spider):
        try:
            self.file = open(self.filepath, "w+", encoding='utf-8')
            self.file.write('{0:^10}\t{1:^10}\n'.format('股票名', '股票码', chr(12288)))
        except Exception as e:
            print("open error:", e)

    def close_spider(self, spider):
        try:
            self.file.close()
        except:
            print("close error")
