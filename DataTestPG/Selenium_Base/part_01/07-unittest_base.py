# encoding = utf-8
import unittest
import random

class TestSequnceFunction(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def runTest(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)


class TestDictValueFormatFunction(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError,  random.shuffle, (1,2,3))


class myclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b

class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化固件'''
        print('---setUpclass')

    @classmethod
    def tearDownClass(cls):
            print('---tearDownclass')

    def setUp(self):
        self.a = 3
        self.b = 1
        print('--setup')

    def tearDown(self):
        print('---tearDown')


    def testsum(self):
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        self.assertEqual(myclass.sub(self.a, self.b), 3, 'test sub fail')


if __name__ == '__main':
    unittest.main()
    
    '''setUpClass()和tearDownClass()方法在整个测试类运行过程中执行了一次，
    setUp()和tearDown()每个测试方法执行前后都被调用'''