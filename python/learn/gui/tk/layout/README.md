---

title: Layout
date: 2018-07-24 12:48:53
tags: [  ]
categories: [  ]

---

三大
====

Tkinter对于图形界面的布局管理有三大类：pack、grid、place
Pack()方法提供了选项来布局组件在界面中的位置，选项有：side、expand、fill、等
Grid()方法是采用行列来确定组件在界面中的位置，row是行号，column是列号。
Place()方法是通过组件在界面中的横纵坐标来固定位置。


Pack参数
========

expand
------

当值为“yes”时，side选项无效(?? 亲测不对)。组件显示在父配件中心位置；若fill选项为”both”,则填充父组件的剩余空间。
“yes”, 自然数, “no”, 0 （默认值为“no”或0）

fill
----

填充x(y)方向上的空间，当属性side=”top”或”bottom”时，填充x方向；当属性side=”left”或”right”时，填充”y”方向；当expand选项为”yes”时，填充父组件的剩余空间。
“x”, “y”, “both” (默认值为待选)

ipadx, ipady
------------

组件内部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
非负浮点数（默认值为0.0）

padx, pady
----------

组件外部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
非负浮点数（默认值为0.0）
padx=(left, right)

side
----

定义停靠在父组件的哪一边上。 (顺次放置控件)
“top”, “bottom”, “left”, “right”（默认为”top”）

anchor
------

对齐方式，左对齐”w”，右对齐”e”，顶对齐”n”，底对齐”s”
“n”, “s”, “w”, “e”, “nw”, “sw”, “se”, “ne”, “center” (默认为” center”)


Grid参数
========

columnspan
----------

从组件所置单元格算起在列方向上的跨度。
自然数（起始默认值为0）

rowspan
-------

从组件所置单元格算起在行方向上的跨度。
自然数（起始默认值为0）

sticky
------

(not support anchor, use sticky)
组件紧靠所在单元格的某一边角。
“n”, “s”, “w”, “e”, “nw”, “sw”, “se”, “ne”, “center” (默认为” center”)
