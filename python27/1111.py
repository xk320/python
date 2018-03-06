#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging

# define the log file , file mode and logging level
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='python.log', filemode='w',
                    level=logging.DEBUG)
logging.debug('This is a debug message!')
logging.info('This is a info message!')
logging.warning('This is a warning message!')
logging.warn
c = open('python.log', 'r')
for line in c.readlines():
    print line
c.closed
a = 1
b = 2
