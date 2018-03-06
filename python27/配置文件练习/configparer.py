#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import ConfigParser
import sys

# #创建一个configparser实例
# config = ConfigParser.ConfigParser()
#
# #返回配置文件中节顺序
# config.sections()
#
# #返回某个项目中的所有键的序列
# config.get(section,option)
#
# #添加一个配置文件节点
# config.add_section(str)
#
# #读取配置文件
# config.read(filenames)
#
# #写入配置文件
# config.write(obj_file)

#  综合实例
#config.readfp(open("config.conf","rb"))
#print config.get('global','gateway')
#print config.get('db','gateway')

def writeConfig(filename):
    config = ConfigParser.ConfigParser()
    # set DB
    section_name='DB'
    config.add_section(section_name)
    config.set(section_name,'dbname','MySQL')
    config.set(section_name,'host','127.0.0.1')
    config.set(section_name,'port','3306')
    config.set(section_name,'password','123456')
    config.set(section_name,'datebasename','test')

    #set app
    section_name='app'
    config.add_section(section_name)
    config.set(section_name,'loggerapp','192.168.20.2')
    config.set(section_name,'reportapp','192.168.30.3')

    #write to fire
    config.write(open(filename,'a'))

def updateConfig(filename,section,**keyv):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    print '-'*20,config.sections(),'-'*20
    for section in config.sections():
        print "[",section,"]"
        items = config.items(section)
        for item in items:
            print "\t",item[0],"=",item[1]
    print config.has_option('DB','dbname')
    print config.set('DB','dbname','11')
    print "\t",'dbname',config.get('DB','dbname')
    print '..................'
    for key in keyv:
        print "\t",key,"=",keyv[key]
        config.set(section,key,keyv[key])
        print config.get(section,key,keyv[key]),'----------------'
    config.write(open(filename,'r+'))

if __name__ == '__main__':
    file_name = '配置文件练习/test.ini'
    # writeConfig(file_name)
    updateConfig(file_name,'app',reportapp='192.168.1.100')
