#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/2/5 上午12:00
# software: PyCharm
# project: django_sample
from django.urls import path

from paginator_example.views import UserEndPoint, UserV2EndPoint

urlpatterns = [
    path('users', UserEndPoint.as_view()),
    path('users_v2', UserV2EndPoint.as_view())
]
