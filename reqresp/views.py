from django.urls import reverse

import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def qs(request):
    return HttpResponse('hello !!')

def qs_hello(request):
    # 反解析
    # url = reverse('reqresp:qs') # 反解析的url　
    # print(url)
    # print(request.path) # 当前请求的ｕｒｌ
    # return HttpResponse('qs    hello !!')
    # 重定向
    return redirect(reverse('reqresp:qs'))

def demo_view(request,city,weather):
    print(weather)
    print(city)
    return HttpResponse('OK')

def get_qs(request):
    a = request.GET.get("a")
    a_list = request.GET.getlist('a')
    b = request.GET.get('b')
    print(a,a_list,b)
    return HttpResponse('OK')

def get_form_data(request):
    print(request.POST.get('a'))
    print(request.POST.get('b'))
    return HttpResponse('OK')


def get_json_data(request):
    body_data = request.body
    print(type(body_data))
    str_data = body_data.decode()
    print(type(str_data))
    print(str_data)
    data = json.loads(str_data)
    print(data('a'))
    return HttpResponse('OK')

def get_header(request):
    print(request.method)
    print(request.META)
    print(request.META['PYTHONIOENCODING'])
    return HttpResponse('OK')

def get_resp(request):
    return HttpResponse({'a':12,'itcast':'python'},content_type = 'application/json')

