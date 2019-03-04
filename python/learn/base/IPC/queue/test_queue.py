#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import multiprocessing

def foo(queue):
    queue.put([11, 'hello', True])
    print("sub pid[{}], count[{}]".format(os.getpid(), queue.qsize()))


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target = foo, args=(queue,))
    process.start()
    print("main pid[{}]:{}".format(os.getpid(), queue.get()))
