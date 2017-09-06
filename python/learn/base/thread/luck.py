#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, threading

balance = 0  
lock = threading.Lock()  

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    global balance
    while n < 5:
        n = n + 1
        lock.acquire()
        balance = balance + 1
        print('thread %s >>> %s balance %d' % (threading.current_thread().name, n, balance))
        lock.release()
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

t1 = threading.Thread(target = loop, name = 'LoopThread1')
t2 = threading.Thread(target = loop, name = 'LoopThread2')

t1.start()
t2.start()

t1.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)
