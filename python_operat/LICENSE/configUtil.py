# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import platform, os,configparser


class Locationfile(object):
    def __init__(self):
        if 'Windows' in platform.system():
            self.separator = '\\'
        else:
            self.separator = '/'
        self.o_path = os.getcwd()

    def findPath(self, file):
        str = self.o_path
        str = str.split(self.separator)
        while len(str) > 0:
            spath = self.separator.join(str) + self.separator + file
            leng = len(str)
            if os.path.exists(spath):
                return spath
            str.remove(str[leng - 1])

class GetConfig(object):
    def __init__(self):
        p = Locationfile()
        Path = p.findPath('config.yml')
        config = configparser.ConfigParser()
        config.read_file(Path)
        self.log_level = config.get('log', 'loglevel')
        self.ftp_server=config.get('ftp','server')
        self.ftp_username=config.get('ftp','username')
        self.ftp_password=config.get('ftp','password')
        self.ftp_port = config.get('ftp', 'port')

if __name__ == '__main__':
    # a=GetConfig()
    pass