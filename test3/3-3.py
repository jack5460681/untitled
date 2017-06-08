#!/usr/bin/python
#coding=utf-8
import unicodedata

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:

        unicodedata.numeric(s)
        return True
    except TypeError:
        pass
    return False


#调用is_number 函数
print is_number('10')