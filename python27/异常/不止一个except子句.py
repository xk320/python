#!/usr/bin/env python
# _*_ coding:utf-8 _*_
try:
    x = input('Enter the first number:  ')
    y = input('Enter the second number: ')
    print x/y
except ZeroDivisionError:
    print 'The second number can`t be zero!'
except TypeError:
    print "That wasn't a number was it ?"
