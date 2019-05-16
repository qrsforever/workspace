#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
File: l_file.py
Author: qrsforever
Email: 985612771@qq.com
Github: https://github.com/qrsforever
Description: learn io
"""

import sys, os
from tempfile import TemporaryFile, NamedTemporaryFile

tmpfile='/tmp/tmpfile.txt'

def writeFile():
    try:
        with open(tmpfile, 'wt') as f:
            for i in range(0, 10, 1):
                f.write("Hello World {}\n".format(i))
    except IOError as err:
        print("File error: " + str(err))


def readFile():
    try:
        with open(tmpfile, 'rt') as f:
            for line in f:
                print(line, end='')
    except IOError as err:
        print("File error: " + str(err))


def tempFile():
    with TemporaryFile("w+t", encoding='utf-8') as f:
        f.write("Hello world\n")
        f.write("This is test\n")

        f.seek(0)
        print(f.read())


def binaryFile():
    sys.stdout.write('Hello World')
    sys.stdout.flush() # 没有换行符需要flush
    sys.stdout.write(' ---> Hello World\n')
    try:
        sys.stdout.write(b'Hello')
    except TypeError as err:
        print("write error: " + str(err))
    
    sys.stdout.buffer.write(b'Hello\n')  # This is ok.


def fd2fo():
    fd = os.open(tmpfile, os.O_CREAT | os.O_WRONLY | os.O_APPEND)
    fo = open(fd, 'wt', closefd=False) # False: 当fo close时不影响fd
    fo.write("Hi")
    fo.flush()
    fo.close()
    os.close(fd)


def namedtmpFile():
    with NamedTemporaryFile('w+t') as f:
        print('FileName: ', f.name)


if __name__ == "__main__":
    writeFile()
    readFile()
    tempFile()
    binaryFile()
    fd2fo()
    namedtmpFile()
