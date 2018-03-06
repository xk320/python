#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# python中可以自动执行写在注释中的代码
# 当我们编写注释时，如果写上这样的注解无疑更明确地告诉函数的调用者 函数的期望输入和输出：
def abs(n):
    '''
    Function to get absolute value of number:
    Example
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)


# python 内置文档测试 doctest 模块可以直接提取注释中的代码并执行测试。
# doctest严格按照python交互命令行的输入和输出来判断结果是否正确，只有测试异常的时候，可以用...表示中间一大段烦人的输出
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # 什么输出也没有。这说明我们编写的doctest运行都是正确的。如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错：
    # 注意到最后两行代码，当模块正常导入时，doctest不会被执行，只有在命令行运行时才执行doctest，所以不必担心doctest会在非测试
    # 环境下执行。
