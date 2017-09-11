#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet import defer, reactor 
  
def loadRemoteData(callback):  
    print("---> loadRemoteData  callback: ", callback)
    import time 
    time.sleep(1)  
    callback(1) # 将1传给getResult, 只有callback之后才能触发callbacks结果
  
def loadRemoteData2(callback):  
    print("---> loadRemoteData2 callback: ", callback)
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
    
    # 不像其他生成器函数, send抛StopIteration, 异常, 而是主动跑_DefGen_Return异常
    defer.returnValue(r1+r2) # raise
    # 也可以使用return
    #  return r1+r2
  
def getResult(v):  
    print ("result = ", v)  

if __name__ == '__main__':  
    d0 = getRemoteData()  
    print("main d0 : ", d0)
    d0.addCallback(getResult)  
  
    #  import time 
    #  time.sleep(4)
    # 以下两行可以使用sleep替换, 不影响功能测试
    reactor.callLater(4, reactor.stop);   
    reactor.run()
