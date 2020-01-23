#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

line = "aaaa 0.1"
temp = re.findall(r'-?\d+\.?\d*e?-?\d*?', line)
