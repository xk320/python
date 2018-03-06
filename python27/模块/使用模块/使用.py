# -*- coding: UTF-8 -*-

# python本身就内置类很多非常拥有的模块，只要安装完毕，这些模块就可以立即使用
# 我们一内建的sys模块为例，编写一个hello的模块：

# 表示模块的文档解释，任何模块代码的第一个字符串都被是为模块的文档注解
' a test module '

# __author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
__author__ = 'LWM'

# 导入sys模块，我们就有类变量sys只想该模块，利用sys这个变量，就可以访问sys模块的功能
import sys


def test():
    # sys模块有一个argv变量，用list存储类命令行的所有参数，argv至少有一个元素，因为第一个参数永远是该py文件的名称
    args = sys.argv
    print args[0].decode('utf8')
    if len(args) == 1:
        print 'Hello World!'
    elif len(args) == 2:
        print 'Hello %s!' % args[1]
    else:
        print 'Too many arguments!'


# 当我们在命令航运行模块文件时，python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断失败，因此这🀄️种
# if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()

