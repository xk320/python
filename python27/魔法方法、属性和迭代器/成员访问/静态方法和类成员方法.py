# -*- coding: UTF-8 -*-
#静态方法和类成员方法分别在创建时分别被装入staticmethod类型和classmethod类型的对象中。
#静态方法的定义没有self参数，切能够被类本身直接调用。类方法在定义时需要名为cls的类似于self的参数。
#类成员方法可以直接用类的具体对象调用。但cls参数是自动被绑定到类的
__metaclass__ = type
class Myclass:
    @staticmethod
    def smeth():
        print 'This is a static method'
    smth = staticmethod(smeth)
    @classmethod
    def cmeth(cls):
        print "This is a class method of",cls
    cmeth = classmethod(cmeth)

# Myclass.cmeth()
Myclass.smeth()
Myclass.cmeth()
