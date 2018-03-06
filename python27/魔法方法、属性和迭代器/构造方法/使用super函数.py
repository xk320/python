#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# super函数智能在新式类中使用。
# 注意，在python3.0中，super函数可以不带任何参数进行调用，功能依然具有魔力
__metaclass__ = type
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaah....'
            self.hungry = False
        else:
            print 'No,thanks!'
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()