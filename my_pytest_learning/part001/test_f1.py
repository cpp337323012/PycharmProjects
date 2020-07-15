# coding:utf-8

import pytest

# 不带参数参数时，默认scope = 'function'

@pytest.fixture()
def login():
    print('请输入账号，密码登录')

def test_1(login):
    print('需要先登录，在做其他操作111')

def test_2():
    print('不需要做登录，可以做其他操作222')

def test_3(login):
    print('需要先登录,在做其他操作333')

if __name__ == '__main__':
    pytest.main(['-s', 'test_f1'])
