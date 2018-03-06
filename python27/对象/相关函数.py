#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# callable   确定对象是否可调用  Python2.0
class Test111:
    def test_haha(self):
        print 11111;
a=Test111()
print callable(getattr(a,'test_haha'))