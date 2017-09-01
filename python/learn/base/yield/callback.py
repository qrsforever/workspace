#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred
from twisted.internet import reactor
 
def loadRemoteData(callback,errback,url):
    callback('url数据')

def getRemoteData():
    d = Deferred()
    reactor.callInThread(loadRemoteData,d.callback,d.errback,"http://www.baidu.com")
    return d

def getResult(v):
    print("result=",v)

if __name__ == '__main__':
    d=getRemoteData()
    d.addCallback(getResult)

    reactor.callLater(4, reactor.stop); 
    reactor.run()
