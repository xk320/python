#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#使用dict时，key是无序的，在对dict做迭代时，我们无法确定dict的顺序。如果要保持key的顺序，可以用OrderedDict
import collections
d = dict([('a',2),('b',4),('c',6)])
print d
od=collections.OrderedDict([('a',2),('b',4),('c',6)])
print od  # OrderedDict的Key是有序的
#OrderedDict的key会按照插入的顺序排列，不是key本身排序
odd=collections.OrderedDict()
odd['x']=3
odd['a']=3
odd['z']=3
print odd

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超过限制，先删除最早添加的key
class LastUpdateOrderedDict(object):
    pass
