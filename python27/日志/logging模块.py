#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
# LOG = logging.getLogger('应用程序名')
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# LOG.addHandler(console)
# LOG.debug('调试信息')
# LOG.info('有用的信息')
# LOG.warning('警告信息')
# LOG.error('错误信息')
# LOG.critical('严重错误信息')

#创建一个logger
logger = logging.getLogger('MyTestLogger')
logger.setLevel(logging.DEBUG)

#创建一个handler，用于写入日志
# fn = logging.FileHandler('E:\按机构统计\按机构统计'.decode('utf8').encode('gb2312')+'test.log')
# fn.setLevel(logging.DEBUG)

#在创建一个handler，用于控制台输出
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#定义handler的输出格式
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fn.setFormatter(formater)
ch.setFormatter(formater)

#给logger添加handler
logger.addHandler(ch)
# logger.addHandler(fn)

logger.debug('调试信息')
logger.info('有用的信息')
logger.warning('警告信息')
logger.error('错误信息')
logger.critical('严重错误信息')



