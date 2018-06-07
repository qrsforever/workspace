---

title: Clips C++ interface
date: 2018-06-04 16:24:24
tags: [ Clips, C++ ]
categories: [ Local ]

---

依赖
====

1. 源码clips630
    - [Download from baidu yunpan](https://pan.baidu.com/s/1hzLVwX_clG50FjaJ0t7hdg)
    - [Download from offical web](https://sourceforge.net/projects/clipsrules/files/CLIPS/6.30/)

2. 编译clips630

build lib:

- `cd clips_core_source_630/core`
- `ln -s ../makefiles/makefile.lib makefile`
- `make`

build clips:
-  `cd clips_core_source_630/core`
-  `ln -s ../makefiles/makefile.gcc makefile`
-  `make`


调试编译
========

1. 修改`Makefile`指定`CLIPS630_DIR`路径

2. make; make test; make clean
