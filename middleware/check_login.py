#!/usr/bin/python3
# coding: utf-8
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CheckLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 从请求到路由urls过程，触发此函数
        print('---CheckLoginMiddleware--', 'process_request')
        print(request.path,
              request.COOKIES)
        dontfilters = ['/user/login/', '/user/code/']
        if request.path not in dontfilters:
            # 验证用户是否登录
            if not request.COOKIES.get('token'):
                return HttpResponse('<h3>Login</h3><form><input><button>Login</button></form>')

    def process_view1(self, request, callback, callback_args, callback_kwargs):
        print('---CheckLoginMiddleware--', 'process_view')
        # callback 是调用的view函数
        # 新增一个关键参数， 类似于匹配路由 stock/<stock_id>/<page>/
        callback_kwargs['page'] = request.GET.get('page', 1)

        print(callback, callback_args, callback_kwargs)


    def process_response1(self, request, response):
        print('---CheckLoginMiddleware--', 'process_response')
        return response
