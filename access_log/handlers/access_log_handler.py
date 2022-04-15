#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/4/30 下午4:28
# project: django_sample
from django.dispatch import receiver
from dongtai_signals.signals import view_access


@receiver(view_access)
def record_log(sender, **kwargs):
    print('触发access log')
