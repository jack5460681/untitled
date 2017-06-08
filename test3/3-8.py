#!/usr/bin/python
#coding=utf-8

def my_abs(args,h):
    if not isinstance(args,int):
        raise "typeError"
    if args>0:
         return  1,h
    else:
        return  0,h

b=my_abs(3,2)
c=my_abs(32,5)
print b,c
