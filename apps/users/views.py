# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .models import UserProfile, EmailVerfyRecord
from forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.email_send import sed_register_email


# Create your views here.验证不同的方式登录：用户名、邮箱、手机等等


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(moblie=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录业务逻辑

class loginView(View):
    def get(self, request):
        return render(request, "login.html", {})  # ß

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


# 注册页面

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户名已存在"})
            pass_word = request.POST.get("password", "")
            uesr_profile = UserProfile()
            uesr_profile.username = user_name
            uesr_profile.email = user_name
            uesr_profile.password = make_password(pass_word)
            uesr_profile.save()
            sed_register_email(user_name, "register")
            # else:
            #     return render(request, "register.html", {"msg": "用户名已存在"})
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class AcitveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerfyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                sed_register_email(user_name, "forget")
                return render(request, "forgetpwd.html", {"forget_form": forget_form, "msg": "重置密码已发送至邮箱"})
            else:
                return render(request, "forgetpwd.html", {"forget_form": forget_form, "msg": "用户名不存在"})

        return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerfyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class Logoutview(View):
    def get(self, request):
        logout(request)
        return render(request, "index.html")
