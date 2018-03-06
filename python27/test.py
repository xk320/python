#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import ConfigParser
import sys


config = ConfigParser.ConfigParser()
config.readfp(open('config.conf','rwb'))
config.set('DEFAULT','port','3333')
config.write(sys.stdout)
print  config.get('DEFAULT','port')
print config.get('log','loglevel')
