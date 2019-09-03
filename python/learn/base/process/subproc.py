#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import subprocess

task = subprocess.Popen(['top', '-n', '5'])
print(task.pid)

while True:
    print(task.poll())
    time.sleep(1)
