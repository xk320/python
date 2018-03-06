#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#变量和所对应的值用的是一个不可见的字典，这类不可见字典叫做命名空间或者作用域
#除了全局作用域外，每个函数调用都会创建一个新的作用域
# 
x=1
scope=vars()
print scope['x']
scope['x'] +=1
print x
#函数中读取全局变量
def combine(parameter):
    print parameter,external
external='berry'
combine('test')

#函数中声明修改全局变量
x=1
def change_global():
    global x
    x+=1
print x

#函数嵌套
#一个函数位于另外一个函数的里面，外层函数返回里层函数。也就是说函数本身被返回了，但并没有被调用。
#重要的是返回的函数还可以访问它的定义所在的作用域，它带着它的环境。
#类似multiplyByFactor函数存储子封闭作用域的行为叫做闭包（closure）
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
double=multiplier(2)
print double
print double(5)