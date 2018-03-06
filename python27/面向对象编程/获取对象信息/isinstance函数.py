# -*- coding: UTF-8 -*-
# 对于class的继承关系来说，使用type()就很不方便，我们要判断class类型可以使用isinstance()函数
class AAA(object):
    def run(self):
        print 'aaa'


class BBB(AAA):
    def run(self):
        print 'bbb'


class CCC(AAA):
    def run(self):
        print 'ccc'


class DDD(CCC):
    def run(self):
        print 'ddd'
a=AAA()
b=BBB()
c=CCC()
d=DDD()

#isinstance()可以告诉我们，一个对象是否是某中类型，
print isinstance(a,AAA)
print isinstance(b,AAA)
print isinstance(d,AAA)
print isinstance(d,CCC)
print isinstance(d,BBB)

#type()能判断的 所有基本类型isinstance()也可以判断：
print isinstance(123,int)
print isinstance('123',str)
