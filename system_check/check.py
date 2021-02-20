#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/2/19 上午9:51
# software: PyCharm
# project: django_sample
from django.core.checks import Error, register, Tags


# fixme 完成系统检查的demo，学习django系统检查框架的使用，了解使用场景
@register(Tags.compatibility)
def example_check(app_configs, **kwargs):
    errors = []
    # do check in there
    check_failed = False
    checked_object = None

    if check_failed:
        errors.append(
            Error(
                'error name',
                hint='this is error hint',
                obj=checked_object,
                id='check.id'
            )
        )
