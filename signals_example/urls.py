#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/31 上午9:13
# software: PyCharm
# project: django_sample
from django.urls import path

from signals_example.views import ExampleEndPoint

urlpatterns = [
    path('example', ExampleEndPoint.as_view())
]
