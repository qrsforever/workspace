#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyther console

import pandas as pd

## read: !cat ./pydata-book/examples/ex1.csv
data1 = pd.read_csv('./pydata-book/examples/ex1.csv')
data1

data2 = pd.read_table('./pydata-book/examples/ex1.csv', sep=',')
data2

## read: !cat ./pydata-book/examples/ex2.csv
data3 = pd.read_csv('./pydata-book/examples/ex2.csv', header=None)
data3
data4 = pd.read_csv('./pydata-book/examples/ex2.csv',
        names=['a', 'b', 'c', 'd', 'message'])
data4
data5 = pd.read_csv('./pydata-book/examples/ex2.csv',
        names=['a', 'b', 'c', 'd', 'message'], index_col='message')
data5

## read: !cat ./pydata-book/examples/csv_mindex.csv
data6 = pd.read_csv('./pydata-book/examples/csv_mindex.csv',
        index_col=['key1', 'key2'])
data6

## read: !cat ./pydata-book/examples/ex3.csv
data7 = pd.read_table('./pydata-book/examples/ex3.csv', sep='\s+')
data7

## read: !cat ./pydata-book/examples/ex4.csv
data8 = pd.read_csv('./pydata-book/examples/ex4.csv',
        skiprows=[0,2,3])
data8

## read: !cat ./pydata-book/examples/ex5.csv
data9 = pd.read_csv('./pydata-book/examples/ex5.csv')
data9
pd.isnull(data9)

sentinels = {'message' : ['foo'], 'something' : ['two', 'three']}
data10 = pd.read_csv('./pydata-book/examples/ex5.csv', na_values=sentinels)
data10

## big data: !cat ./pydata-book/examples/ex6.csv | head -n 10
data11 = pd.read_csv('./pydata-book/examples/ex6.csv')
data11

data12 = pd.read_csv('./pydata-book/examples/ex6.csv', nrows=5)
data12
