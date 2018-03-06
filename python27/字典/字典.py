#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#空字典🈶️两个大括号组成
a = {}
b = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print (b.get('Alice'))
print (b['Beth'])
b['Jack']='7890'
print (b)

#dict函数
#通过其他映射或者键值对的序列建立字典
c = [('host', '192.168.1.1'), ('ip', '192.168.1.200'), ('port', '3316')]
d = dict(c)
print (d)
#通过dict函数来创建字典
e = dict([('host', '192.168.1.1'), ('ip', '192.168.1.200'), ('port', '3316')])
print (e)

#len(d)返回字典d的键值对数量
print (len(d))
#del  删除字典上的键值对
print (b)
del b['Alice']
print (b)
#'Alice' in b 检查字典中是否含有键为'Alice'的项
print ('Alice' in b)
