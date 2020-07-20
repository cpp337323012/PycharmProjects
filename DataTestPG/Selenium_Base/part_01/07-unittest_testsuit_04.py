# coding:utf-8

import unittest
import random
# 被测试类
def MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def div(cls, a, b):
        return a / b

    @classmethod
    def return_None(cls):
        return None

myclass = MyClass()
myclass.sum(1,2)