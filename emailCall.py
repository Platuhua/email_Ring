import imaplib
import email  #导入两个库
def accept_imap():
    conn = imaplib.IMAP4_SSL(port = '993',host = 'c1.icoremail.net')
    #QQ企业邮箱：imap.exmail.qq.com

    print('已连接服务器')
    conn.login('qihongtao@rinpo.com','qht131427')
    print('已登陆')

    #循环
    # while 1:
    conn.select()
    type, data = conn.search(None, 'UNSEEN') #未读邮件  #进行邮件查询
    print("type:   ",type)
    print("data:   ",data)
    list_message=data[0].decode().split()
    print("未读邮件列表: ",list_message)
    if len(list_message) >0:
        print("有未读邮件，{}封".format(len(list_message)))
        print("报警")
        #todo 报警  放入queue队列
    # for num in data[0].split():
    #     print("第{}封".format(num))
    #     typ, msg_data = conn.fetch(num, '(RFC822)')
    #     print(len(msg_data))
    #     for response_part in msg_data:
    #         # print("详情：{}".format(response_part))
    #         msg = email.message_from_string(response_part[1].decode(""))
    #         print("解析的数据：{}".format(msg["subject"]))

            # print(msg_data[0][1])# msgdata[0][1]是正文
        # print(msg_data[0][1].decode(""))
        # msg = email.message_from_string(msg_data[0][1].decode("ascii"))
        # print('Message %s,%s' % (num, msg))
    # type, data = conn.fetch(data[0][1], '(RFC822)')

    # msg = email.message_from_string(data[0][1].decode())
    conn.close()
    conn.logout()
if __name__=='__main__':
    accept_imap()

# import poplib
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
#
# # email = input('Email:')
# email = "qihongtao@victorysoft.com.cn"
# # password = input('Password: ')
# password = "Qht131427"
# # pop3_server = input('POP3 server: ')
# pop3_server = 'pop.exmail.qq.com'
#
# # 这是检测编码部分，有点不懂
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
#
# # 这里只取出第一发件人
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
#
# # 递归打印信息
# def print_info(msg, indent=0):
#     if indent == 0:
#         for header in ['From', 'To', 'Subject']:
#             value = msg.get(header, '')
#             if value:
#                 if header == 'Subject':
#                     value = decode_str(value)
#                 else:
#                     hdr, addr = parseaddr(value)
#                     name = decode_str(hdr)
#                     value = u'%s <%s>' % (name, addr)
#             print('%s%s: %s' % ('  ' * indent, header, value))
#     if (msg.is_multipart()):
#         parts = msg.get_payload()
#         for n, part in enumerate(parts):
#             print('%spart %s' % ('  ' * indent, n))
#             print('%s--------------------' % ('   ' * indent))
#             print_info(part, indent + 1)
#     else:
#         content_type = msg.get_content_type()
#         if content_type == 'text/plain' or content_type == 'text/html':
#             content = msg.get_payload(decode=True)
#             charset = guess_charset(msg)
#             if charset:
#                 content = content.decode(charset)
#             print('%sText: %s' % ('  ' * indent, content + '...'))
#         else:
#             print('%sAttachment: %s' % ('  ' * indent, content_type))
#
# # 下载原始邮件
# server = poplib.POP3(pop3_server)
# server.set_debuglevel(0)
# print(server.getwelcome().decode('utf-8'))
# server.user(email)
# server.pass_(password)
# # 打印邮件数量和占用空间
# print('Message: %s, Size: %s' % server.stat())
# resp, mails, octets = server.list()
# print(mails)
#
# # 解析邮件
# index = len(mails)
# resp, lines, octets = server.retr(index)
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# msg = Parser().parsestr(msg_content)
# print_info(msg)
#
# server.quit()