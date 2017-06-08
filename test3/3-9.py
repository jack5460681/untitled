#!/usr/bin/python
#coding=utf-8

import math

#a*x² + b*x + c ==0

def qiugen(a,b,c,):

    if (b*b-4*a*c>=0):
        d = math.sqrt(b * b - 4 * a * c)
        x1 = ((-b + d) / 2 * a)
        x2 = ((-b - d) / 2 * a)
        return x1,x2



    else:
        return '没有根'
print qiugen(1,-1,4)
