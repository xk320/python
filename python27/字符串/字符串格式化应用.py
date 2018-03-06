#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 格式化字符串%s部分为转换说明符（conversion specifier)，它们标记了需要插入转换值的位置
# %s  字符串   #f 浮点数   #d  数值
# 如果格式化字符串中包含百分号，那么必须使用%%。这样就python就不会将百分号误认为是转换说明符
string_format = "Hello %s %s enough for ya %%100 ?"
string_values = ('World','Hot')
print (string_format % string_values)

#格式化实数
#格式化浮点数，并保留3位小数
import math
a = "Pi with three decimals: %.3f"
print (a % math.pi)

#模板字符串
#尽量使用safe_substitute方法,不会因缺少值或者不正确使用$符号而出错。
import string
s = string.Template('$x glorious $x !')
s.substitute(x='haha')
print (s.substitute(x='haha'))
print (s.safe_substitute(x=123))

b = {'var':'foo'}
try:
    t = string.Template('''''$$ $var is here but $ missing is not provided! ''')
    print (t.safe_substitute(b))
    print (t.substitute(b))
except ValueError as err:
    print 'Error: ',str(err)
#可使用$$插入美元符号
print (t.safe_substitute(b))
#除了关键字参数之外，还可以使用字典变量提供值/名称对
c = string.Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show is socks'
print (c.safe_substitute(d))

#简单转换只需要写出转换类型
a = 'Price of eggs : $%d'
print a % 42
a = 'Price of eggs : $%x'
print a % 42
a = 'Price of eggs : %f'
print a % math.pi
a = 'Price of eggs : %i'
print a % math.pi
a = 'Using str: %s'
print a % 42L
a = 'Using repr: %r'
print a % 42L

#字段宽度和精度
a = '%10f'  #字符宽10
print (a % math.pi)
a = '%10.2f'  #宽度10，精度2
print (a % math.pi)
a = '%.2f'  #精度2
print (a % math.pi)
a = '%.5s'
print (a % 'Guido van Rossum')
#使用*（星号）作为字段宽度或者精度，此时数值会从元组参数中读出
a = '%.*s'
print (a % (9,'Guido van Rossum'))

#符号、对齐和用0填充
a = '%010.2f'  #宽度10 ，不够用0进行填充
print (a % math.pi)
a = '%-10.2f'  #减号左对齐，默认右对齐
print (a % math.pi)
a = '%+d'
print (a % 10)
print (a % -10)


width = input('Please enter width: ')
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
nformat = '%-*s%*.2f'
print ('=' * width)
print (header_format % (item_width,'Item',price_width,'Price'))
print ('-' * width)
print (nformat % (item_width,'Apples',price_width,0.4))
print (nformat % (item_width,'Pears',price_width,0.5))
print (nformat % (item_width,'Cantaloupes',price_width,0.1923))