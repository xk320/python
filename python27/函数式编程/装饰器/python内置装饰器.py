# -*- coding: UTF-8 -*-
# 在python中有三个内置装饰器，都是跟class相关的，staticmethod、classmethod和property
# staticmethod是类静态方法，其跟成员方法的区别是没有self参数，并且可以在类不进行实例化的情况下调用
# classmethod与成员方法的区别在于所接收的第一个函数不是self（类实例的指针）而是cls（当前类的具体类型）
# property是属性的意思，表示可用通过类实例直接访问的信息

class Foo(object):
    def __init__(self,var):
        super(Foo,self).__init__()
        self._var=var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self,var):
        self._var=var

fo=Foo('var 1')
print fo.var
fo.var='var2'
print fo.var

#注意，对于python新式类如果将上面的@var.setter装饰器所装饰的成员函数去掉，则foo.var属性为只读属性，
#使用foo.var='var2'进行赋值时会抛出异常，