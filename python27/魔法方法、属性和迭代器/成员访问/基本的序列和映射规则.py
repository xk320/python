#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#序列和映射是对象的集合。为了实习三他们基本的行为（规则），如果对象时不可变的，那么就需要使用两个魔法方法，如果是可变的则需要使用4个
#__len__(self) 这个方法应该返回集合中所含项目的数量，对于序列来说，就是元素的个数，对于映射来说，则是键值对的数量。
#__getitem__(self) 这个方法返回与所给的键对应的值，对于序列，键应该是一个0- n-1的证书，n是序列的长度，对于映射来说，可以使用任何种类的键
#__setitem__(self) 这个方法应该按一定的方法存储和key相关的valuse，该值随后可使用__getitem__来获取，当然，智能为可以修改的对象定义这个方法
#__delitem__(self) 这个方法在对一部分对象使用del语句时被调用，同时必须删除和键相关的键，这个方法也是为可以修改的对象定义的
#对于这些方法的附加要求如下：
#   对于一个序列来收，如果键时负整数，那么要从末尾开始计数。
#   如果键是不合适的类型，会引发一个TypeError异常
#   如果序列的索引时正确的类型，但超出了范围，应该引发一个IndexError异常
def checkIndex(key):
    """
    所给的键是能接收的索引吗？
    为了能被接收，键应该是一个非负的证书，如果他不是一个证书，会引发TypeError；，如果他是一个负数，则会引发IndexError
    :param key:
    :return:
    """
    if not isinstance(key,(int,long)):
        raise TypeError
    if key < 0 :
        raise IndexError
class AritheticSequence:
    def __init__(self,start=0,step=1):
        """
        初始化算数序列，
        :param start:初始值
        :param step: 步长
        """
        self.start = start
        self.step = step
        self.changed = {}
        self.listd = [1,3,2,3,2,1,4]
    def __getitem__(self, key):
        """
        Get an iten from the arithmetic sequence
        :param key:
        :return:
        """
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self, key, value):
        """
        修改算数序列中的一个项
        :param key:
        :param value:
        :return:
        """
        self.changed[key] = value

    def __delitem__(self, key):
        """
        :param key:
        :return:
        """
        print self.changed[4],'-----'
        print self.changed
        del self.changed[key]
        print self.changed


s = AritheticSequence(1,2)
print s[4]
s[4]=2
print s[4]
print s[5]
del s[4]
print s[4],'delete'
print len(s.listd)


