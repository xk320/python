#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#finally子句可以用来在可能的一场后进行清理，
# x = None
# try:
#     x = 1/0
# finally:
#     print 'cleaning up ....'
#     del x
#上面的代码中，finally子句肯定会被执行，不try子句中是否发生异常(在try子句之前初始化x的原因是如果不会这样做，由于
# ZeroDivisionError的存在，x就永远不会被赋值。这样就会导致在finally子句中使用del删除他的时候产生异常，而且整个异常时无法捕捉的 )
#因为使用del语句删除一个变量是非常不负责任的清理手段，所以finally子句用于关闭文件或者网络套接字时会非常有用，还可以在同一条局域
# 中组合使用try、except、finally和else
try:
    1/0
except ZeroDivisionError as e:
    print e
else:
    print 'That went well!'
finally:
    print 'Cleaning up.'