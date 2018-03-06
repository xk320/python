# -*- coding: UTF-8 -*-
# python中lambda函数的作用
# 1、使用python写一些脚本时，使用lambda可以省区定义函数的过程，让代码更精简
# 2、对于一些抽象的，不会别的地方在复用的函数，有时候函数起个名字也是那题，使用lambda不需要考虑
# 3、使用lambda在某些时候让代码更容易理解

# lambda语句中，冒号前是参数，可以有多个用都好隔开，冒号右边是返回值，lambda语句构建的是一个函数
# 对象，如下：
g = lambda x: x ** 2
print g


def make_incrementor(n):
    return lambda x: x + n
m=make_incrementor(2)
n=make_incrementor(6)
print m(3),n(4)
print make_incrementor(22)(33)
