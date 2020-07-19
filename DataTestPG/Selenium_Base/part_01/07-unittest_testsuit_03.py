'''忽略某个测试方法'''

#coding:utf-8
import random
import unittest
import sys

class TestSequceFunctions(unittest.TestCase):
    a = 1

    def setUp(self):
        self.seq = list(range(10))

    @unittest.skip("skipping") # 无条件忽略该测试方法
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    # 如果a > 5,则忽略
    @unittest.skipIf(a > 5, "condition is not satisfied")
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    # 除非执行测试用例的平台式windows平台，否则忽略该方法
    @unittest.skipUnless(sys.platform.startswith("linux"), "requires mac")
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
if __name__ == '__main__':
    # unittest.main()
    testCase = unittest.TestLoader().loadTestsFromTestCase(TestSequceFunctions)
    suite = unittest.TestSuite(testCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

