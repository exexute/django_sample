#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/31 上午9:13
# software: PyCharm
# project: django_sample
from django.urls import path

from log_sample_normal.views import SampleLogEndPoint

urlpatterns = [
    path('sample_log', SampleLogEndPoint.as_view())
]
