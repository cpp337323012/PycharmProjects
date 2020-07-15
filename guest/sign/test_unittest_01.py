# coding:utf-8

import unittest
from module import Calculator

class ModuleTest(unittest.TestCase):
    # 导入unittest创建ModuleTest继承unittest.TestCase
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        pass
    # 测试方法
    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    # unittest.main()
    # 构造测试集，通过addTest添加测试案例
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)




