#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#从模块导入函数的方法
#导入整个模块，引用的时候需要加模块的名字
# import math
# print math.abs(-4)

#导入整个模块，引用的时候不需要加模块的名字
# from math import *
# print fabs(-4)

#导入模块中的某一个函数，引用的时候不需要加模块的名字
# from  math import fabs
# print fabs(4)

#在语句末尾使用as子句，为整个模块提供别名或为函数提供别名
# import ConfigParser as cp
# config = cp.ConfigParser()
# from math import sqrt as foobar
# print foobar(4)