---

title: 使用工具代码模块介绍
date: 2018-05-31 13:43:50
tags: [ Utils ]
categories: [ C++ ]

---


技巧
====

更改namespace名字
-----------------

```
sed -i "s/namespace\ UTILS/namespace\ IOT/g" `grep "namespace\ UTILS" -rl .`
```

编译
====

单独编译静态库
--------------

1. cd Misc; make; make test

2. cd Message; make; make test

3. cd Log; make; make test


编译成一个动态库
----------------

1. make -f Makefile.utils

2. make -f Makefile.utils clean
