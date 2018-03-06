# -*- coding: UTF-8 -*-
#列表声称式即List Comprehensions，是python内置的非常简单却强大的可以用来创建list的生成式
#举个例子，要生成list[1,2,3,4,5,6,7,8,9,10]可以用 range(1,11)
print range(1,11)

#但是如果要生成[1x1,2x2,3x3,...,10x10]
#方法一循环：
L=[]
for x in range(1,11):
    L.append(x*x)
print L

#方法二，列表生成式
print [x*x for x in range(1,11)]
#写列表生成式时，吧要生成的元素x*x放到前面，后边for循环，就可以把list创建出来

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print [x*x for x in range(1,11) if x % 2 ==0]

#还可以使用两层循环，可以生成全排列
print [n+m for n in 'ABC' for m in 'abc']

#实例一，列出当前目录下所的所有文件和目录眀，可以通过一行代码实现
import os
print [d for d in os.listdir('.')]

#列表生成式也可以使用两个变量来生成list
d={'x':'A','y':'B','z':'C'}
print [k+'='+v for k,v in d.iteritems() ]

#将list中所有的字符串变成小写
A=['HELLO','WORLD','ORACLE','APPLE','DELL','IBM']
print [d.lower() for d in A]
B=[123,23,2,'a','ab','c']
print [str(d).lower() for d in B]
