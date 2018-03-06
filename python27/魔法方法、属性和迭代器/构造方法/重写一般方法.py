#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#重写一般方法
class A:
    def hello(self):
        print 'Hello,I`m A.'
class B(A):
    def hello(self):
        print 'Hello,I`m B.'
#重写是集成机制中的一个重要的内容，对于构造方法尤其重要。构造方法用来初始化新创建对象的状态，大多数子类不仅要拥有自己的初始化代码，
#还要拥有超类的初始化代码。虽然重写的机制对于所有方法来说都是一样的，但是当处理构造方法比重写普通方法时，更可能遇到特别的问题：
# 如果一个类的构造方法被重写，那么就需要调用超类的构造方法，否则对象可能不会被正确地初始化,示例如下：
#在这个类中定义所有鸟都具有的一些最基本的能力，吃
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if  self.hungry:
            print 'Aaah.....'
            self.hungry = False
        else:
            print 'No,thanks!'
#现在考虑子类SongBird，添加唱歌的行为
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
sb.eat()
#在子类中调用eat方法时出现异常错误，原因是在SongBird中，构造方法被重写，但新的构造方法没有任何关于初始化hungry特性的代码。
#为了达到预期的效果，SongBird的构造方法必须调用其超类的构造方法来确保进行基本的初始化，有两种方法能达到这个目的：
#调用超类构造方法的未绑定版本，或者使用super函数。


