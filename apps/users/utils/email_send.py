# -*- coding: utf-8 -*-

from random import Random
from users.models import EmailVerfyRecord
from django.core.mail import send_mail
from Mxoline_app.settings import EAMIL_FROM


def sed_register_email(email, send_type="register"):
    email_record = EmailVerfyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "幕雪忘注册激活链接"
        email_body = "点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EAMIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "幕雪网密码重置链接"
        email_body = "点击下面的链接重置你的密码:http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EAMIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
