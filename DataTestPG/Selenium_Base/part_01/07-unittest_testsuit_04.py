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
            self.assertIs(a, b, f'{a},{b}不属于同一个对象')
        except AssertionError as e:
            print(e)

    # test_assertIsNot()方法实例
    def test_assertIsNot(self):
        # 断言两个变量类型不属于同一个对象
        try:
            a = 12
            b = 'test'
            self.assertIsNot(a, b, f'{a},{b}属于同一个对象')
        except AssertionError as e:
            print(e)

    # assertIsNone()方法实例
    def test_assertIsNone(self):
        # 断言结果为None
        try:
            result = MyClass.return_None()
            self.assertIsNone(result, "not is None")
        except AssertionError as e:
            print(e)

    # assertIsNotNone()方法实例
    def test_assertIsNotNone(self):
        # 断言结果不为None
        try:
            result = MyClass.return_None()
            self.assertIsNotNone(result, "is None")
        except AssertionError as e:
            print(e)

    # assertIn()方法
    def test_assertIn(self):
        # 断言对象A是都包含在对象B中
        try:
            strA = MyClass.sum(2, 5)
            strB = "is"
            self.assertIn(strB, strA, f'{strB}不包含在{strA}中')
        except AssertionError as e:
            print(e)

    # assertNotIn()方法
    def test_assertNotIn(self):
        try:
            strA = "this is a start"
            strB = "Selenium"
            self.assertNotIn(strB, strA,f'{strB}包含在{strA}中' )
        except AssertionError as e:
            print(e)

    # assertIsInstance()方法
    def test_assertIsInstance(self):
        # 测试对象A的类型是否是指定的类型
        try:
            x = MyClass
            y = object
            self.assertIsInstance(x, y, f'{x}的类型不是{y}')
        except AssertionError as e:
            print(e)

    # assertNotIsInstance()方法
    def test_assertNotIsInstance(self):
        # 测试对象A的类型是否是指定的类型
        try:
            x = 123
            y = str
            self.assertNotIsInstance(x, y, f'{x}的类型不是{y}')
        except AssertionError as e:
            print(e)

    # assertRaises()方法
    def test_assertRaises(self):
        # 测试抛出的指定异常类型
        # assertRaises(exception)
        with self.assertRaises(ValueError) as cm:
            random.sample([1, 2, 3, 4, 5], 'j')
        # 打印详细的异常信息
        print('===', cm.exception)

        # assetRaises(exception, callable, *agrs, **kwds)
        try:
            self.assertRaises(ZeroDivisionError, MyClass.div, 3, 0)
        except ZeroDivisionError as e:
            print(e)

    #assertRaisesRegexp()方法实例
    def test_assertRaisesRegexp(self):
        # 测试抛出的指定异常类型，并用正则验证
        with self.assertRaisesRegexp(ValueError, 'literal') as ar:
                int("xyz")
        # 打印详细的异常信息
        print(ar.exception)
        # 打印正则
        print(ar.expected_regexp)

        # assertRaisesRegexp(exception, regexp, callable, *args, **kwds)
        try:
            self.assertRaisesRegexp(ValueError, 'invalid literal for,*ZZZ$', int, 'XYZ')
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()