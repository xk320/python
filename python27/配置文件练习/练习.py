# -*- coding: UTF-8 -*-
import ConfigParser
class config():
    #重新封装一个配置文件使用方法
    def writeConfig(self,filename,d):
        conf = ConfigParser.ConfigParser()
        print d.keys()
        for key in d.keys():
            conf.add_section(key)
            print d[key].keys()
            for k,i in d[key].items():
                conf.set(key,k,i)
        conf.write(open(filename,'r+'))

c = config()
d = {'MYSQL':{'IP':'192.168.1.200','PORT':'3306'},'ORCLE':{'IP':'192.168.1.120','PORT':'1521'}}
c.writeConfig('config.conf',d)

