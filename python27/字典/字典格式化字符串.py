#!/usr/bin/env python
# _*_ coding:utf-8 _*_
phonebook = {'Beth':'9102','Alice':'2341','Cecil':'3258'}
print ("Cecil 's phone number is %(Cecil)s." % phonebook)

template = '''<html>
    <head><title>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>
'''
data = {'title':'My Home Page','text':'Welcome to my home page!'}
print (template % data)