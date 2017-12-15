# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class DatasetPipeline(FilesPipeline):

    # 基类实现
    # def process_item(self, item, spider):
    #     return item

    # 如果item字典中有file_urls, 该函数不用重写
    def get_media_requests(self, item, info):
       # 默认files_urls_field: file_urls
       #  return [Request(x) for x in item.get(self.files_urls_field, [])]

       # DatasetItem里面的file_url并不是dict类型 
       return [Request(item.get('file_url', []))]

    # 如果item字典中有files, 该函数不用重写
    def item_completed(self, results, item, info):
        # 默认files_result_field: files
        #  if isinstance(item, dict) or self.files_result_field in item.fields:
        #       item[self.files_result_field] = [x for ok, x in results if ok]
        #  return item

        # DatasetItem里面的file_url并不是dict类型 
        ok, x = results[0]
        if ok:
            item['file'] = x['path']
        return item

    # 重写file_path, 下载后的文件名从url中解析出
    def file_path(self, request, response=None, info=None):
         
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        return url.split("/")[-1] 
