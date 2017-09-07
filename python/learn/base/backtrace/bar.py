#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import traceback

def testPrintStackInfo():  
    msg = traceback.format_exc() # 方式1  
    print(msg)  

def genException():
    testPrintStackInfo()
    # try:
    #    raise Exception("抛出一个异常")
    # except Exception as e:  
    #     logging.exception(e)    # 方式2  
    # finally:  
    #    pass  


def main():
    genException()

if __name__ == "__main__":
    main()

