#coding:utf-8
import unittest
import HTMLTestRunner
import math

class Calc(object):

    def add(self, x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    def sub(self, x, y, *d):
        # 减法计算
        result = x - y
        for i in d:
            result -= i
        return result

class SuiteTestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    @unittest.skip("skipping")
    def test_Sub(self):
        print('Sub')
        self.assertEqual(self.c.sub(100, 34, 6), 60, '求差结果错误')

    def test_Add(self):
        print('Add')
        self.assertEqual(self.c.add(1, 32, 56), 89, '求和结果错误')


class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_Pow(self):
        print('Pow')
        self.assertEqual(pow(6, 3), 216, '求幂结果错误')

    def test_hasattr(self):
        print('hasattr')
        self.assertEqual(hasattr(math, 'pow'), '检测的属性不存在')


if __name__ == '__main__':

    suite1 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)

    suite = unittest.TestSuite([suite1, suite2])
    filename = './test.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Report_title', description='Report_description')
    # 运行测试集合
        runner.run(suite)

'''执行testcase成功，未生成测试报告，参考：https://blog.csdn.net/huilan_same/article/details/51727572解决'''
