#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = '***'
receiver = '***'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

#构造附件
att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
