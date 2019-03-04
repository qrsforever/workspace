#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import time

def foo(n):
    print(n)
    time.sleep(1)

if __name__ == '__main__':
    pool_obj=Pool(5)    #
    for i in range(5):
        pool_obj.apply_async(func=foo,args=(i,))
        #  pool_obj.apply(func=foo,args=(i,))    # 子进程的生成是靠进程池对象维护的
        # apply同步，子进程一个个执行
        # apply_async异步，多个子进程一起执行
    pool_obj.close()
    pool_obj.join() # after close or terminate called
    print('ending')
