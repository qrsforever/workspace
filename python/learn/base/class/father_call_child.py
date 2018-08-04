#!/usr/bin/python3
# -*- coding: utf-8 -*-


class mx(object):
    def f(self, str):
        try:
            func = getattr(self, str)
            func()
        except AttributeError as e:
            print("not found %s method" % str)

class cmx(mx):
    def a(self):
        print('haaa')

    def b(self):
        print('hbbb')


mycmx = cmx()
mycmx.f('a')
mycmx.f('c')
