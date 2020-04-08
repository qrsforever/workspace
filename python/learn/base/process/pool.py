#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file pool.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2020-04-08 14:34:15

################################  jupyter-vim #######################################
# Start: JupyterXvfb or Jupyter
# ji, jj, jc, je, jp, jt
#####################################################################################


from multiprocessing import Pool, Manager
import subprocess

##
def func0(a, b):
    print(a + b)


def main0():
    args = [(1, 2), (3, 4), (5, 6)]
    pool = Pool(3)
    pool.starmap(func0, args) # wait


main0()


## 进程间共享
def func1(dic, c):
    print(dic['count'], c)
    dic['count'] += c


def main1():
    d = Manager().dict()
    d['count'] = 0
    args = [(d, 1), (d, 2), (d, 3)]
    pool = Pool(3)
    pool.starmap(func1, args)
    pool.close()
    pool.join()
    print(f'dict={d}')


main1()


## map run
def func2(sh):
    (statusLoad, outputLoad) = subprocess.getstatusoutput(sh)
    print('command:', sh, '\n', outputLoad)
    return (statusLoad, outputLoad)


def main2():
    sh_list = []
    sh_list.append('ls -l')
    sh_list.append('ls -a')
    sh_list.append('ls')

    pool = Pool(len(sh_list))
    pool.map(func2, sh_list)
    pool.close()
    pool.join()


main2()
