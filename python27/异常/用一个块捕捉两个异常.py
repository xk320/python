#!/usr/bin/env python
# _*_ coding:utf-8 _*_
try:
    x = input('Enter the first number:  ')
    y = input('Enter the second number: ')
    print x/y
except (ZeroDivisionError,TypeError,NameError):
    print "Your numbers were bogus..."
#上面代码中，如果用户输入字符串或者其他类型的值，而不是数字，或者第二个数为0，都会打印同样的错误信息。
#当然，值打印一个错误信息并没有什么帮助，另外一个方案就是继续要求输入数字直到可以进行除法运算位置。