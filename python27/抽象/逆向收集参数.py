#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import operator
#对于参数列表的逆向使用，在逆向过程中*不是要收集参数，是在调用而不是在定义的时候使用
def add(x,y):
    return x+y
params=(1,2)
print add(*params)

#对于参数字典的逆向使用，在逆向过程中*不是要收集参数，是在调用而不是在定义的时候使用
def hello(name,greeting):
    print '%s, %s%s' % (greeting,name,'!')
params1={'name':'Sir Robin','greeting':'Well met'}
hello(**params1)

