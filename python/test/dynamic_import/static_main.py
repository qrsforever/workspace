#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from imp import reload

def dy_import_fun():
    import dyimp
    reload(dyimp)
    dyimp.show()

if __name__ == "__main__":
    dy_import_fun()
    print("to modify dyimp.py show function: print(\"2\")")
    time.sleep(5)
    dy_import_fun()
