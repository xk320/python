# -*- coding: UTF-8 -*-
import functools
def add(a,b):
    return a+b
print add(3,5)
print add(4,7)
#创建一个a的默认值是100的偏函数
adda100=functools.partial(add,100)
print adda100(2)