#!/usr/bin/python2.7
#coding:utf-8

def main():
    """
    TODO main
    """
    #  print dir(m1)
    for key in dir(m1):
        print key, getattr(m1, key)

    # print dir(m2) # 错误 m2模块对象并没有导入该符号表中
    f1 = m1.fun1
    f2 = m1.fun2
    print f1(8)
    print f2(8)
    print fun3(10)
    print f4(10)
    b1.b1_fun()
    # b2.b2_fun() # 没有定义（__init__.py)

if __name__ == "__main__" :
    import sys
    print sys.path
    sys.path.append("mod") # 将mod模块加入到搜索路径中
    import m1
    from m2 import fun3, fun4 as f4
    from pack import *
    main()
