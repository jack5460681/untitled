#!/usr/bin/python
# _*_coding:utf-8 _*_

#输入一个数字，判断是否是质数



while 1:
    num = input("请输入一个数字：\n")  # 用户输入数字
    if num>1:
        #判断质数大于1
        for i in range(2,num):
            if num%i==0:   #是否有其他因子
                print num ,"不是质数"
                print  num,"等于",i,"乘以",num/i
                break
        else:
            print  num,"是质数"
    else:
        print num ,"不是质数"