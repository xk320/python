# -*- coding: UTF-8 -*-
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass，metaclass直译为元类，简单解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
# 连接起来就是先定义metaclass，就可以创建类，最后创建实例
# 所以，metaclass允许你创建或者修改类，换句话说，你可以把类看成metaclass创建创建出来的实例。
# metaclass是python面向对象的最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，
# 所以一下内容看不懂没关系，基本上不会用到。

# 一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add的方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚第表示这是一个metaclass

# metaclass是创建类，所以必须从type类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    # 指示使用ListMetaclass来定制类
    __metaclass__ = ListMetaclass


# 当我们写下__metaclass__=ListMetaclass语句时，魔术就生效了，它指示python解释器在创建Mylist时，要通过ListMetaclass.__new__()
# 来创建，再次，我们可以修改类的定义，比如加上新的方法，然后返回修改后的定义
# __new__()方法接收到参数依次是：
# 1、当前准备创建的类的对象
# 2、类的名字
# 3、类继承的父类集合
# 4、类的方法集合
L = MyList()
L.add(1)
print L
# 普通的list没有add()方法
l = list()
try:
    l.add(2)
except Exception as e:
    print e


# 动态修改有什么意义？直接在MyList定义中写上add () 方法不是更简单，正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是总会遇到通过metaclass修改类的定义的。ORM就是一个典型的例子
# ORM全称 Object Relational Mapping 即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，
# 写代码就更简单，不用直接操作SQL语句
# 要编写一个ORM框架，所有的类只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
# 尝试编写一个ORM框架
# 编写底层模块的第一步，就是先把调用接口写出来，比如使用者如果使用换个ORM框架，想定义一个user类来操作对应的数据库表User，我们
# 期待它写出这样的代码：
# class User(Model):
#     #定义类的属性到列的映射：
#     id=IntegerField('id')
#     name=StringField('name')
#     email=StringField('email')
#     password=StringField('password')
#
# #创建一个实例：
# u=User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')
# #保存到数据库：
# u.save()
# 其中，父类Model和属性类StringField、IntegerField是又ORM框架提供的，剩下的魔术方法比如save()全部🈶️metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来去异常简单。
# 现在就按上面的接口来实现ORM
#
# 首先来定义Field类，它负责保存数据库表的字段和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField、IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'vachar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 下一步，就编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print ('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 假设表明和类型一致
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)


# 基类
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            raise AttributeError(r"'Model' object has on attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print ('SQL: %s' % sql)
        print ('ARGS: %s' % str(args))

        # 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__，如果没有找到，就继续父类Model
        # 中查找__metaclass__,找到了就使用Model中定义的__metaclass__的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地
        # 继承到子类，但子类自己却感觉不到。
        # 在ModelMEetaclass中，一共做了几件事情：
        # 1、排除掉对Model类对修改
        # 2、在当前类（比如User）中查找定义的类的所有属性，如果找到类Field属性，就把它保存在一个__mappings__的dict中，同时，从属性中
        #    删除该Field属性，否则容易造成运行错误
        # 3、把表名保存到__table__中，这里简化为表明默认类名
        # 在Model类中，就可以定义各种操作数据库的方法，比如save(),delete(),find(),update()等等
        # 我们实现类save()方法，把一个实例保存到数据库中，因为有表名，属性到字段的映射和属性值的集合，就可以构造出insert语句


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()


# 可以看到，save()方法已经打印出可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL就可以完成真正的功能。
# 不到100行代码，我们就通过metaclass实现了一个精简的ORM框架，完整的代码从这里下载：
# https://github.com/michaelliao/learn-python/blob/master/metaclass/simple_orm.py
# 最后解释一下类的属性和实例属性，直接在class定义的是类属性：
class Student(object):
    name = 'Student'


# 实例属性必须通过实例来绑定，比如self.name='xxx'
s = Student()
s.name = 'XXXZ'
print s.name
# 因此，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字
# 在我们编写ORM中，ModelMetaclass会删除掉User的所有类属性，目的就是避免造成混淆。
