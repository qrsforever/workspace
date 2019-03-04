#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing

def foo(sk):
    sk.send('hello world')
    print(sk.recv())

if __name__ == "__main__":
    conn1,conn2=multiprocessing.Pipe() # 开辟两个口，都是能进能出，括号中如果False即单向通信
    p=multiprocessing.Process(target=foo,args=(conn1,))  # 子进程使用sock口，调用foo函数
    p.start()
    print(conn2.recv())  # 主进程使用conn口接收
    conn2.send('hi son') # 主进程使用conn口发送
