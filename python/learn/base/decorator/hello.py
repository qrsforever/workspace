#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import traceback


def callme():
    type_, value_, traceback_ = sys.exc_info()
    print(type_,  value_)
    traceback.print_tb(traceback_)


def myexception(handler):
    def decorator(func=None):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ZeroDivisionError as e:
                type_, value_, traceback_ = sys.exc_info()
                traceback.print_tb(traceback_)
                print("#####################")
                callme()
                print("#####################")
                traceback.print_tb(e.__traceback__)
            except Exception: # noqa
                handler(traceback.format_exc())
        return wrapper
    return decorator


class MessageHandler(object):
    @staticmethod
    def report(msg):
        print(msg)


@myexception(MessageHandler.report)
def zero_divide():
    1 / 0


if __name__ == '__main__':
    zero_divide()
