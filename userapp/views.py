# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as django_login, logout as django_logout, authenticate as django_auth
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

# 错误码
ERROR_LOGIN_OK = 100
ERROR_LOGIN_WRONG_PARAMS = 101
ERROR_LOGIN_WRONG_USERNAME_PASSWORD = 102
ERROR_LOGIN_ONLY_POST = 103
ERROR_LOGOUT_OK = 200


def index(request):
    return render_to_response('userapp/index.html')


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = request.POST.get('username', json_data.get('username'))
        password = request.POST.get('password', json_data.get('password'))
        print username, password
        res = None
        if username is None or password is None:
            res = JsonResponse({
                'code': ERROR_LOGIN_WRONG_PARAMS,
                })
            return res
        # 验证用户名/密码合法性
        user = django_auth(username=username, password=password)
        if user is None:
            # 用户名/密码非法
            res = JsonResponse({
                'code': ERROR_LOGIN_WRONG_USERNAME_PASSWORD
                })
            return res
        else:
            django_login(request, user)
            res = JsonResponse({
                'code': ERROR_LOGIN_OK
                })
            return res
    else:
        res = JsonResponse({
            'code': ERROR_LOGIN_ONLY_POST})
        return res

# 注销
def logout(request):
    django_logout(request)
    return JsonResponse({
        'code': ERROR_LOGOUT_OK
        })

# 获取用户信息
def get_user_info(request):
    user = request.user
    if user.is_authenticated():
        return JsonResponse({
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'lastlogin': datetime.datetime.strftime(user.last_login, '%Y/%m/%d %H:%M'),
            'datejoined': datetime.datetime.strftime(user.date_joined, '%Y/%m/%d %H:%M'),
            })
    else:
        return JsonResponse({

            })

def github_file_explorer(request):
    return render_to_response('userapp/github_file_explorer.html')