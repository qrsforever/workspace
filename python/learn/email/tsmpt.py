#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tsmpt.py
# @brief
# @author QRS
# @home qrsforever.github.io
# @version 1.0
# @date 2019-05-09 16:30:31

import os

import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'
mail_user = os.environ.get('U1')
mail_pass = os.environ.get('E1')

sender = '985612771@qq.com'
receivers = ['705723886@qq.com']

# qq not support
md = """
## Hello1
### H1
## Hello2
### H2.1
### H2.2
Hello world!
"""

html = """
<table align='center'>
<tr><td>R1C1</td><td>R1C2</td></tr>
<tr><td>R2C1</td><td>R2C2</td></tr>
<tr><td>R3C1</td><td>R3C2</td></tr>
</table>
"""

txt = html
subtype = 'html' # plain,  html, x-markdown

message = MIMEText(txt, subtype, 'utf-8')
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'Python SMTP Test'

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print('ok')
except smtplib.SMTPException as e:
    print(e)
