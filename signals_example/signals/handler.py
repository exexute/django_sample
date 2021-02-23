#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/2/20 上午9:37
# software: PyCharm
# project: django_sample
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from signals_example.signals import django_ready


@receiver(django_ready)
def monkey_patch_settings(sender, **kwargs):
    print('a')


@receiver(pre_save, sender=User)
def regisiter_user(sender, **kwargs):
    model = kwargs['instance']
    user = User.objects.filter(username=model.get_username()).first()
    if not user:
        # fixme 发送注册验证邮件前，创建用户唯一凭证，可使用django内置的sign创建验证token
        model.email_user(subject='用户注册', message='欢迎注册xxxx，请访问链接xxxx进行验证。', from_email='owefsad@gmail.com')
        model.is_active = False
