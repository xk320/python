#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#clear 方法 清除字典中所有的项
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print (d)
returned_value = d.clear()
print returned_value
#x和y最初对应同一个字典，x关联到一个新的空字典来清空x，对y一点影响都没有
x = {}
y = x
x['key'] = 'value'
print (y)
x = {}
print (y)
#x和y最初对应同一个字典，x通过clear方法进行清空后，y同时也被清空
x = {}
y = x
x['key'] = 'value'
print (y)
x.clear()
print (y)

#copy 方法 copy方法返回一个具有相同键值对的新字典（浅复制）
#浅复制，当副本中替换值的时候，原始字典不受影响，但是如果修改了某个值，原始的字典也会改变
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'guset'
y['machines'].remove('bar')
print (x)
print (y)
#deepcopy 深复制
from copy import deepcopy
d = {'names':['Alfred','Bertrand']}
#浅复制
c = d.copy()
#深复制
e = deepcopy(d)
d['names'].append('Clive')
print (c)
print (e)

#fromkeys 方法  使用给定的键建立新的字典，每个键都对应一个默认的值，默认None，可指定默认值
print ({}.fromkeys(['A','b','c']))
print (dict.fromkeys(['A','b','c']))
#指定默认值
print (dict.fromkeys(['A','b','c'],'default'))

# get 方法  更宽松的访问字典项的方法，一般来说，在访问字典中不存在的项时不会出现任何异常，而是得到None值，还可以自定义默认值
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
#字典中没有HAHAHA  返回None
print (b.get('HAHAHA'))
#字典中没有HAHAHA，返回hhhhh
print (b.get('HAHAHA','hhhhh'))

#items 方法 将字典所有项以列表的形式返回
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print (b.items())
#iteritems 方法与items基本相同，但是返回的是一个迭代器对象而不是列表
print (b.iteritems())

#key 方法 将字典中的键以列表的形式返回， iterkeys则返回针对键的迭代器
print (b.keys())
print (b.iterkeys())

#pop  用来获取对应于给定的键的值，然后将这个键值对从字典中移除
print (b)
#返回Alice对应的值，并在字典中删除Alice键值对
c = b.pop('Alice')
print (c)
print (b)

#popitem 方法 类似于 list pop 后者会弹出列表中最后一个元素，popitem弹出随机的项，因为字典中并没有最后的元素或者其他有缘顺序的概念。
#若要一个一个移除并处理，这个方法非常有效
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print ('=' * 60)
c = b.popitem()  #popitem返回的是元组
print (c)
print (b)

#setdefault 方法 在某种程度上类似get方法，能够获得与给定键相关联的值，在字典中不含有该键的情况下添加相应键值。
d = {}
d.setdefault('IC') #自动添加key是IC的键值对，默认value是None
print (d)
d = {}
d.setdefault('IP','192.168.1.1') #自动添加key是IP的键值对，默认value是192.168.1.1
print (d)

#update 方法 可以利用一个字典更新另外一个字典
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
c = {'Ice':'5566','Beth':'0000'}
# 将C字典中没有的键值对添加到b字典中，将c与b字典都有的键，value值从C更新到b
b.update(c)
print (c)
print (b)

#values 以列表的形式返回字典中的值，  itervalues返回值的迭代器
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print (b.keys())
print (b.iterkeys())

