# -*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


# 格式化邮件地址函数，注意不能简单传入name <addr@example.com>,因为如果包含中文，需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr
    ))


from_addr = raw_input('From : ')
password = raw_input('Password : ')
to_addr = raw_input('To : ')
smtp_server = 'smtp.163.com'

# 发送文本邮件
# 配置邮件正文
msg = MIMEText('Hello ,send by python ...', 'plain', 'utf-8')
# 配置邮件发送这及显示名称
msg['From'] = _format_addr(u'python发送者 <%s>' % from_addr)
# 配置邮件接受这及显示名称
# msg['To']接受的是字符串而不是list，如果有多个邮件地址，用，分隔即可
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# 配置邮件主题
msg['Subject'] = Header(u'来自SMTP的问候。。', 'utf-8').encode()

#发送HTML邮件
# 配置邮件正文
msg_html = MIMEText('<html><body><h1>PYTHON</h1><p>send by <a href="www.baidu.com">baidu</a></p></body></html>', 'html', 'utf-8')
# 配置邮件发送这及显示名称
msg_html['From'] = _format_addr(u'python发送者 <%s>' % from_addr)
# 配置邮件接受这及显示名称
# msg['To']接受的是字符串而不是list，如果有多个邮件地址，用，分隔即可
msg_html['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# 配置邮件主题
msg_html['Subject'] = Header(u'来自SMTP的问候。。', 'utf-8').encode()

server = smtplib.SMTP()
server.connect(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.sendmail(from_addr, [to_addr], msg_html.as_string())
server.quit()
