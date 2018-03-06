# -*- coding: UTF-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle

#pickle.load()方法直接从file-like object中反序列化对象
with open('tt','r') as f :
    d = pickle.load(f)
print d

#pickle.loads()方法从str反序列化对象
with open('tt','r') as f:
    a=f.read()
d=pickle.loads(a)
print '-'*80
print pickle.load(f)