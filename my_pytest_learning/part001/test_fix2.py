# coding:utf-8

import pytest

def test_s4(login):
    print('案例4，登录后再操作')

def test_s5():
    print('案例5，直接操作')

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])


'''
通过conftest.py文件抽象，可实现测试案例，调用公共前置条件login()
'''