#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#尽管内建的异常类已经包括了大部分情况，而且对于很多要求都已经足够了，但有些时候还是需要创建自己的异常类。
#只要确保从Exception类继承（不管是直接的或者是间接的，也就是所继承其他的内建异常类也是可以的）。
class SomeGustomExceptions(Exception):
    pass
