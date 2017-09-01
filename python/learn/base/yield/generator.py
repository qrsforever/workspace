#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gen_generator():
    print("gen_generator")
    yield 1

def gen_value():
    print("gen_value")
    return 1

def gen_example():
    print("Before any yield")
    x = yield 'First return from yield'
    print("Middle yield, x = ", x)
    x = yield 'Second return from yield'
    print("No yield any more, x = ", x)

def gen_example2():
    print("Before any yield")
    x = yield gen_value()
    print("Middle yield, x = ", x)
    x = yield gen_value()
    print("No yield any more, x = ", x)

def gen_example3():
    print("Before any yield")
    x = yield gen_generator()
    print("Middle yield, x = ", x, " type(x)", type(x))
    x = yield gen_generator()
    print("No yield any more, x = ", x)

if __name__ == '__main__':
    ret = gen_generator()
    print(ret, type(ret))    #<generator object gen_generator at 0x02645648> <type 'generator'>
    ret = gen_value()
    print(ret, type(ret))    # 1 <type 'int'>

    print("------__next__()-------- ")
    ret = gen_example()
    print(ret, type(ret))
    print(ret.__next__())       # First return from yield
    print(ret.__next__())       # Second return from yield
    try:
        print(ret.__next__())   # Exception StopIteration
    except Exception as e:
        pass

    print("------send(msg)-------- ")
    ret = gen_example()
    print(ret, type(ret))
    print(ret.send(None))        # First return from yield (第一次send(None))
    print(ret.send("x's value")) # Second return from yield
    try:
        print(ret.send("End"))   # Exception StopIteration
    except Exception as e:
        pass

    print("------yield func()-------- ")
    ret = gen_example2()
    print(ret, type(ret))
    print(ret.__next__())       # 1 x = None
    print(ret.__next__())       # 1 x = None
    try:
        print(ret.__next__())
    except Exception as e:
        pass

    print("------yield func(){ yield }-------- ")
    ret = gen_example3()
    print(ret, type(ret))
    #  print(ret.__next__())       # 1 x = None
    #  print(ret.__next__())       # 1 x = None
    #  try:
        #  print(ret.__next__())
    #  except Exception as e:
        #  pass
