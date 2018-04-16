---

title: IOT规则引擎设计构思
date: 2018-04-16 14:49:03
tags: [ IOT ]
categories: [ SQL ]

---

<!-- vim-markdown-toc GFM -->

* [数据模型](#数据模型)
    * [温度和湿度设备](#温度和湿度设备)
    * [空调设备](#空调设备)
* [规则设置](#规则设置)
    * [数据处理](#数据处理)
    * [数据转发](#数据转发)

<!-- vim-markdown-toc -->

数据模型
========

数据库名: iot.db

以`product_产品ID`组合为表名建立表, 表中存储多个设备

温度湿度设备
------------

表名: `product_8GBCH2FO2`

dname      | temp  | humi  | date
-----------|:-----:|:-----:|:----------:
testTH1    |  10   |  10   | 2018-04-15


空调设备
--------

表名: `product_S7JV8369SF`

dname      | power 
-----------|:-----:
testAC1    |  0


规则设置
========

规则名:  `on_temp_humi_update`

数据处理
--------

Name    | Value
--------|----------------
字段    | temp, humi
TOPIC   | 8GBCH2FO2/testTH/event
条件    | temp > 30

数据转发
--------

Name    | Value
--------|----------------
TOPIC   | S7JV8369SF/testAC/control
PAYLOAD | {"command": "attr_set", "parameters": {"power":"on"}}
