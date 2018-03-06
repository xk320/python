#!/usr/bin/env python
# _*_ coding:utf-8 _*_
name = ''

#while循环
# while not name:
#     name=raw_input('Enter input your name: ')
# print 'Hello my friend %s' % name

#for循环
words = ['this','is','an','ex','parrot']
for i in words:
    print  i
print range(10)
print range(1,10)

#循环遍历字典元素
d = {'a':1,'b':2,'c':3,'d':4}
for key in d :
    print key,'corresponds to ',d[key]
for key,value in d.items():
    print key,'corresponds to ',value
