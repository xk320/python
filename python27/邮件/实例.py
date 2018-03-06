#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header



mail_host='smtp.sina.net'
mail_user='luweiming@zucp.com.cn'
mail_pass='jiguang123'


sender='luweiming@zucp.com.cn'
receivers=['luweiming@zucp.com.cn']  #接收邮箱，可以设置为你的QQ邮箱或者其他邮箱

#三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
message=MIMEText('python测试邮件.....','plain','utf-8')
message['from']=Header('测试教程','utf-8')
message['to']=Header('测试','utf-8')

subject='python测试邮件'
message['subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)  #  25是smtp端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print '邮件发送成功'
except EOFError as e:
    print e
    print 'Error  :邮件发送失败'
