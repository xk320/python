# -*- coding: UTF-8 -*-
# 如果我们要在不同的程序语言之间传递对象，就必须把对象序列化为标准格式，比如XM，但更好但方法是序列化为JSO，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输，JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取非常方便
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和python内置的数据类型对应对下
#  JSON类型          python类型
#   {}               dict
#   []               list
#   string           str或u'unicode'
#   123.56           int或float
#   true/false       True/False
#   null             None
# python内置的json模块提供来非常完善的python对象到JSON格式的转换，将python对象转换成JSON如下：
import json

d = dict(name='Bob', age=20, score=99)
a = json.dumps(d)
print a, type(a)
# dumps()方法返回一个str，内容就是标准的JSO，类似的dump()方法直接把JSON写入一个file-like object
# 要包JSON反序列化为python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like object中读取字符串并反序列化
json_str = '{"age": 20, "score": 99, "name": "Bob"}'
print type(json_str)
b = json.loads(json_str)
print a, type(b)
