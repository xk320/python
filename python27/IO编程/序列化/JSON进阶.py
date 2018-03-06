# -*- coding: UTF-8 -*-
# python的dict对象可以直接序列化JSON的{}，不过很多时候我们更喜欢用class表示对象，比如定义一个Student类，然后序列化：
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Jam', 18, 89)


# print json.dumps(s)
# 代码执行肯定报错，TypeError，错误原因是Student对象不是一个可反序列化的JSON对象
# 我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
# https://docs.python.org/2/library/json.html#json.dumps
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSO，是因为默认情况下dumps()方法不知道如何将Student
# 实例变成一个JSON的{}对象。可选参数default就是把任意一个对象变成一个可序列化JSON的对象，我们只需要为Student转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print json.dumps(s, default=student2dict)
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。
# 不过下次如果遇到Teacher类的实例，照样无法序列化为JSO，我们可以偷个懒，把任何class的实例变为dict：
b = json.dumps(s, default=lambda obj: obj.__dict__)
print b
f = '{"age": 18, "score": 89, "name": "Jam","classroom":"三年一班"}'


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量，比如定义类__slots__的class
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换一个dict对象，然后我们传入object_hook函数负责把dict转
# 换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


c = json.loads(f, object_hook=dict2student)
print c

# 小结
# python语言特定的序列化模块是pickle，但是如果要把序列化高得更通用、更符合web标准，就可以使用json模块
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足
# 我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
