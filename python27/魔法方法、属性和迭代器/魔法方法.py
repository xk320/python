#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#在python中，有的名称会在前面和后面都加上两个下划线，这种写法很特别，前面几章中已经出现过一些这样的名称，这种拼写标识名字
#名字有特殊含义，所以绝不要在自己的程序中使用这种名字。在python中，由这些名字组成的集合所包含的方法称为魔法方法。
#为了确保类是新型的，应该把赋值语句__metaclass__=type放在你的模块的最开始或者子类化内建类object。
class NewStyle(object):
    '''hahahhahahah'''
    def pppp(self):
        print '111111111111111'
class OldStyle:
    pass
#在上文中的两个类，一个是新式的类一个是旧式的类。如果文件以__metaclass__=type开始，那么两个类都是新式的类。
#除此之外，在可以在自己的类的作用域中对__metaclass__变量赋值，这样只会为这个类设定元素。元素是其他类的类，这是个更高级的主题。
#注意：在Python3.0中没有旧式的类，也不需要显式地子类化object或者将元素设置为type。所有的类都会隐式地成为object的子类。
#如果没有明确超类的话，就会直接子类化
c = NewStyle()
print c.__doc__

