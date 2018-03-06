#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import chilkat


mailman = chilkat.CkMailMan()
success = mailman.UnlockComponent('MAILT34MB34N_6ADE5E140UIY')
if success != True:
    print mailman.lastErrorText()
    sys.exit()

# set proxy server
mailman.put_HttpProxyHostname('proxy.piccnet.com.cn')
mailman.put_HttpProxyPort(3128)
# mailman.put_HttpProxyUsername('')
# mailman.put_HttpProxyPassword('')

# set mail server
mailman.put_SmtpHost('smtp.sina.net')
mailman.put_SmtpUsername('luweiming@zucp.com.cn')
mailman.put_SmtpPassword('jiguang123')

# set mail
email = chilkat.CkEmail()
email.put_Subject('邮件标题'.decode('utf8').encode('gb2312'))
email.put_Body('邮件内容'.decode('utf8').encode('gb2312'))
email.put_From('luweiming@zucp.com.cn')
success = email.AddTo('test'.decode('utf8').encode('gb2312'), 'luweiming@zucp.com.cn')

# add some attackments
contenetType=email.addFileAttachment('E:\按机构统计\按机构统计2017-11-28.csv'.decode('utf8').encode('gb2312'))
if email.get_LastMethodSuccess() != True:
    print email.lastErrorText()
    sys.exit()


success = mailman.SendEmail(email)
if success != True:
    print mailman.lastErrorText()
    sys.exit()
success = mailman.CloseSmtpConnection()
if success != True:
    print ('Connection to SMTP server not closed cleanly.')
print 'Mail Sent!'
