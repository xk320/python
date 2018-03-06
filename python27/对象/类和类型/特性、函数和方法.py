#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# self参数试试上正式方法和函数的区别。
# 方法将他们的第一个参数绑定到所属的实例上，因此无需显示提供该参数，
__metaclass__=type
class Bird:
    song='Squaawk!'
    def sing(self):
        print self.song
bird=Bird()
bird.sing()
#尽管下列的方法看起来与函数调用十分相似，但是变量birdsong引用绑定方法binrd.sing上，
#也就意味着还是会对self参数进行访问
birdsong=bird.sing
birdsong()

#私有化
class Person:
    def setName(self,name):
        self.name=name
    def getNmae(self):
        return self.name
    def greet(self):
        print 'Hello World!I`m %s.' % self.name
#下边的例子是程序从外部访问一个对象的特性
c=Person()
c.setName('Tom')
print c.name
c.name='Lucy'
print c.getNmae()
#不同观点：SmallTalk认为上边的例子破坏了封装的原则，他认为对象的状态对于外部应该是完全隐藏（不可访问）的
#使用私有特性private 外部对象无法访问，但是内部能够访问。Python并不直接支持私有方式
#达到私有特性效果的小技巧
#为了让方法或者特性变成私有的，只要在他的名字前面加上双下划线即可
class Secretive:
    def __inaccessible(self):
        print "Bet you can't see me ...."
    def accessible(self):
        print "The secret message is ..."
        return self.__inaccessible()
#现在__inaccessible从外界是无法访问的，而在类的内部还能使用访问
s=Secretive()
#s.__inaccessible无法直接访问执行报错
s.accessible()

#类的内部定义中，所有以爽下划线开始的名字都被翻译成前面加上单下划线和类名的形式
#实际上还是能在类外访问这些私有方法的，尽管不应该这么做
#Python中确保其他人不会访问对象的方法和特性使不可能的，但是这个类名称变化术就是他们不应该访问这些函数或者特性的信号
s._Secretive__inaccessible()