# -*- coding: UTF-8 -*-
import logging
import ConfigParser
import myconfig

p = myconfig.Locationfile()
Path = p.findPath('config.conf')





class Outlog(myconfig.GetConfig):
    def __init__(self):
        '''
        初始化系统日志配置
        '''
        super(Outlog, self).__init__()
        self.logger = logging.getLogger('systemlog')
        if self.log_level == 'INFO':
            self.logger.setLevel(logging.INFO)
        elif self.log_level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        self.ch = logging.StreamHandler()
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formater)
        self.logger.addHandler(self.ch)

    def loginfo(self, data):
        self.logger.info(data)

    def logdebug(self, data):
        self.logger.debug(data)

    def logerror(self, data):
        self.logger.error(data)


if __name__ == '__main__':
    l = Outlog()
    l.loginfo('aaaaa')
    l.logdebug('BBBBB')
    l.logerror('eeeee')
