#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def story(**kwargs):
    return 'Once upon a time.there was a %(job)s called %(name)s.' % kwargs
def power(x,y,*args):
    if  args:
        print 'Received redundant parameters:',args
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i < stop:
        result.append(i)
        i+=step
    return result
print story(job='King',name='Gumby')
print story(name='Sir Robin',job='brave knight')
params={'job':'language','name':'Python'}
print story(**params)
del params['job']
print params
print story(job='stroke of genius',**params)
print power(2,3)
print power(y=3,x=2)
params=(5,)*2
print params
print power(*params)
print interval(10)
print interval(1,5)
print interval(1,10,2)