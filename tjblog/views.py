from django.shortcuts import render
import sys
import os
import logging
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from tjblog.models import UserProfile
# Create your views here.

logger = logging.getLogger('smallplan')

def index(request):
    """
        首页
        :param request:
        :return:
    """
    return render_to_response("index.html")

def login(request):
    """
        登录注册
        :param request:
        :return:
    """
    if request.method == 'POST':
        username = request.POST.get('account')
        password = request.POST.get('password')

        if UserProfile.objects.filter(username__exact=username).filter(password__exact=password).count() == 1:
            logger.info('{username} 登录成功'.format(username=username))
            request.session["login_status"] = True
            request.session["now_account"] = username
            return HttpResponseRedirect('/api/index/')
        else:
            logger.info('{username} 登录失败, 请检查用户名或者密码'.format(username=username))
            request.session["login_status"] = False
        return render_to_response("login.html")
    elif request.method == 'GET':
        return render_to_response("login.html")

def register(request):
    """
        登录注册
        :param request:
        :return:
    """

    return render_to_response("register.html")

def blog(request):
    """
        主创博客
        :param request:
        :return:
    """
    return render_to_response("blog.html")

def blogDetail(request):
    """
        文章展示页
        :param request:
        :return:
    """
    return render_to_response("blogDetail.html")

def Teammembers(request):
    """
        主创成员介绍
        :param request:
        :return:
    """
    return render_to_response("Teammembers.html")

def download(request):
    """
        下载
        :param request:
        :return:
    """
    return render_to_response("download.html")

def sudoku(request):
    """
        小游戏-数独
        :param request:
        :return:
    """
    return render_to_response("sudoku.html")