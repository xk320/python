#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)


logger.addHandler(console)
consoleFormatte=logging.Formatter('%(asctime)s  %(levelname)s - %(name)s - %(message)s')
console.setFormatter(consoleFormatte)

logger.debug('调试信息')
logger.info('有用的信息')
logger.warning('警告信息')
logger.error('错误信息')
logger.critical('严重错误信息')
