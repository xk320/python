# -*- coding: UTF-8 -*-

# 如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir('123')

# 类似__xxx__的属性和方法在Python中都有特殊的用户，比如__len__方法返回的是长度，在python中如果你调用len()函数试图获取一个对象的长度，实
# 际在len内部它自动去调用该对象的__len__（）方法，所以下面的代码是等价的:
print '23'.__len__()
print len('23')


# 我们自己写的类，如果也想用len(myobj)的化，就自己写一个__len__()方法：
class Myobject(object):
    def __len__(self):
        return 100


obj = Myobject()
print len(obj)


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接直接操作一个对象的状态

class mobject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


mob = mobject()
print hasattr(mob, 'x')  # mob有属性x吗？
print hasattr(mob, 'y')  # mob有属性y吗？

setattr(mob, 'y', 19)  # 为对象mob设置y属性
print getattr(mob, 'y')  # 获取y属性

# 如果试图获取不存在的属性，会抛出AttributeError的错误,可以出入一个default参数，如果属性不再就返回默认值
try:
    getattr(mob, 'z')
except AttributeError as e:
    print e

print getattr(mob, 'z', 404)

# 也可以获取对象的方法
print hasattr(mob, 'power')  # 有属性power吗？

# 获取属性power
print getattr(mob, 'power')

# 获取属性power并赋值到变量fn
fn = getattr(mob, 'power')
print fn


# 总结
# 通过内置的一些列函数，我们可以对任何python对象进行刨析，拿到其内部的数据，要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
# 一个正确用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在则该对象是一个流，如果不存在，则无法读取。hasattr()就
# 派上了用场，请注意，在python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的字节流，但只要
# read()方法返回的是有效的图像数据，就不影响读取图像的功能
