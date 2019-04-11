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
        self.fmt = ""
        for i in range(13):
            self.fmt = self.fmt + '{%d:^10}\t' % i
        self.fmt = self.fmt + '\n'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('STOCK_INFO_FILE'))

    def process_item(self, item, spider):
        try:
            self.file.write(self.fmt.format(
                item['name'],
                item['code'],
                item['report_date'],
                item['earning_ps'],
                item['net_assets_ps'],
                item['net_profit'],
                item['net_asset'],
                item['gross_sales'],
                item['ROE'],
                item['PER'],
                item['PBR'],
                item['cash_flow_ps'],
                item['gross_profit'],
                chr(12288)))
        except Exception as e:
            print("write error:", e)
        return item

    def open_spider(self, spider):
        titles = (
                '股票名称',
                '股票代码',
                '截止日期',
                '每股收益（元）',
                '每股净资产（元）',
                '净利润（亿元）',
                '净资产（亿元）',
                '营业收入（亿元）',
                '净资产收益率（%）',
                '市盈率',
                '市净率',
                '每股现金流净额（元）',
                '销售毛利率（%）'
                )
        try:
            self.file = open(self.filepath, "w+", encoding='utf-8')
            for each in titles:
                self.file.write('{0} '.format(each, chr(12288)))
            self.file.write('\n')
        except Exception as e:
            print("open error:", e)

    def close_spider(self, spider):
        try:
            self.file.close()
        except:
            print("close error")
