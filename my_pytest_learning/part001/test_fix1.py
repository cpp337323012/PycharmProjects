# coding:utf-8
import pytest

def test_s1(login):
    print('用例1，登录后做其他操作')

def test_s2():
    print('用例2，直接操作')

def test_s3(login):
    print('用例3，登录后做其他操作')

if __name__ == '__main__':
    pytest.main(['-s', 'test_fix1.py'])