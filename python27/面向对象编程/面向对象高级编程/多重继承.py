# -*- coding: UTF-8 -*-

# 继承是面向对象编程一个重要的方式，因为通过继承，子类就可以扩展父类的功能
# 假设我们要实现一下4种动物：Dog 狗狗、Bat 蝙蝠 、Parrot  鹦鹉、  Ostrich  鸵鸟
# 按照哺乳动物归类和鸟类归类，按照能跑和能飞，我们可以设计出不同的层次结构，如果将两种情况都涵盖进来我们将设计更多的层次结果
# 哺乳类： 能跑的  、能飞的
# 鸟类： 能跑的  能飞的
# 如果在加宠物类和非宠物类，类的数量会几何倍的增长，很明显这么设计是不行的
# 正确的做法是采用多重继承，首先主要的类层次仍然是哺乳类和鸟类的设计
import SocketServer
import threading

class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 现在，我们要给动物在加上Runnable和Flyable的功能，只需要定义好Runnable和Flyable的类：


class Runnable(object):
    def run(self):
        print 'Running......'


class Flyable(object):
    def run(self):
        print 'Flying......'


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Pig：
class Pig(Mammal, Runnable):
    pass


# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bas：
class Bas(Bird, Flyable):
    pass

# Mixin
# 在设计类的继承关系时，通常主线都是单一继承下来的，例如，Ostrich继承自Bird，但是如果需要混入额外的功能，通过多重继承就可以实现。
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常较多Mixin
# Mixin的目的就是给一个类增加多个功能，这样在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系
# Python自带的很多库也使用来Mixin，举个例子，python自带的TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或者
# 多线程模式，这两种模型由ForkingMixin和ThreadingMixin提供，通过组合，我们就可以创造出合适的服务来。
# 比如编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(SocketServer.TCPServer,SocketServer.ForkingMixIn):
    pass
#想编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(SocketServer.UDPServer,SocketServer.ThreadingMixIn):
    pass
#如果打算高一个更先进的协程模型，可以编写一个CoroutineMixin：
# class MyTCPServer(SocketServer.TCPServer,CoroutineMixin):
#     pass

#总结
#由于python允许使用多重继承，因此Mixin是一种常见的设计，只允许单一继承的语言（如java）不能使用Mixin的设计

