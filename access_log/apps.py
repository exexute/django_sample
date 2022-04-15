from django.apps import AppConfig


class AccessLogConfig(AppConfig):
    name = 'access_log'

    def ready(self):
        from access_log import handlers
