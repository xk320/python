#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 使用dict时，如果引用的key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
import collections

dd = collections.defaultdict(lambda: 'N/A')
ddd = {}
print dd['key']
try:
    print ddd['key']
except Exception, e:
    print e

    # 默认值是调用函数返回的，二函数在创建defaultdict对象时传入。
    # 除了key不存在时返回默认值，defaultdict与dict功能完全一样。
