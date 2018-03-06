#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#下文子类化一个内建list类示例，实现获取用户访问列表次数计数
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

cl = CounterList(range(10))
print cl
cl.reverse()
print cl,cl.counter
del cl[3:6]
print cl,cl.counter

for i in range(7):
    print cl[i],cl.counter


