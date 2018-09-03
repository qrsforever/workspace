#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyter console

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

## merge
data1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'], 'data1':range(7)})
data1
data2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
data2
pd.merge(data1, data2)
pd.merge(data1, data2, on='key')

data3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'], 'data1':range(7)})
data3
data4 = pd.DataFrame({'rkey':['a', 'a', 'b','d'], 'data2':range(4)})
data4
pd.merge(data3, data4, left_on='lkey', right_on='rkey')
pd.merge(data4, data3, left_on='rkey', right_on='lkey')

pd.merge(data3, data4, left_on='lkey', right_on='rkey', how='outer')
pd.merge(data3, data4, left_on='lkey', right_on='rkey', how='left')
pd.merge(data3, data4, left_on='lkey', right_on='rkey', how='right')


## numpy: concatenate
data5 = np.arange(12).reshape((4,3))
data5
np.concatenate((data5, data5))
np.concatenate((data5, data5), axis=1)

## pandas: concat
data6 = Series(['a','b','c'])
data7 = Series(['d','e'], index=[3,4])
pd.concat([data6, data7])
data8 = pd.concat([data6, data7], axis=1)
type(data8)
data9 = pd.concat([data6, data7], axis=1, join='inner')

## numpy: where
data10 = Series([np.nan, 1.5, np.nan, 2.5, 3.5], index=list('abcde'))
data11 = Series(np.arange(len(data10), dtype=np.float64), index=list('abcde'))
data11[-1] = np.nan
np.where(pd.isnull(data10), data11, data10)

## transform: remove duplicates
data12 = DataFrame({'col1': ['xx'] * 3 + ['yy'] * 4, 'col2': [1,1,2,2,3,4,4]})
data12.duplicated()
data12.drop_duplicates()
data12['col3'] = range(7)
data12.drop_duplicates(['col1'])

