#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.internet import defer, reactor

@defer.inlineCallbacks
def print_file():
    try:
        # async_get_file still returns a Deferred
        file_ = yield async_get_file() # After yield, it's not a Deferred anymore
        yield async_print_file(file_)
        print("Success.")
    except Exception as err:
        print("Error", err)
    finally:
        print("Shutting down")
        reactor.stop()

if __name__ == '__main__':
    print_file()
