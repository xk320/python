# -*- coding: UTF-8 -*-
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用，能不能直接在实例本身上调用？
# 类似 instance()？在python中是可以的
# 任何类只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print ('My name is %s' % self.name)

    def run(self):
        print self.name


s = Student('LWM')
# __call__还可以定义参数，对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象
# 因为两者之间本来就没什么根本区别
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类对实例都是运行期创建出来的。
# 怎么判断一个变量是对象还是函数呢？其实，更多时候我们需要判断一个对象是否能被调用，能被调用的对象就是一个callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例：
print callable(Student)
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')

#通过()函数，可以判断一个对象是否是可调用对象

#总结
#python额class允许定义许多定制方法，可以让我们非常方便第生成特定的类
