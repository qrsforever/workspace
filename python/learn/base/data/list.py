#!/usr/bin/python3
#coding:utf-8

from itertools import zip_longest

def test():
    print(dir(list))

    l = [x for x in range(10)]

    print(l.__class__)

    l.append('d')
    l.insert(0, 0)
    l.insert(3, 'a')
    print(l)
    print(l.count('a'))
    print("l.pop():", l.pop()) # 最后一个
    print("l.pop(0):", l.pop(0))
    print("l.remove(a):", l.remove('a'))
    print(l)
    l.reverse()
    print(l)
    l.sort(reverse=True)
    for x in l:
        print(x, end=',')


    print("-------------- enumerate")

    for i, x in enumerate(l, 0):
        print(i, x)

    print("-------------- zip")

    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    for x, y in zip(a, b):
        print(x, y) # 7 not output

    print("-------------- zip_longest")

    for x, y in zip_longest(a, b, fillvalue=0):
        print(x, y) 


    print("-------------- ")

    data = [1, 2 , 3, 4, 5]

    print(data[:-2]) # 1,2,3
    print(data[-1])  # 5
    print(data[-2])  # 4

if __name__ == "__main__":
    # ?? [::-1]
    colors = ['#f7fbff', '#deebf7', '#c6dbef',
            '#9ecae1', '#6baed6', '#4292c6',
            '#2171b5','#08519c','#08306b'][::-1]

    print(colors[0])
