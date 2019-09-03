#!/usr/bin/python3
# -*- coding: utf-8 -*-

import atexit
import time
import os

def cleanup(file):
    print(file)

atexit.register(cleanup, "/tmp/a.txt")

time.sleep(100)

os.waitpid(0,0)
