#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Dict(dict):
    def __init__(self,**kwargs):
        super(Dict, self).__init__(**kwargs)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" %  item)
    def __setattr__(self, key, value):
        self[key]=value

Dict()