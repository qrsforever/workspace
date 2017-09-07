#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred
from twisted.internet import reactor

import threading
import time

def loadRemoteData(callback, errback, url):
    print("thread[%s] url = %s" % (threading.current_thread().name, url))
    # callback 和 errback 只能调用其中一个,  否则:AlreadyCalledError
    callback('callback data')
    #  errback(ValueError("errback dat"))

def getResult(v):
    print("thread[%s] result = %s" % (threading.current_thread().name, v))

def getError(e):
    print("thread[%s] error = %s" % (threading.current_thread().name, str(e)))

if __name__ == '__main__':
    d = Deferred()
    d.addCallback(getResult)
    d.addErrback(getError)

    print("main():thread[%s]" % threading.current_thread().name)
    reactor.callInThread(loadRemoteData, d.callback, d.errback, "http://www.baidu.com")
    reactor.callLater(4, reactor.stop); 
    # 测试, 验证 如果run不调用, callInThread 不工作
    time.sleep(2)
    reactor.run()

