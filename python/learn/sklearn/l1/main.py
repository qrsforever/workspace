#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  import urllib.request
from numpy import genfromtxt, zeros, array
#  pylab 是matplotlib的接口
from pylab import plot, figure, subplot, hist, xlim, show
from sklearn.naive_bayes import GaussianNB

#  url = 'http://aima.cs.berkeley.edu/data/iris.csv'
#  u = urllib.request.urlopen(url)
#  localFile = open('iris.csv', 'w')
#  mybytes = u.read()
#  mystr = mybytes.decode('utf8')
#  localFile.write(mystr)
#  localFile.close()

#  花萼长， 花瓣长， 花萼宽， 花瓣宽
#  5.1,     3.5,    1.4,    0.2,    setosa
data = genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
#  print(data)
#  print(data.size)
#  通过shape获取数据集大小
#  print(data.shape)

target = genfromtxt('iris.csv', delimiter=',', usecols=(4,), dtype=str)
#  print(target)
#  print(target.shape)
#  样本集合 {'virginica', 'setosa', 'versicolor'}
#  print(set(target))

#  返回布尔类型数组
#  print(target=='setosa')))))))))))))))))
#  print(data[target=='setosa', 0])

#  二维散点图
plot(data[target=='setosa', 0], data[target=='setosa', 2], 'bo') 
plot(data[target=='virginica', 0], data[target=='virginica', 2], 'ro') 
plot(data[target=='versicolor', 0], data[target=='versicolor', 2], 'go') 
#  show()

#  特性直方图
xmin = min(data[:, 0])
xmax = max(data[:, 0])
print(xmin, xmax)
figure()
#  4行1列 第一列
subplot(411)
#  hist函数，给定一堆数据，统计数据在某一值的个数。plot是给定横/纵坐标向量，描绘点列。
hist(data[target=='setosa', 0], color='b', alpha=.7)
xlim(xmin, xmax)
subplot(412)
hist(data[target=='virginica', 0], color='r', alpha=.7)
xlim(xmin, xmax)
subplot(413)
hist(data[target=='versicolor', 0], color='g', alpha=.7)
xlim(xmin, xmax)
subplot(414)
hist(data[:, 0], color='y', alpha=.7)
xlim(xmin, xmax)
#  show()

#  把字符串数组转型成整型数据 (类别)
t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'virginica'] = 2
t[target == 'versicolor'] = 3

# 分类: 高斯朴素贝叶斯(http://www.cnblogs.com/pinard/p/6074222.html)
classifier = GaussianNB()
classifier.fit(data, t)
print(data)
print(t)
print(classifier.predict(data))
# 模拟数据(修改data中的最后一条)
test=array([5.7, 2.8, 5.3, 2.0])
# 转换为二维
#  print(test.reshape(1, -1))
print(classifier.predict(test.reshape(1, -1)))


#  学习来源： http://python.jobbole.com/83563/
