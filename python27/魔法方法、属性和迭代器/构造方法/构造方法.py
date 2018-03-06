#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#构造方法时一个奇特的名字，它代表类似于以前例子中使用过的那种名为init的初始化方法。但是构造方法和其他普通方法不同的地方在于，
#当一个对象被创建后，会立即调用构造方法。

# f = FooBar()
# f.init()
# 构造方法能让他简化成如下形式：   f = Foobar()
#简单的构造方法：
class FooBar:
    def __init__(self):
        self.somevar = 42
f = FooBar()
print f.somevar

#可传参数的构造方法
class Foo:
    def __init__(self,value=42):
        self.vars = value
c = Foo('This is a new vars!')
print c.vars

