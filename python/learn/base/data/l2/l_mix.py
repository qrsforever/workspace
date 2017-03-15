#!/usr/bin/python3
#coding:utf-8

# 所有迭代对象都可以分离出变量

a = ('a', 'b', 'c')
a1, a2, _ = a   # 不需要的内容可以使用占位符(任意字符，推荐使用_)
print('{0} {1}'.format(a1, a2))

b = [100, 'a', 'b', (2017, 3, 7)]
b1, *_, (*_, b2) = b  # 使用*_忽略多个
print(b1, b2)

# 裁判评分
c = [85, 84, 90, 88, 81, 85]
c.sort()
print(c)
_, *c1, _ = c
print (sum(c1)/len(c1))

# 字符串也是迭代对象
d = 'abcdef'
d1, *_, d2, d3 = d
print(d1, d2, d3)

f = 'aa:bb:cc:dd'
_, f1, f2, _ = f.split(':')
print(f1, f2)

def do_foo(x, y):
    print('foo', x, y)

def do_bar(args):      
    print('bar', args)

g = [('foo', 1, 2), ('bar', 3, 3, 4, 4), ('foo', 5, 6)]
for tag, *args in g:
    if tag == 'foo':
        do_foo(*args) # 将元组参数化
    elif tag == 'bar':
        do_bar(args)  # args 参数本身是元组

