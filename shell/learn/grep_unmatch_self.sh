#!/bin/bash

# 通过进程启动名查询进程时, grep自身也被查询到

ps aux | grep goldendict

# xxx  3:38 goldendict
# xxx  0:00 grep --color=auto --exclude-dir=.svn --exclude-dir=.git --exclude=tags goldendict


ps aux | grep [g]oldendict
# xxx  3:38 goldendict
