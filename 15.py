#!/usr/bin/python
#coding=utf-8

score=int(raw_input("please enter your score:\n"))
if score>=90:
    grade="A"
elif score>60:
    grade="B"
else:
    grade="c"
print "%f blongs to %s"%(score,grade)

