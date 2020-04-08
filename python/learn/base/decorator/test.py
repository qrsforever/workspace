#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.datacamp.com/community/tutorials/decorators-python


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'


print(say_hi())
