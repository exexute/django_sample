from django.dispatch import Signal
from django.test import TestCase


# Create your tests here.

def my_callback(sender, **kwargs):
    print('request finished!')


Signal.connect(my_callback, )
