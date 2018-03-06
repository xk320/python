#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#find 在字符串中查找指定字符，返回指定字符的起始位置。没有查到返回-1,可以指定查询范围。
subject =  '$$$ Get rich now !!! $$$'
print (subject.find('rich'))
print (subject.find('rich',3,8))  #从第三个字符开始查找，到第八个字符结束
#join，它是split方法的逆方法，用来连接序列中的元素
seq = ['1','2','3','4','5','6']
sep = '+'
print ( sep.join(seq))  #join 连接必须是字符串
dirs = '','usr','bin','env'
print ('/'.join(dirs))
print ('%s%s' %  ('c:','\\'.join(dirs)))

#lower 返回字符串的小写字母
print ('Test Python Study!'.lower())

#upper 返回字符串的大写字母
print ('Test Python Study!'.upper())

#replace返回某字符串的所有匹配项均被替换之后得到字符串
print ('Hello is World is Test!'.replace('World','hahah'))
print ('Hello is World is Test is !'.replace('is','hahah'))

#split 用来将字符串分割成序列
seq = '1,2,3,4,5,6,7'
print (seq.split(','))

#strip返回去除两侧（不包括内部）空格的字符串
a = '   Hello World !   '
print (a.strip())
#strip去除指定字符，只会去除两侧的字符
a = '*** SPAM * FOR EVERYONE!!! ***'
print (a.strip(' *!'))

#translate与replace一样，可以替换字符串中的某些部分；