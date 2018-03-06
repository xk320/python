#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 第四种方式就是启动python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态，
s = '0'
n = int(s)
print 10 / n
# 然后启动：
#
# $ python -m pdb err.py
# > /Users/michael/Github/sicp/err.py(2)<module>()
# -> s = '0'
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
# 这种通过pdb在命令行调试的方法理论上是万能的，但如果有一千行代码，要运行到第999行得敲多少命令，还有另一种调试方法。
#
# pdb.set_trace()
#
# 这个方法也是用pdb，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
#
# # err.py
# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print 10 / n
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
#
# $ python err.py
# > /Users/michael/Github/sicp/err.py(7)<module>()
# -> print 10 / n
# (Pdb) p n
# 0
# (Pdb) c
# Traceback (most recent call last):
#   File "err.py", line 7, in <module>
#     print 10 / n
# ZeroDivisionError: integer division or modulo by zero
# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。
