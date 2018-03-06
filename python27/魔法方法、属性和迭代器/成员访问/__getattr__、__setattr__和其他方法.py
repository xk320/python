# -*- coding: UTF-8 -*- 
#拦截（intercept）对象的所有特性访问是可能的，这样可以用旧式类实现属性（因为property方法不能使用）。
#为了在访问特性的时候可以执行代码，必须使用一些魔法方法。下面的4中方法提供类需要的功能
#__getattribute__(self,name):当特性那么被访问时自动被调用（只能在新式类中使用）。
#__getattr__(self,name):当特性name被访问且对象没有响应的特性时被自动调用。
#__setattr__(self,name,value):当试图给特性name赋值时会被自动调用
#__delattr__(self,name):当试图删除特性name时被自动调用
#尽管和使用property函数相比有点复杂，但这些特殊方法时很强大的，因为可以处理很多属性的方法进行在编码

class   Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
#__setattr__方法在所设计的特性不是size时也会被调用，因此，这个方法必须把两方面都考虑进去，如果属性时size，那么就行前面那样执行操作，否则
#就要使用特殊方法__dict__，该特殊方法包含一个字典，字典里面时所有实例的属性，为了避免__setattr__方法被再次调用，__dict__方法被用来代替
# 普通特性赋值操作
    def __setattr__(self, name, value):
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value
#__getattr__方法值在普通的特性没有找到的时候调用，这就是说如果给她的名字不是size，这个特性不存在，这个方法会引发一个AttributeError异常
#，如果希望类和hasattr或者时getattr这样的内建函数一起正确的工作，__getattr__方法就很重要，如果使用的时size属性，就会使用前面的实现中找
# 到的表达式
    def __getattr__(self, name):
        if name == 'size':
            return self.width,self.height
        else:
            return AttributeError
        
#就像死循环陷阱和__setattr__有关系一样，还有一个陷阱和__getattribute__有关系，因为__getattribute__拦截所有特性的访问（在新式类中），
# 也拦截__dict__的访问，访问__getattribute__中与self相关的特性时，使用超类的__getattribute__方法（使用super函数）时唯一安全的路径。