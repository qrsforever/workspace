#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Bar(object):

    def __init__(self):
        print("__init__") 

    def do(self, task):
        print("do.task")
        task()

    def report(self, bug):
        print("report.txt")
        bug()

def justdo(task):
    print("just do")
    bar = Bar()
    @bar.do
    def doWork():
        print("doWork")
        task()
        @bar.report
        def doReport():
            print("<------report---->")


def task():
    print("I am worker, now do...")

justdo(task)
