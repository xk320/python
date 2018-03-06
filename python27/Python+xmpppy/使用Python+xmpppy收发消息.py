#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import xmpp
import  time
#注意账号信息，必须加@域名格式
from_user='lw'
password='lw'

#可添加多个接收人
to_user=['lh@msg']
msg='测试消息1111'
def to_msg():
    """
    基于xmpp协议的即时通讯消息发送，需求安装xmpp库
    使用openfire搭建的即时通讯都可以使用
    google talk也可以使用
    """
    client=xmpp.Client('192.168.1.100',5222)
    client.connect(server=('192.168.1.100',5222))
    client.auth(from_user,password,'botty',sasl=0)
    client.sendPresence('lw','available')
    client.sendInitPresence()
    for i in to_user:
        client.sendInitPresence()
        message=xmpp.Message(i,msg,typ='chat')
        client.send(message)
        time.sleep(10000)
if __name__=='__main__':
    to_msg()



