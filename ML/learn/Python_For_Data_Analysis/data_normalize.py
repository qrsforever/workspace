#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyther console

#  from pandas import Series, DataFrame
import pandas as pd

## merge and join
data1 = pd.DataFrame(data={'cv1' : ['rv2','rv1','rv2','rv3','rv2'],
    'cv2' : range(5)})
data1

data2 = pd.DataFrame(data={'cv1' : ['rv1', 'rv4', 'rv2'],
    'cv3' : range(3)})
data2

pd.merge(data1, data2)
data1.merge(data2)
data2.merge(data1)

data3 = pd.DataFrame({'key':['b','b','a','c','a','a','b'], 'data1':range(7)})
data3
data4 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
data4
pd.merge(data3, data4)
pd.merge(data3, data4, on='key')

data5 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'], 'data1':range(7)})
data5
data6 = pd.DataFrame({'rkey':['a', 'a', 'b','d'], 'data2':range(4)})
data6
pd.merge(data5, data6, left_on='lkey', right_on='rkey')
pd.merge(data6, data5, left_on='rkey', right_on='lkey')

pd.merge(data5, data6, left_on='lkey', right_on='rkey', how='outer')
pd.merge(data5, data6, left_on='lkey', right_on='rkey', how='left')
pd.merge(data5, data6, left_on='lkey', right_on='rkey', how='right')
