from django.shortcuts import render
import sys
import os
import logging
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
# Create your views here.

logger = logging.getLogger('smallplan')

def index(request):
    """
        首页
        :param request:
        :return:
    """
    return render_to_response("index.html")