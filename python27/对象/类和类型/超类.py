#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#将其他类名写到class语句后的圆括号就可以指定超类
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked=['SPAM']
#检查一个类是否是另一个类的子类，返回布尔值
print issubclass(SPAMFilter,Filter)
print issubclass(Filter,SPAMFilter)

print issubclass(SPAMFilter,Filter)
print SPAMFilter.__bases__

#-----------------多重继承----------------
#多重集成是非常有用的工具，当使用多重集成是，有个需要主机的地方是如果一个方法从多个超类继承，那么必须要注意超类的顺序，先继承的类中
#方法会重写后继承类中的方法
class Calculator:
    def calculate(self,expreesion):
        self.value=eval(expreesion)

class Talker:
    def talk(self):
        print 'Hi,my value is',self.value

class TalkingCalculator(Calculator, Talker):
    pass
a = TalkingCalculator()
a.calculate('1*2*3')
a.talk()