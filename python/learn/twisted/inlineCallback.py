#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet import defer, reactor 
  
def loadRemoteData(callback):  
    print("-----------> loadRemoteData callback: ", callback)
    import time 
    time.sleep(1)  
    callback(1) # 将1传给getResult, 只有callback之后才能触发callbacks结果
    print("callback end!")
  
def loadRemoteData2(callback):  
    print("-----------> loadRemoteData2 callback: ", callback)
    import time  
    time.sleep(1)  
    callback(2)  
 
@defer.inlineCallbacks  
def getRemoteData():  
    d1 = defer.Deferred()  
    # d1.callback 遍历回调所有callbacks
    reactor.callInThread(loadRemoteData, d1.callback)  
    print("yiled d1: ", d1)
    r1 = yield d1
    d2 = defer.Deferred()  
    reactor.callInThread(loadRemoteData2, d2.callback)  
    print("yiled d2: ", d2)
    r2 = yield d2  
  
    defer.returnValue(r1+r2)
  
def getResult(v):  
    print ("result = ", v)  

if __name__ == '__main__':  
    d = getRemoteData()  
    print("main d = ", d)
    print("main getResult: ", getResult)
    d.addCallback(getResult)  
  
    #  import time 
    #  time.sleep(4)
    # 以下两行可以使用sleep替换, 不影响功能测试
    reactor.callLater(4, reactor.stop);   
    reactor.run()
