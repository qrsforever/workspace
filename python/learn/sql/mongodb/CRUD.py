#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pprint import pprint
from datetime import datetime
from pymongo import MongoClient

##############
# <codecell> #
##############
# client CRUD
mymongo = MongoClient('mongodb://localhost:27017/')
mymongo.drop_database('learn_crud')
mymongo.list_database_names()
mydb = mymongo.learn_crud
mycol = mydb.mycol

#####################################################################################
## [insert](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/)

##############
# <codecell> #
##############
## Create
# if not exits, then create
# run twice, add twice, _id is unique, but not user
# if _id is same, then insert to update operate
mycol.insert_one({'user': 'lidong', 'passwd': '123456'})
mycol.insert_many([
    {'user':'aaa', 'passwd':'111', 'age':10},
    {'user':'bbb', 'passwd':'222', 'age':20},
    {'_id':'000001', 'user':'ccc', 'passwd':'333', 'age':30},
    ])
# below error: _id is duplicate
try:
    mycol.insert_one({'_id': '000001', 'user': 'lidong', 'passwd': '123456'})
except Exception as e:
    print(e)

#####################################################################################
## [find](https://docs.mongodb.com/manual/reference/method/db.collection.find/)

##############
# <codecell> #
##############
## Read
# db.collection.find(query, projection)

### query parameters

##############
# <codecell> #
##############

type(mycol.find())
# Out[60]: pymongo.cursor.Cursor

##############
# <codecell> #
##############
# -1 is descending
for each in mycol.find().sort('age', -1):
    print(each)

##############
# <codecell> #
##############

for each in mycol.find({'_id':'000001'}):
    print(type(each)) # <class dict'>
    print(each)

##############
# <codecell> #
##############

# $eq 	Matches values that are equal to a specified value.
# $gt 	Matches values that are greater than a specified value.
# $gte 	Matches values that are greater than or equal to a specified value.
# $in 	Matches any of the values specified in an array.
# $lt 	Matches values that are less than a specified value.
# $lte 	Matches values that are less than or equal to a specified value.
# $ne 	Matches all values that are not equal to a specified value.
# $nin 	Matches none of the values specified in an array.

for each in mycol.find({'age':{'$gte': 20}}):
    print(each)

### projection parameters: specify the fields to return
# json: { field1: <value>, field2: <value> ... }

##############
# <codecell> #
##############
# only return the passwd that projection by value:true
for each in mycol.find({}, {'passwd':True}).limit(2):
    print(each)

#####################################################################################
## [update](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne)

# db.collection.updateOne(
#    <filter>,
#    <update>,
#    {
#      upsert: <boolean>,
#      writeConcern: <document>,
#      collation: <document>,
#      arrayFilters: [ <filterdocument1>, ... ]
#    }
# )
##############
# <codecell> #
##############
mydb.restaurant.drop()
mydb.restaurant.insert_many([
    { "_id" : 1,
        "name" : "Central Perk Cafe", "Borough" : "Manhattan" },
    { "_id" : 2,
        "name" : "Rock A Feller Bar and Grill", "Borough" : "Queens", "violations" : 2 },
    { "_id" : 3,
        "name" : "Empire State Pub", "Borough" : "Brooklyn", "violations" : 0 }
])
for each in mydb.restaurant.find():
    pprint(each)

##############
# <codecell> #
##############
# no voilation -> have
mydb.restaurant.update_one(
    {'name': 'Central Perk Cafe'},
    {'$set': {'violations': 3}}
).raw_result
# Out[127]: {'n': 0, 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}

##
for each in mydb.restaurant.find():
    pprint(each)

##############
# <codecell> #
##############
# if no -> insert
mydb.restaurant.update_one(
    {'name': "Pizza Rat's Pizzaria"},
    {'$set': {'_id': 4, 'violations':7,'borough':'Manhattan'}},
    upsert=True
).raw_result

##
for each in mydb.restaurant.find():
    pprint(each)


