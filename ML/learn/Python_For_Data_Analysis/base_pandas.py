#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyter console
import numpy as np
from pandas import Series, DataFrame
#  import pandas as pd

## Series
obj1 = Series([2,4,6,8])
obj1.values
obj1.index
obj1.align

obj2 = Series([2,4,6,8], index=['a','b','c','d'])
obj2.values
obj2.index

obj1[2]
obj2['b'] = 14
obj2[['b', 'c','d']]
obj2[obj2 > 6]
obj2 * 2
np.exp(obj2)

## Series data align
sdata = { 'aa' : 1, 'bb' : 2 , 'cc' : 3 }
obj3 = Series(sdata)
obj3
obj4 = Series(sdata, index=['xx', 'aa', 'bb'])
obj4
obj4.isnull()
obj4.notnull()
obj3 + obj4

## DataFrame
data = {
        'year': [2001, 2002, 2003],
        'state' : ['aa', 'bb', 'cc'],
        'pop' : [ 1.1, 2.2, 3.3]
        }
obj5 = DataFrame(data)
obj5

obj6 = DataFrame(data, columns=['year', 'state', 'pop'])
obj6

## DataFrame length must match, index(xx,yy,zz)
obj7 = DataFrame(data, columns=['year', 'state', 'pop'], index=['xx','yy','zz'])
obj7
obj7.loc['yy']
obj7.iloc[1]
obj7['state']
obj7.state
obj7['dat'] = 1.4

## Base function: reindex
obj8 = Series([1.5, 3.5, 6.5], index=['b','c','a'])
obj8
obj9 = obj8.reindex(index=['a','b','c', 'd'], fill_value=0.0)
obj9

obj10 = Series(['red', 'blue', 'yellow'], index=[0, 2, 4])
obj10
obj11 = obj10.reindex(index=range(6), method='ffill')
obj11

obj12 = Series(['red', 'blue', 'yellow'], index=[1, 3, 5])
obj12
obj13 = obj12.reindex(index=range(6), method='bfill')
obj13

obj14 = DataFrame(data=np.arange(9).reshape((3,3)),
        index=['r1','r2','r3'], columns=['col1','col2','col3'])
obj14
obj15 = obj14.reindex(columns=['col2', 'col3', 'col1'], index=['r3', 'r1', 'r2'])

## Base function: drop
obj9.drop(['d'])
obj15.drop(['r2'])
obj15.drop(['col2'], axis=1)

## Base function: cut
obj9['b':'c']
obj15['col1']
obj15[['col2', 'col3']]
obj15[:2]
obj15[obj15 > 4] = 0
obj15

## Base function: broadcast
obj16 = DataFrame(data=np.arange(12).reshape((4,3)),
        index=['r1', 'r2', 'r3', 'r4'],
        columns=['col1', 'col2', 'col3'])
obj16
obj16.iloc[1]
obj16.loc['r2']

## Base function: apply
obj17 = DataFrame(data=np.random.randn(4,3),
        index=['r1', 'r2', 'r3', 'r4'],
        columns=['col1', 'col2'])
obj17
np.abs(obj17)

obj17.apply(lambda x : x.max() - x.min(), axis=0)
obj17.apply(lambda x : x.max() - x.min(), axis=1)

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
obj17.apply(f)

## Base function: sort
obj17.sort_index(ascending=False)
obj17.sort_index(ascending=False, axis=1)

obj18 = Series(np.random.randint(1,100,12))
obj18
obj18.sort_values()


## two data type: obj19 == obj20
obj19 = DataFrame(data={'col1':[1,2,3,4], 'col2':[4,3,2,1]})
obj20 = DataFrame(data=[
    {'col1':1, 'col2':4}, {'col1':2, 'col2':3},
    {'col1':3, 'col2':2}, {'col1':4, 'col2':1}])

