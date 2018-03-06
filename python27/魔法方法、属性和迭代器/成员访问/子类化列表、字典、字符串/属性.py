#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#如果访问给定的特性时必须要采取一些行动，那么封装状态变量就很重要：
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
        print size
    def getSize(self):
        return self.width,self.height
r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()
r.setSize((100,200))
# print r.getSize()
# print r.height

# Python 有两种创建属性的机制，下面主要是新的机制，只在新式类中使用property函数，
#propertiy函数

