#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#链式赋值是将一个变量同时赋值给多个变量的方法
a = 10
x = y = a
print x , y
#相当于 y=a   ,x=y

#增量赋值们没有将赋值表达式写成x=x+1  ，而是将表达式运算符放在赋值运算符=的左边写成x+=1，这种就叫增量赋值
#对于*  /  % 等标准运算符都使用
x = 2
x += 1
print x
x %= 2
print x
#对于其他数据类型也适用，增量赋值可以让代码更加紧凑和简练，
fnord = 'foo'
fnord += 'bar'
print fnord
fnord *= 2
print fnord