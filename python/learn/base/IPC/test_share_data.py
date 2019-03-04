#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Manager,Process

def foo(l,i):
    l.append(i**i)

if __name__ == '__main__':
    man = Manager()
    mlist = man.list([11,22,33])
    processes = []
    for i in range(5):
        p = Process(target=foo,args=(mlist,i))
        p.start()
        processes.append(p)
    for p in processes: # 必须要join，不然会执行报错，处理一个数据必须要一个个来，不能同时处理一个数据
        p.join()
    print(mlist)
