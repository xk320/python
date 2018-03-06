#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#多个赋值操作可以同时进行
x,y,z = 1,2,3
print x,y,z
#可以交换两个变量的值
x,y = y,x
print x,y,z
#序列解包(递归解包）  将多个值的序列解开，然后放在变量的序列中。
#所解包的序列中的元素数量必须和放置在赋值符号左边的变量数量完全一致。
values=[4,5,6]
x,y,z = values
print x
scoundrel = {'name':'Robin','girlfriend':'Marion'}
key,value = scoundrel.popitem()
print key,value