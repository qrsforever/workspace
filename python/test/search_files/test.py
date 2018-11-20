#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

headers_dirs = []

def search_header_dirs(path):
    for root, dirs, files in os.walk(path):
        if os.path.basename(root) in ['include', 'inc', 'Include', 'Inc']:
            headers_dirs.append(root)

        for file in files:
            if os.path.splitext(file)[1] == '.h':
                headers_dirs.append(root)
                break


def main():
    path = "/data/source/homebrain/iotivity/homebrain/src/http-handler" #input("Input dir:")
    search_header_dirs(path);
    print(headers_dirs)

if __name__ == "__main__":
    print(os.path.abspath( __file__ ))
    main()

