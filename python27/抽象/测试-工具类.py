#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class gongjulei1:
    def gongju1(self):
        print 'gongju1'

    def gongju2(self):
        print 'gongju2'
class gongjulei2:
    def gongju3(self):
        print 'gongju3'
    def gongju4(self):
        print 'gongju4'

class gongjulei(gongjulei1,gongjulei2):
    pass

c = gongjulei()
c.gongju1()
c.gongju2()
c.gongju3()
c.gongju4()