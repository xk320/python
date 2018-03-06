# -*- coding: UTF-8 -*-
# SMTP是发送邮件的协议，python内置对smtp的支持，可以发纯文本邮件、html邮件以及带附件的邮件
# python对smtp支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
import smtplib
from email.mime.text import MIMEText

# 构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入plain，最后一定要用utf-8编码保证多语言兼容
msg = MIMEText('hello,this is testing email....', 'plain', 'utf-8')
# 然后通过smtp发送出去。
# 输入email口令：
from_addr = raw_input('From: ')
password = raw_input('Password: ')
smtp_server = 'smtp.163.com'
to_addr = raw_input('To: ')

# server=smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
server=smtplib.SMTP()
server.connect(smtp_server,25)
#利用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息，SMTP协议就是简单的文本命令和响应，login()方法用来登录服务器，sendmai()
#方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()和MIMEText对象变成str
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
#问题
#1、邮件没有主题
#2、收件人的名字没有显示不友好
#3命名收到了邮件，去体会不再收件人中
#这是因为邮件主题，如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，我们必须把FRO、To、Subject添加到
#MIMEText中才是一封完整的邮件

