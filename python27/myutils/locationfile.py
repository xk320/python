# -*- coding: UTF-8 -*-
import platform, os


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
