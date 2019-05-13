#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess


p = subprocess.Popen(args="ls -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
result =p.communicate()
print(result[0].decode("gbk"))

