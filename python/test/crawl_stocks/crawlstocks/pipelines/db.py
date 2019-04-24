#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pymongo import MongoClient

class GuchengCodesPipeline(object):
    def __init__(self, host, name, table):
        self.mongo = MongoClient(host)
        self.db = self.mongo[name]
        self.table = self.db[table]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('DB_HOST'),
                crawler.settings.get('DB_NAME'),
                crawler.settings.get('DB_CODES_TABLE_NAME'))

    def process_item(self, item, spider):
        try:
            # self.table.insert_one({'_id': item['code'], 'name': item['name'], 'code':
                # item['code']})
            self.table.update_one({'_id': item['code']},
               {'$set': {
                   '_id': item['code'],
                   'name': item['name'],
                   'code':item['code']}},
               upsert = True)
        except Exception as e:
             spider.logger.info("write error:", e)
        return item

    def open_spider(self, spider):
        try:
            pass
        except Exception as e:
            spider.logger.info("open error:", e)

    def close_spider(self, spider):
        try:
            self.mongo.close()
        except:
            spider.logger.info("close error")


class QuotesCHDDataPipeline(object):
    def __init__(self, host, name, table):
        self.mongo = MongoClient(host)
        self.db = self.mongo[name]
        self.table = self.db[table]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('DB_HOST'),
                crawler.settings.get('DB_NAME'),
                crawler.settings.get('DB_CHDDATA_TABLE_NAME'))

    def process_item(self, item, spider):
        try:
            key = item['code'] + '_' + item['date']
            self.table.update_one({'_id': key},
               {'$set': {
                   '_id': key,
                   'name': item['name'],
                   'code':item['code'],
                   'date': datetime.strptime(item['date'], '%Y-%m-%d'),
                   'tclose': item['tclose'],
                   'high': item['high'],
                   'low': item['low'],
                   'topen': item['topen'],
                   'lclose': item['lclose'],
                   'chg': item['chg'],
                   'pchg': item['pchg'],
                   'turnover': item['turnover'],
                   'voturnover': item['voturnover'],
                   'vaturnover': item['vaturnover'],
                   'tcap': item['tcap'],
                   'mcap': item['mcap']
                   }},
               upsert = True)
        except Exception as e:
             spider.logger.info("write error:", e)
        return item

    def open_spider(self, spider):
        try:
            pass
        except Exception as e:
            spider.logger.info("open error:", e)

    def close_spider(self, spider):
        try:
            self.mongo.close()
        except:
            spider.logger.info("close error")
