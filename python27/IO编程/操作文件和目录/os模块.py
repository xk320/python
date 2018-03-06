# -*- coding: UTF-8 -*-
# 如果我们要操作文件、目录可以在命令行下面输入操作系统提供的各种命令来完成，比如dir、cp命令
# 如果要在python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用来操作系统提供的接口函数，python内置的os模块也可
# 以直接调用操作系统提供的接口函数
import os

print os.name  # 操作系统的名字
# posix说明是linux、unix 或者MAC OS ，如果是nt就是Windows系统
# 要获取详细的系统信息，可以调用uname()函数
print os.uname()
# 注意uname函数在windows上不提供，也就是说os模块的某些函数是跟操作系统相关的。

#环境变量
#在操作系统中定义的环境变量，全部保存在environ这个dict中，可以直接查看
print os.environ
#要获取某个环境变量的值，可以调用getenv()函数：
print os.getenv('PATH')
print os.getenv('PYTHONPATH')