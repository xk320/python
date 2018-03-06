#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#将其他类名写到class语句后的圆括号就可以指定超类
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked=['SPAM']

print(issubclass(SPAMFilter,Filter))
s = SPAMFilter
print(issubclass(s,SPAMFilter))
print(issubclass(s,Filter))
print(s.__bases__)
print('--------------fengexian------------------')
#---------------getattr----------------
#---------------setattr-----------------
setattr(s,'names','hahaha')
print(getattr(s,'names'))