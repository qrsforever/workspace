#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

sentence = " hello world "

# 删除字符串中的所有空格，甚至是单词之间：
print(re.sub(r"\s+", "", sentence, flags=re.UNICODE))

# 删除字符串BEGINNING中的空格：
print(re.sub(r"^\s+", "", sentence, flags=re.UNICODE))

# 删除字符串END中的空格：
print(re.sub(r"\s+$", "", sentence, flags=re.UNICODE))

# 删除BEGINNING和字符串END中的空格：
print(re.sub("^\s+|\s+$", "", sentence, flags=re.UNICODE))

# 仅删除DUPLICATE空格：
print(" ".join(re.split("\s+", sentence, flags=re.UNICODE)))

