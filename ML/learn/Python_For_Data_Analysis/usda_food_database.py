#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyter console
import pandas as pd
import json

##
db = json.load(open('./pydata-book/datasets/usda_food/database.json'))
type(db) # list
len(db)
type(db[0]) # dict
db[0].keys()
type(db[0]['nutrients']) # list
len(db[0]['nutrients'])
db[0]['nutrients'][0]

##
nutrients = pd.DataFrame(db[0]['nutrients'])
nutrients[:7]
nutrients.describe()

info = pd.DataFrame(db,
        columns=['description', 'group', 'id'])
info[:7]
len(info.id)
pd.value_counts(info.group)[:10]

## id as outer key
nutrients = []
for rec in db:
    df = pd.DataFrame(rec['nutrients'])
    df['id'] = rec['id']
    nutrients.append(df)
len(nutrients)
nutrients = pd.concat(nutrients, ignore_index=True)
type(nutrients)
nutrients.duplicated().sum()
nutrients.drop_duplicates()
nutrients[:7]

## description and group overlap
info = info.rename(columns={'description':'food', 'group':'fgroup'}, copy=False)
info[:7]
nutrients = nutrients.rename(columns={'description':'nutrient', 'group':'nutgroup'}, copy=False)
nutrients[:7]

data = pd.merge(nutrients, info, how='outer', on='id')
data[:7]
