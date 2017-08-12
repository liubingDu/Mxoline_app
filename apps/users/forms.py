# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField


# 登录页面表单验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


# form表单验证

# 注册页面表单验证
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # captcha = CaptchaField()#error_messages={"invalid": u"验证码错误"}
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码表单验证
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=8)
    password2 = forms.CharField(required=True, min_length=8)