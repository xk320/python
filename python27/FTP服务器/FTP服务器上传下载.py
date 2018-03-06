#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ftplib import FTP
import myutil.myconfig


class FTPclass(myutil.myconfig.GetConfig):
    def __init__(self):
        super(FTPclass, self).__init__()
        self.ftp=FTP()
        # 打开调试级别2，显示详细信息
        self.ftp.set_debuglevel(2)
        self.ftp.connect(self.ftp_server,21)
        self.ftp.login(self.ftp_username,self.ftp_password)

    def filelist(self):
        self.ftp_list=self.ftp.dir('/mms')
        print self.ftp_list

if __name__ == '__main__':
    a=FTPclass()
    a.filelist()
