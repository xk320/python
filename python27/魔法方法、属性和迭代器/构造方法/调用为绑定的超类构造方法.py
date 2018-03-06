#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if  self.hungry:
            print 'Aaah.....'
            self.hungry = False
        else:
            print 'No,thanks!'
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb = SongBird()
print sb.hungry
sb.sing()
sb.eat()
sb.eat()
