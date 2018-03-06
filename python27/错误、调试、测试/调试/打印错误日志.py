#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 把print替换为logging是第三种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging

s = '0'
n = int(s)
logging.basicConfig(level=logging.INFO)
logging.info('n = %d' % n)
print 10 / n
# logging.info()可以输出一段文本，运行发现除了ZeroDivisionError没有任何信息，需要制定日志输出级别
# 这就是logging的好处，他允许你指定记录信息的级别，有debug、info、warning、error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信
# 息，也不用删除，最后统一控制输出哪个级别的信息。logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，
# 比如console和文件。
