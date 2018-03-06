#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#下列两个语句等阶，都创建了返回参数平方的函数，
def foo(x):
    return x*x
bar=lambda x:x*x
print foo(8)
print bar(8)

#定义类是，所以位于class语句中的代码都在特殊的命名空间中执行-----类命名空间（class namespace）
#这个命名空间可有类内所有成员访问，并不是所有Python程序员都知道类的定义其实就是执行代码块，在类的定义区并不只限定只能使用def语句
class C:
    print 'Class C being defined.....'

class MemberCounter:
#在类的作用域内声明一个可供所有成员访问的变量
    members=0
    def init(self):
        MemberCounter.members+=1
        return self.members
m1=MemberCounter()
print m1.init()
m2=MemberCounter()
print m2.init()
#新的members值被写到m1的特性中，屏蔽了类范围内的变量
m1.members='name'
print m1.members
print m2.members

