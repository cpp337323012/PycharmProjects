'''
添加测试集合的步骤：
    1.TestLoader(测试用例加载器)根据传入的参数获取相应的测试用例的测试方法
    2.makeSuite(通常是单元测试框架调用，才生产testsuite对象的实例)所有的测试用例组装成test suite集合
    3.最后将testsuite集合传给test runner
'''
# encoding:utf-8
import unittest
import random

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_choice(self):
        # 从序列seq中随机选取一个元素
        element = random.choice(self.seq)
        # 验证随机元素确实属于列表中
        self.assertTrue(element in self.seq)

    def test_sample(self):
        # 验证执行的语句是否抛出了异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        # 验证执行函数h时抛出了TypeError异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
if __name__ == '__main__':
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromModule(TestDictValueFormatFunctions)
    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite(testCase1, testCase2)
    # 设置verbosity=2，可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)


'''verbosity 小于等于 0，输出结果不提示执行成功的用例数
   verbosity 等于1 输出结果中仅以点（.）表示执行成功的用例数
   verbosity 大于等于2，可以输出每个案例详细信息，特别是在大量案例执行时，可以根据信息判断用例哪些失败
   TestRunner.run()返回一个TestResult实例对象，存储有测试用例执行过程中的详细信息，如需要可以使用dir()查看'''