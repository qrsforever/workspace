#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

## 数据库连接
# [mongod](https://docs.mongodb.com/manual/introduction/)
myclient = MongoClient('mongodb://localhost:27017/')

## 数据库删除
myclient.drop_database('learn')
mydb = myclient['learn']
mycol = mydb.mysite
doc = {"name":"lidong", "age":26, "address":"BJ"}
mycol.insert_one(doc)

## 数据库
alldbs = myclient.list_database_names()
alldbs
# Out[17]: ['admin', 'config', 'learn', 'local']

## 数据库集合
allcols = mydb.list_collection_names()
allcols
# Out[18]: ['mysite']

## 查询Doc
doc = mycol.find_one()
doc
# Out[26]: {'_id': ObjectId('5cb8835834d23a565a74ba2d'),
#  'name': 'lidong',
#  'age': 26,
#  'address': 'BJ'}


## 输入数据 (重复数据提示错误)
mydoc = [
        {"_id":"201904191800", "name":"AA", "age":20, "address":"SH"},
        {"_id":"201904191801", "name":"BB", "age":23, "address":"SZ"},
        {"_id":"201904191802", "name":"CC", "age":24, "address":"ZZ"}
        ]
mycol.insert_many(mydoc)
docs = mycol.find()
for each in docs:
    print(each)
