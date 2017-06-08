#!/usr/bin/python
#coding=utf-8

#输入任意年月日，知道是该年第几天
p=[31,28,31,30,31,30,31,31,30,31,30,31] #平年
r=[31,29,31,30,31,30,31,31,30,31,30,31] #润年

year=int(raw_input("请输入年份;\n"))
month=int(raw_input("请输入月份:\n"))
day=int(raw_input("请输入天数:\n"))

arr=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=day
for i in range(0,month-1):
    sum+=arr[i]

if year%4==0:
    if year%100==0and year%400!=0:
        print "%d,%d,%d是%d的第%d天"%(year,month,day,year,sum)
    else:
        sum=sum+1
        print "%d,%d,%d是%d的第%d天"%(year,month,day,year,sum)
else:
    print "%d,%d,%d是%d的第%d天"%(year,month,day,year,sum)