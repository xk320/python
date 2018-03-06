#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#并行迭代  程序可以同时迭代两个序列
a=['anne','beth','george','damon']
b=[12,45,32,102]
for i in range(len(a)):
    print a[i],'is',b[i],'year old'
#内建zip函数可以用来并行迭代, zip函数将两个列表压缩并返回一个元素列表
for key,value in zip(a,b):
    print key,'is',value,'year old'
#zip函数可以处理不等长的序列，当最短的序列用完时就会自动停止
print zip(range(5),xrange(100000))
#不推荐使用range替换xrange，range会计算所有的数字，这个要花费很长的 时间。

#按索引迭代 enumerate函数返回索引与值的键值对
print a
for index,string in enumerate(a):
    if 'n' in string:
        a[index]='hahaha'
print a

#翻转和排序迭代
#reversed和sorted同列表的reverse和sort方法类似，作用域任何序列和可迭代对象上，不是原地修改对象，而是返回翻转或排序后的版本
print sorted('Hello World!')
#reversed返回的是一个对象
print list(reversed('Hello World!'))




