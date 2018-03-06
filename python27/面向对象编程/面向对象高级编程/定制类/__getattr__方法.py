# -*- coding: UTF-8 -*-
# __getattr__
# 正航情况下，当我们调用类的方法或属性时，如果不存在就会报错，比如定义Stu类：
class Stu(object):
    def __iter__(self):
        self.name = 'python'


s = Stu()
try:
    print s.score
except Exception as e:
    print e


# 要避免上述错误，处理可以增加一个score属性外，python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性，如下：
class Lsn(object):
    def __init__(self):
        self.name = 'JAVA'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        elif item == 'age':
            return 22


# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
l = Lsn()
print l.score


# 注意，只有在没有找到属性的情况下，才调用__getattr__，此外注意调用如l.abc会返回None，这是因为我们定义的__getattr__默认返回None，要是
# 让class只响应特定的几个属性，我们就要按照约定，抛出AttrbuteError的错误：
class LL(object):
    def __getattr__(self, item):
        if item == 'age':
            return 999
        raise AttributeError('Error!')


# 这实际上可以把一个类的所有属性和方法全部动态化处理了，不需要任何特殊手段。这种完全动态处理的特性有什么实际作用呢？作用就是可以针对完全动
# 态的情况作调用
# 举个例子：现在有很多网站都搞REST AP，比如新浪微博，调用api的URL类似：http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那么得累死，而且API一旦改动，SDK也要更改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list
# 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且不随API的增加而改变
# 还有些REST API会把参数放到URL中，比如GitHub的AP：
# GET /users/:user/repos
#调用是，需要把:user替换为实际用户名，如果我们能写出这样的链式调用：Chain().users('michael').repos,就可以非常方便第调用API了
