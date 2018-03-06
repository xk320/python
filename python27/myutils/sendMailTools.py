# -*- coding: UTF-8 -*-
import locationFile
import systemLogger
from email import encoders
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import ConfigParser
import traceback


class SetSendMail(object):
    def __init__(self):
        p = locationFile.Locationfile()
        PATH = p.findPath('config.conf')
        config = ConfigParser.ConfigParser()
        config.readfp(open(PATH, 'rwb'))
        self.from_addr = config.get('mail', 'from_addr')
        self.mail_pass = config.get('mail', 'mail_pass')
        self.smtp_server = config.get('mail', 'smtp_server')
        self.message = ''
        self.to_addr = ''
        self.from_name = ''
        self.to_name = ''
        self.subject = ''
        self.file_name=''
        self.file_type=''


class MySendTextMail(SetSendMail):
    def __init__(self):
        super(MySendTextMail, self).__init__()

    def _format_addr(self, s):
        '''
        格式化邮件地址函数
        :param s: name <addr@example.com>
        :return:
        '''
        name, addr = parseaddr(s)
        return formataddr((
            Header(name, 'utf-8').encode(),
            addr.encode('utf-8') if isinstance(addr, unicode) else addr
        ))

    def mysendmail(self,send_file=False,test_type='plain'):
        # 配置邮件正文
        if  send_file :
            self.msg=MIMEMultipart()
            with open('','rb') as f:
                mime=MIMEBase('image','png',filename=self.file_name)
                mime.add_header('Content-Disposition', 'attachment', filename='test.png')
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                self.msg.attach(mime)
        else:
            self.msg = MIMEText(self.message, test_type, 'utf-8')
        # 配置邮件发送这及显示名称
        self.msg['From'] = self._format_addr(u'%s <%s>' % (self.from_name, self.from_addr))
        # 配置邮件接受这及显示名称
        # msg['To']接受的是字符串而不是list，如果有多个邮件地址，用，分隔即可
        self.msg['To'] = self._format_addr(u'%s <%s>' % (self.to_name, self.to_addr))
        # 配置邮件主题
        self.msg['Subject'] = Header(u'%s' % self.subject, 'utf-8').encode()

        # 发送电子邮件
        self.server = smtplib.SMTP()
        self.server.connect(self.smtp_server, 25)
        self.server.login(self.from_addr, self.mail_pass)
        self.server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        self.server.quit()


if __name__ == '__main__':
    s = MySendTextMail()
    s.to_addr = u'xk320@163.com'
    s.message = u'测试邮件，学习python'
    s.from_name = u'陆炜眀'
    s.to_name = u'测试用户2'
    s.subject = u'通知信息'

    s.mysendmail()
