#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LeecoSlots(object):

    """Docstring for LeecoSlots. """

    __slots__ = ("_year", "_month", "_day",)

    def __init__(self, year, month, day):
        """Test slots： 紧凑的内部表示， 存储空间优化, 缺点不能添加新的属性

        :year: TODO
        :month: TODO
        :day: TODO

        """
        self._year = year
        self._month = month
        self._day = day
        #  self._newitem = None  # 添加新属性会报错
