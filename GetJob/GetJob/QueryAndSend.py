#encoding:utf-8
import pymysql
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class QueryAndSend(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',db='Hunan_University',charset='utf8')
        self.cursor = self.conn.cursor()
        sql3 = "alter table HNU modify meet_time date not null comment '宣讲会时间'"
        self.cursor.execute(sql3)


    def Query(self):
        sql = 'select * from HNU'
        self.cursor.execute(sql)
        a = self.cursor.fetchall()
        li_heads=['学校','招聘会地址','公司所在城市','公司名称','公司类型','公司所在行业','宣讲会时间','公司所招专业','被浏览量','岗位','岗位所招专业','薪水','招聘人数','学历','工作城市','详情页链接','关键字出现次数(max=4)','公司福利']
        t = datetime.date.today() + datetime.timedelta(days=3)
        message = ''
        for i in a:
            if i[7] < t:
                msg = ''
                for j in range(1,len(i)):
                    msg += li_heads[j-1] + ' : '
                    msg += str(i[j]) + '<br>'
                message += msg +'<br><br>'

        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return message

    def Send(self,body):
        # print(body)
        host = 'smtp.163.com'
        # 设置发件服务器地址
        port = 465
        # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
        sender = 'zhangkaixiang0425@163.com'
        # 设置发件邮箱，一定要自己注册的邮箱
        pwd = 'zhang1234'
        # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
        receiver = 'zhangkaixiang0425@163.com'
        # 设置邮件接收人，可以是QQ邮箱
        # 设置邮件正文，这里是支持HTML的
        msg = MIMEText(body, 'html')
        # 设置正文为符合邮件格式的HTML内容
        msg['subject'] = 'sadacsqwmc'
        # 设置邮件标题
        msg['from'] = sender
        # 设置发送人
        msg['to'] = receiver
        # 设置接收人
        try:
            s = smtplib.SMTP_SSL(host, port)
            # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(sender, pwd)
            # 登陆邮箱
            s.sendmail(sender, receiver, msg.as_string())
            # 发送邮件！
            print('Done.sent email success')
        except smtplib.SMTPException as e:
            print('Error.sent email fail:' + str(e))

    def run(self):
        body = self.Query()

        self.Send(body)

if __name__ == '__main__':
    QueryAndSend = QueryAndSend()
    QueryAndSend.run()