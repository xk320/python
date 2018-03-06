#!/usr/bin/env python
# _*_ coding:utf-8 _*_
name = 'Hello world!'
if name.endswith('rld!'):
    print 'test p111'

#else子句  else子句可以增加一种选择，他不是独立的语句，只能做if语句的一部分
if name.endswith('ld'):
    print '条件真'
else:
    print '条件假'
#elif子句， 需要检查多个条件的时候，可以使用elif他是else if的简写，
num = input('Enter a number: ')
if num == 0:
    print num
elif num >1 :
    print '>1'
else:
    print 11111