#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

def bar():
    print("bar in")
    time.sleep(1)

    r1 = yield "one"

    print("r1 = ", r1)
    print("bar out")

f = bar()
print("start...")
time.sleep(3)
print(f.send(1)) # 不调用send bar()不会执行
#  print(f.send(None)) # 不调用send bar()不会执行
print("next")
print(f.send(1)) # 异常, 不调用yield后面的代码不执行
print("end...")

time.sleep(100)
