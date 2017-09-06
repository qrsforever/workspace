#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool  
import os, time, random  
  
def long_time_task(name):  
    print('Run task %s (%s)...' % (name, os.getpid()))  
    start = time.time()  
    time.sleep(random.random() * 3)  
    end = time.time()  
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))  
  
if __name__=='__main__':  
    print('Parent process %s.' % os.getpid())  
    p = Pool(4) # Pool的默认大小是CPU的核数
    for i in range(5):  
        p.apply_async(long_time_task, args=(i,))  
    print('Waiting for all subprocesses done...')  
    p.close() # 调用close()之后就不能创建新的进程 
    p.join() # 等待所有subprocess finish
    print('All subprocesses done.')  
