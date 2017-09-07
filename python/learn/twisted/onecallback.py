#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer

def not_call_deferred(result):
    print("not_call_deferred {}".format(result));

def getDummyData(inputData):
    print('getDummyData called')
    deferred = defer.Deferred()

    # deferred.callback 会进一步调用deferred添加进去的cb
    reactor.callLater(2, deferred.callback, inputData * 3)
    # 如果这里的回调是 not_call_deferred, 那么不会触发deferred.addCallback中的cb
    #  reactor.callLater(2, not_call_deferred, inputData * 3)
    return deferred

def cbPrintData(result):
    print('cbPrintData Result received: {}'.format(result))
    return "deliver next" # 这个返回会作为下一个callback的参数

def cbPrintData2(result):
    print('cbPrintData2 Result received: {}'.format(result))
    # 不起作用
    deferred = defer.Deferred()
    deferred.addCallback(cbPrintData, "new callback")
    return deferred

# 一直不执行, but why?
def cbPrintData3(result):
    print('cbPrintData Result received: {}'.format(result))
    return "deliver next next"

deferred = getDummyData(3)
print("lidong deferred : ", deferred)
deferred.addCallback(cbPrintData)
deferred.addCallback(cbPrintData2)
deferred.addCallback(cbPrintData3)

# manually set up the end of the process by asking the reactor to
# stop itself in 4 seconds time
reactor.callLater(4, reactor.stop)
# start up the Twisted reactor (event loop handler) manually
reactor.run()
