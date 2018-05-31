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
