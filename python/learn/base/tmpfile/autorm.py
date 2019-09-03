#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tempfile
import time

tmpfile = tempfile.NamedTemporaryFile('w', suffix='running',
        prefix='test', dir='/workspace/python/learn/base/tmpfile')

# 名字还是随机的
print(tmpfile.name)

time.sleep(20)
