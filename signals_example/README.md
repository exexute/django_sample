### Django 信号开发规范
1. 自定义信号及信号处理程序应该放在`signals`子模块中
2. 在django app的`ready`方法中导入signals子模块或将信号连接至接收器函数

### Django信号的特性
- 信号与信号接收器之间是同步调用，只能解藕应用，不能实现异步

### 自定义信号及使用步骤
1. 创建自定义信号
2. 编写信号接收器函数
3. 连接/注册接收器函数
4. 发送信号

#### 1.创建信号实例化对象
```python
from django.dispatch import Signal

django_ready = Signal()
```

#### 2.编写信号接收器函数
```python
def monkey_patch_settings(sender, **kwargs):
    print('a')

```

#### 3.连接/注册接收器函数
```python
from django.dispatch import receiver

from signals_example.signals import django_ready

# 方式一：注册接收器函数
@receiver(django_ready)
def monkey_patch_settings(sender, **kwargs):
    print('a')

# 方式二：连接接收器函数
django_ready.connect(monkey_patch_settings)
```

#### 4.发送信号
```python
import sys

from django.apps import AppConfig


class SignalsExampleConfig(AppConfig):
    name = 'signals_example'

    def ready(self):
        # 增加signal_handler处理函数的导入，提前加载处理函数，用于后续处理事件
        from signals_example.signals import handler
        from signals_example.signals import django_ready
        if 'migrate' not in sys.argv:
            django_ready.send(AppConfig)

```
**注意⚠️** 信号发送之前需要将信号处理函数加载至内存中，确保信号发送时，内存中存在对应大的处理函数，否则无法正常处理。


**example 使用pre_save编写创建用户时的**

#### 参考链接
[signals 官方文档](https://docs.djangoproject.com/en/3.1/topics/signals/)

[signals 官方文档-中文](https://docs.djangoproject.com/zh-hans/3.1/topics/signals/)

[signals 内置信号列表](https://docs.djangoproject.com/en/3.1/ref/signals/)
