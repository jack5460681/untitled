#!/usr/bin/python
#coding=utf-8

#判断输入是奇数好是偶数


for i in range(3) :
    num = input("please enter the num:\n")
    if num%2==0 :
        print ('{} is 偶数'.format(num))
    else:
        print('{} is 奇数'.format(num))
print 'it is  over '