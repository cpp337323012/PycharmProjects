# 导入uniitest模块
import unittest

# 继承TestCase类，TestCase类是测试用例类
class Test1(unittest.TestCase):
    def setUp(self):
        print('hello')

    def tearDown(self):
        print('bye')

    def test_001(self):
        print('001')

    def test_002(self):
        print('002')


if __name__ == '__main__':
    # unittest.main()
    # 创建测试套件
    suit = unittest.TestSuite()
    # 定义一个测试用例列表
    case_list = ['test_001', 'test_002']
    for case in case_list:
        suit.addTest(Test1(case))

    # 运行测试用例，verbosity=2 为每个测试用例输出报告，run的参数是测试套件
    unittest.TextTestResult(verbosity=2).run(suit)


