#!/usr/bin/python3
# -*- coding: utf-8 -*-

import setting

for key in dir(setting):
    if key.isupper():
        print(getattr(setting, key))

