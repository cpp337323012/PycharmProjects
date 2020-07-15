# coding:utf-8

import time
import sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from  unittest import defaultTestLoader
from db_fixture import test_data



# 指定测试用例为当前文件夹下interface目录
test_dir = './interface'
discover = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="Guest Manage System Interface Test Report",
        description='运行环境：MySQL(PyMySQL), Requests, unittest')
    runner.run(discover)
    fp.close()

    '''先调用test_data.py的init_data()初始化测试数据
    
    使用unittest框架的discover()，查找interface/目录下，匹配所有文件名称以"_test.py"结尾的测试文件
    
    HTMLTestRuner()类替代unittest单元测试框架的TextTestRunner()类，运行discover中匹配的测试用例，生成HTML报告
    '''
