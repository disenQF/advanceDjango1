#!/usr/bin/python3
# coding: utf-8
from django.urls import path, re_path
from user import views

app_name = 'user'

urlpatterns = [

    path('regist/', views.regist, name='regist1'),
    path('regist/<user_id>/', views.regist, name='regist2'),
]
