#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#callable 内建函数，可以用来判断函数是否能够被调用
#callable在python3.0中不在可用，需要使用表达式hasattr(func,__call__)代替
import math
x=1
y=math.sqrt
print callable(x)
print callable(y)
print y(4)

#创建函数
def hello(name):
    return 'Hello %s' % name
print hello('World')
print hello('Friend')

def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print fibs(10)

#文档化函数
#如果想要给函数写文档，让其他使用该函数的人能理解，可以加入注释。另外一种方式就是直接写上字符串。
#这类字符串在其他地方可能非常有用，比如在def语句后面。如果在函数的开头写下字符串，他就会作为函数的一部分进行存储。
#这成为文档字符串
def fibs(num):
    '此函数时计算斐波那列数列的函数'
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print fibs(10)
print fibs.__doc__
#__doc__是函数的属性

def test():
    print 'this is print'
    return
    print 'test'
x = test()
print x  #没有返回值的函数，默认返回None

