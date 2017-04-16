#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LeecoPoint(object):

    """Docstring for LeecoPoint. """

    def __init__(self, x, y):
       self.x = x
       self.y = y

    def __repr__(self):
        #  return 'LeecoPoint(%r, %r)' % (self.x, self.y)
        return 'LeecoPoint({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        #  return '(%d, %d)' % (self.x, self.y)
        return '({0.x!s}, {0.y!s})'.format(self)
    
    def __unicode__(self):
        pass  

a = LeecoPoint(1, 2)

print(repr(a))
print(eval(repr(a)) == a) # 正确的做法是为真， 但是本实例没能做到。
print(str(a))

_formats = {
        'ymd': '{dd._year}-{dd._month}-{dd._day}',
        'mdy': '{dd._month}/{dd._day}/{dd._year}',
        'dmy': '{dd._day}/{dd._month}/{dd._year}'
        }

#  _formats = {
        #  'ymd': '{0._year}-{0._month}-{0._day}',
        #  'mdy': '{0._month}/{0._day}/{0._year}',
        #  'dmy': '{0._day{/{0._month}/{0._year}'
        #  }

class LeecoDate(object):

    """Docstring for LeecoDate. """

    def __init__(self, year, month, day):
        """TODO: to be defined1.

        :year: TODO
        :month: TODO
        :day: TODO

        """
        self._year = year
        self._month = month
        self._day = day
                
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        #  return fmt.format(self)
        return fmt.format(dd=self)

d = LeecoDate(2017, 4, 16)
print(format(d)) # 函数format
print(format(d, 'mdy'))
print('The date is {:dmy}'.format(d)) # 字符串方法format
