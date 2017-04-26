'''
使用IMAPClient库
'''
from __future__ import unicode_literals
from imapclient import IMAPClient
import email
HOST = 'c1.icoremail.net'
USERNAME = 'qihongtao@rinpo.com'
PASSWORD = 'qht131427'
ssl = False

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

server.select_folder('INBOX', readonly = True)#必须先查文件夹
messages = server.search('UNSEEN')
print("%d 新邮件" % len(messages))
# print(messages)
for i in messages:
    msgdict = server.fetch(i, ['BODY.PEEK[]'])
    for message_id,message in msgdict.items():
        # print(message_id)
        # print(message[b'BODY[]'])
        body=email.message_from_bytes(message[b'BODY[]'])#得到邮件内容  注意这里是获取字节
        # print(type(body))
        # print(body)
        # print(body['Subject'])
        # print(body['SUBJECT'])
        #  >>>>>下面进行解码<<<<<<
        subject = email.header.make_header(email.header.decode_header(body['SUBJECT']))#主题
        mail_from = email.header.make_header(email.header.decode_header(body['From']))
        rev = email.header.make_header(email.header.decode_header(body['Date']))
        print("接收到邮件：{}".format(subject))
        print("来自于：{}".format(mail_from))
        print("时间：{}".format(rev))



