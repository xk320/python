#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 我们知道tuple可以表示不变集合，例如一个点的二维坐标可以表示成 p=(1,2)
# 但时很难看出这个tuple是用来表示一个坐标的。定义一个class又小题大做，这是namedtuple就派上用场：
# namedtuple是一个函数，他用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用数量而不是索引来引用tuple某个元素
# 这样一来，我们就用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print isinstance(p, Point)
print isinstance(p, tuple)
print p.x, p.y