##############
# <codecell> #
##############
# arrayFilters
# { <update operator>: { "<array>.$[<identifier>]" : value } },
# { arrayFilters: [ { <identifier>: <condition> } } ] }
mydb.students.drop()
mydb.students.insert_many([
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
])
for each in mydb.students.find():
    pprint(each)

## filter array, first filter rows, then array_filters
mydb.students.update_one(
    {'grades': {'$gte': 100}},
    {'$set': {'grades.$[element]': 100}},
    array_filters = [{'element' : {'$gte': 100}}]
)
for each in mydb.students.find():
    pprint(each)

##
mydb.students.update_many(
    {},
    {'$set': {'grades.$[element]': 100}},
    array_filters = [{'element' : {'$gte': 100}}]
)
for each in mydb.students.find():
    pprint(each)

## filter array documents
# { <query selector> },
# { <update operator>: { "array.$[<identifier>].field" : value } },
# { arrayFilters: [ { <identifier>: <condition> } } ] }
mydb.students2.drop()
mydb.students2.insert_many([
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
])

##
# mydb.students2.update_many(
mydb.students2.update_one(
   {},
   {'$set': {'grades.$[elem].mean': 100}},
   array_filters=[{'elem.grade': {'$gte': 85 }}]
)
for each in mydb.students2.find():
    pprint(each)


############################Bios data collection#####################################
from bios_collection_data import bios_data

### query array
# [find](https://docs.mongodb.com/manual/reference/method/db.collection.find)

##############
# <codecell> #
##############

mybios = mydb.bios_data
mybios.drop()
mybios.insert_many(bios_data)

##############
# <codecell> #
##############
# {
#  "_id" : <value>,
#  "name" : { "first" : <string>, "last" : <string> }, // embedded document
#  "birth" : <ISODate>,
#  "death" : <ISODate>,
#  "contribs" : [ <string>, ... ],                     // Array of Strings
#  "awards" : [
#  "award" : <string>, year: <number>, by: <string> }  // Array of embedded documents
#         ...
#  ]
# }
for each in mybios.find():
    pprint(each)

##############
# <codecell> #
##############

for each in mybios.find({'_id': 8}, {'name':1}):
    print(each)

for each in mybios.find({'name.first': 'Yukihiro'}):
    pprint(each)

for each in mybios.find({'_id': {'$in': [3, 5]}}, {'awards':1}):
    pprint(each)

for each in mybios.find({'birth': {'$lt': datetime(1950, 5, 1)}}, {'birth':1}):
    pprint(each)

## one field 'and'
for each in mybios.find({'birth': {
    '$lt': datetime(1950, 5, 1),
    '$gt': datetime(1921, 1, 1)}
    }, {'birth':1}):
    pprint(each)

## multiple fields 'and'
for each in mybios.find({'birth': {'$gt': datetime(1955, 1, 1)},
    'death': {'$exists': False}}):
    pprint(each)

## regex
for each in mybios.find({'name.first': {'$regex': r'^J'}}, {'name': 1}):
    pprint(each)

## embedded doc query
for each in mybios.find({'name': {'first':'James', 'last': 'Gosling'}}):
    pprint(each)

## WARNING: no result below, no match all, so no result
for each in mybios.find({'name': {'first':'James'}}):
   pprint(each)

## array element query, if only match one of array elements, that's ok
for each in mybios.find({'contribs': 'ALGOL'}, {'contribs':1}):
    pprint(each)

## match any one of them, that's ok
for each in mybios.find({'contribs': {'$in':['ALGOL', 'UNIX']}}, {'contribs':1}):
    pprint(each)

## must match all, that's ok
for each in mybios.find({'contribs': {'$all':['ALGOL', 'FP']}}, {'contribs':1}):
    pprint(each)

## documents array query
for each in mybios.find({'awards.award': 'Turing Award'}):
    pprint(each)

for each in mybios.find({'awards':
    {'$elemMatch': {'award':'Turing Award', 'year': {'$gt': 1998}}}
    }):
    pprint(each)

# <codecell>
# readConcern and writeConcern 读写脏数据
# TODO
