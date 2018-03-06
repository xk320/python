# -*- coding: UTF-8 -*-
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历成为迭代（lteration）
#在python中，迭代是通过for 。。。 in 来完成的，而很多语言比如C或者java，迭代list是通过下标完成的：
#比如java代码：
# for (i=0,i<list.length;i++){
#     n = list[i]
# }
#可以看出，python的for循环抽象程度要告诉java的for循环，因为python的for循环不仅可以用在list或tuple上，
#还可以作用在其他可迭代的对象上。
#list这种数据理性虽然有下标，但是很多其他数据类型是没有下标的，但是只要是可迭代对象，无论有无下标，都可以
#迭代，比如dict就可以迭代：
d={'a':1,'b':2,'c':3}
for key in d:
    print key
#因为dict的存储不是按照list的方式顺序排列，所以迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代是key，如果要迭代value可以用 for value in d.itervalues()
#如果同时迭代key和value，可以用for 　k,v in d.iteritems()
for v in d.itervalues():
    print v
#由于字符串也可以是迭代对象，因此也可以用for循环：
for c in 'ABC':
    print c

#所以当我们使用for循环时，只要作用与一个可迭代对象，for循环就可以正常运行，而且我们不台关心该对象
#究竟是list还是其他类型数据，那么，如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的lterable类型判断
from  collections import  Iterable
print isinstance('abc',Iterable)

#如果要对list实现类似java那样下标循环，python内置enumerate函数可以吧list编程索引-元素对
for i,value in enumerate(['a','b','c']):
    print i,value

#python中任何迭代对象都可以用于for循环，包括我们自定义的数据类型，只要符合迭代条件就可以