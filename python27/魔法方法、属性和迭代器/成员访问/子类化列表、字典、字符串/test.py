#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Ctext(object):
    def run(self):
        print 1111


class Ctext1(object):
    def run1(self):
        print 222


class Ttext(Ctext,Ctext1):
    pass

a=Ttext()
a.run1()

