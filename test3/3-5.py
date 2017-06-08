#!/usr/bin/python
#coding=utf-8

while 1:
    year=input("please enter the years :\n")
    if year%4==0:
        if year%100==0:
            if year%400==0:                      #  整百年可以被400整除是润年
                print('{} is 润年'.format(year))
            else:
                print ('{} is 平年'.format(year))
        else:
            print('{} is 润年'.format(year))  #非整百年，可以被4整除是润年
    else:
        print ('{} is 平年'.format(year))

