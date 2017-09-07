#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Bar(object):

    def __init__(self):
        print("__init__") 

    def do(self, task):
        print("do.task")
        task()


def justdo(task):
    print("just do")
    bar = Bar()
    @bar.do
    def doWork():
        print("show before task")
        task()

def task():
    print("I am worker, now do...")

justdo(task)
