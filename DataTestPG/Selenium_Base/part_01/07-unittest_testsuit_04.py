# coding:utf-8

import unittest
import random
# 被测试类

class MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b

    @classmethod
    def div(cls, a, b):
        return a / b

    @classmethod
    def return_None(cls):
        return None
# 单元测试类
class MyTest(unittest.TestCase):

    # assertEqual()方法实例
    def test_assertEqual(self):
        # 断言两数之和的结果
        try:
            a,b = 1, 2
            sum = 13
            self.assertEqual(a + b, sum, f'断言失败:{a} + {b} != {sum}')
        except AssertionError as e:
            print(e)

    # assertNotEqual()方法实例
    def test_assertNotEqual(self):
        # 判断两个数之间差的结果,如果相等则抛出异常
        try:
            a, b = 5, 2
            res = 3
            self.assertNotEqual(a - b , res, f'断言失败：{a} + {b} = {res}')
        except AssertionError as e:
            print(e)

    # assertTrue()方法实例
    def test_assertTrue(self):
        # 断言表达式为真
        try:
            self.assertTrue(1 == 1, '表达式为假')
        except AssertionError as e:
            print(e)

    # assertFalse()方法实例
    def test_assertFalse(self):
        # 断言表达是为假
        try:
            self.assertFalse(3 == 2, '表达式为真')
        except AssertionError as e:
            print(e)

    # assetIs()方法实例
    def test_assertIs(self):
        # 断言两变量类型属于同一个对象
        try:
            a = 12
            b = a
            self.assertIs(a, b, f'{a},{b}属于同一个对象')


if __name__ == '__main__':
    unittest.main()