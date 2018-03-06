# -*- coding: UTF-8 -*-
# 在oop程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class成为子类（sunclass）
# 比如：
class Animal(object):
    def run(self):
        print 'Animal is running.....'


# 当我们需要编写Dog类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass


# 继承有上面好处？最大的好处是获得类父类的全部功能。
dog = Dog()
dog.run()

#也可以对子类增加一些方法
class Cat(Animal):
    def eat(self):
        print 'Eating meat.....'
    def run(self):
        print 'Cat is running.....'

#继承的第二个好处需要我们对代码做一点改进，无论是dog还是cat，它们run（）时候都是Animal is running.....，符合逻辑的做法是
#Dog is running.....    Cat is running.....
bbb=Cat()
bbb.run()
