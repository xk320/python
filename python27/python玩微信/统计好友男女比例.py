#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import itchat

itchat.login()

#获取好友列表
friends=itchat.get_friends(update=True)[0:]

#初始化计数器，有男有女
male=female=other=0

#遍历里诶包，列表第一位是自己，所以从自己之后计算
#1表示男性，2女性
for i in friends[1:]:
    sex=i['Sex']
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1

total=len(friends[1:])

print u'男性好友：%d' % male
print u'女性好友：%d' % female
print u'其他：%d' % other
