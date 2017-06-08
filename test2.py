#!/usr/bin/python
#coding=utf-8
class Employee():
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print "Total Employee %d"%Employee.empCount

    def displayEmployee(self):
        print "Name:",self.name,"Salary:",self.salary

"创建Employee类的第一个对象"
emp1= Employee("CHEN",510)
"创建Employee类的第二个对象"
emp2=Employee("ZHI",600)
emp1.displayCount()
emp2.displayEmployee()
emp1.displayEmployee()