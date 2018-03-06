#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#exec 语句最有用的地方在于可以动态的创建代码字符串，如果字符串是从其他地方获得的，很可能是用户，那么几乎不能确认其中到底
#包含什么代码，为了安全起见，可以增加一个字典，起到命名空间的 作用
#命名空间的概念，或称为作用域（scope），可以把他想想成保存变量的地方，类似于不可见的字典，在程序执行x=1这类语句时，
#将键x和值1放在当前的命名空间内，这个命名空间一般来说都是全局命名空间
from math import sqrt
scope={}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()

#eval会计算表达式并返回结果值
print eval(raw_input('Enter an arithmetic expression :'))
#eval也可以使用命名空间，尽管表达式几乎不像语句那样为变量重新赋值。eval可以提供两个命名空间，一个是全局的一个是局部的
#全局的必须是字典，局部的可以是任何形式的映射
#exec和eval语句提供命名空间是，还可以在真正使用命名空间前放置一些值进去
a = {}
a['x']=3
a['y']=4
print eval('x * y',a)

a = {}
exec 'x=9' in a
print eval('x*x',a)
