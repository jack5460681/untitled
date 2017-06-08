#!/usr/bin/python
#coding=utf-8


num=64
num_chance=3

print 'you have only 3 chances to guess'
for i in range(1,num_chance+1):
    print 'chance :',i
    num1 = int(input('please enter the num1:\n'))
    if num1==num:
      print 'bingo  you are best!'
      break
    elif num1>num:
        print 'no,the num1 is bigger than num \nyou have: ',num_chance-i,'chances left'

    else:
        print 'no,the num1 is smaller than num\nyou have: ',num_chance-i,'chances left'

print 'done'