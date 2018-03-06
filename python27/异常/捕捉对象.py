#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#如果希望在except子句中访问异常对象本身，可以使用两个参数。
#就算是要捕捉多个异常也只需向except提供一个参数---- 一个元组
#注意：在python3.0中  except子句会被写作  except (ZeroDivisionError,NameError,SyntaxError,TypeError) as e
# try:
#     x = input('Enter the first number:  ')
#     y = input('Enter the second number: ')
#     print x/y
# # except (ZeroDivisionError,NameError,SyntaxError,TypeError),e:
# except Exception,e:
#     print e
#下列循环中没有异常引发的情况下参会退出，换句话说，只要有错误发生，程序会不断的要求重新输入。
while True:
    try:
        x = input('Enter the first number:  ')
        y = input('Enter the second number: ')
        print x/y
    except Exception as e:
        print e
    else:
        break