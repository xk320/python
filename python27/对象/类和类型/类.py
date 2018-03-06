#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#类可视为种类或者类型的同义词，从很多方面来说，类是一种对象，所有的对象都属于某一个类，成为类的实例
#在面向对象程序设计中，所有子类的关心是隐式的，因为一个类的定义取决于他所支持的方法。
#类的所有实例都会包含这些方法，所以所有子类的所有实例都有这些方法，定义子类只是个定义更多的方法的过程
#创建一个类：
__metaclass__ = type
class Person:
#self在行数被调用的时候，自动将自身作为第一个参数传入函数中
#没有self这个参数，成员方法就没发访问他们要对其特性进行操作的对象本身
    def setName(self,name):
        self.name=name
    def getNmae(self):
        return self.name
    def greet(self):
        print 'Hello World!I`m %s.' % self.name
foo=Person()
bar=Person()
foo.setName('Tom')
bar.setName('Jack')
print foo.name,bar.name
foo.greet()
bar.greet()
foo.name='Lucy'
foo.greet()

