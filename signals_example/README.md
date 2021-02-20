**自定义信号**

1. 创建信号实例化对象
```python
from django.dispatch import Signal

django_ready = Signal()
```

2. 编写并注册信号处理方法
```python
from django.dispatch import receiver

from signals_example.signals import django_ready


@receiver(django_ready)
def monkey_patch_settings(sender, **kwargs):
    print('a')

```

3. 发送信号
```python
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

```
**注意⚠️** 信号发送之前需要将信号处理函数加载至内存中，确保信号发送时，内存中存在对应大的处理函数，否则无法正常处理。


**example 使用pre_save编写创建用户时的**

#### 参考链接
[signals 官方文档](https://docs.djangoproject.com/en/3.1/topics/signals/)

[signals 内置信号列表](https://docs.djangoproject.com/en/3.1/ref/signals/)
