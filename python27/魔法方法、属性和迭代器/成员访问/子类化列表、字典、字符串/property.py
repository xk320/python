# -*- coding: UTF-8 -*-
# Python 有两种创建属性的机制，下面主要是新的机制，只在新式类中使用property函数，
#property函数
#property函数创建了一个属性，其中访问器函数被用作参数(先取值，然后赋值)，这个属性命为size
__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
        print size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)
r= Rectangle()
r.width=5
r.height=10
print r.size
r.size=150,100

