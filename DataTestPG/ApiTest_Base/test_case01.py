# coding:utf-8

import requests
import unittest
import os
import sys
from base_request import request

url = 'http://www.imooc.com'
data = {
    "username": "1111",
    "password": "2222"
}
host = 'http://www.imooc.com'
case_path = os.getcwd()
sys.path.append(case_path)


class TestCase01(unittest.TestCase):

    def setUp(self):
        print('case01开始执行')

    def tearDown(self):
        print('case01结束执行')

    def test_06(self):
        '''
         print('执行case06')
         flag = 'adfadfadfadfadsfaqeewr'
         s = 'fads'
         self.assertIn(s, flag, msg='不包含')
        '''
        res = request.run_main('get', url, data)
        print(res)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCase01('test_06')]
    runner = unittest.TextTestRunner()
    runner.run(suite)