#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#接口的概念与多态有关，在处理多态对象时，只要关心它的接口即可，也就是公开的方法和特性。在Python中，不用显式低指定对象必须
#包含哪些方法才能作为参数接收
class Calculator:
    def calculate(self,expreesion):
        self.value=eval(expreesion)

class Talker:
    def talk(self):
        print 'Hi,my value is',self.value

class TalkingCalculator(Calculator, Talker):
    pass
a = TalkingCalculator()
#判断方法是否存在
print hasattr(a,'talk')
print hasattr(a,'Font')

#判断方法是否能被调用
#--------2.0------------
print callable(getattr(a,'talk',None))
print callable(getattr(a,'fond',None))
#---------3.0---------------
