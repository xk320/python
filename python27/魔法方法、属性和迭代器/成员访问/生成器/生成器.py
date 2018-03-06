# -*- coding: UTF-8 -*-
#生成器是python新引入的概念，他也叫简单生成器。他和迭代器可能是近几年来引入的最强大的两个特性。但是，生成器的概念要更高级一些，需要花写功
# 夫才能理解它是如何工作的以及它有什么作用。升级成可以帮助读者写出非常优雅的呃代码，当然，便携式任何程序是不使用生成器也是可以的 。
#生成器是一种用普通函数语法定义的迭代器，它的工作方式可以用列子来很好的展现
#1、创建生成器，
# 首先创建一个展开嵌套列表的函数，参数是一个列表
nested = [[1,2],[3,4],[5]]
#这个函数大部分是简单的容易理解的，这里的yield语句是新知识，任何包含yield语句的函数成为生成器。除了名称不同，它和普通函数的行为也有很大差
# 别，这就在与它不像return那样返回值，而是每次产生多少值。每次产生一个值（使用yield语句）函数就会被冻结：即函数停在那点等待重新被唤醒，函
# 数被重新唤醒后就从停止的那个点开始执行
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
# for line in flatten(nested):
#     print line

nested1 = [[6,7],[8,9]]
for line in flatten(nested1):
    print line
