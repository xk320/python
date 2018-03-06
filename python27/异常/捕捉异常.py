#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#关于异常的最优意思的地方就是可以处理他们，这个功能可以使用try/except语句来实现。
#假设创建了一个让用户输入两位数，然后进行相处的程序，如下：
# try:
#     x = input('Enter the first number: ')
#     y = input('Enter the second number: ')
#     print x/y
# except ZeroDivisionError:
#     print 'The second number can`t be zero!'
#如果捕捉到异常，但又想重新引发他，那么可以调用不带参数的raise
#当计算器没有打开屏蔽机制时，ZeroDivisionError被捕捉但已传递了。
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            print eval(expr)
            return
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illega!'
            else:
                raise
calculator = MuffledCalculator()
calculator.muffled=True
calculator.calc('10/0')
