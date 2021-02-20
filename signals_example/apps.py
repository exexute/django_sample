import sys

from django.apps import AppConfig


class SignalsExampleConfig(AppConfig):
    name = 'signals_example'

    def ready(self):
        # 增加signal_handler处理函数的导入，提前加载处理函数，用于后续处理事件
        from . import signal_handler
        from .signals import django_ready
        if 'migrate' not in sys.argv:
            django_ready.send(AppConfig)
