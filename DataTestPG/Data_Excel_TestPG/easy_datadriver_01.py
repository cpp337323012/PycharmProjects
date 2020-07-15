#encodong=utf-8

from selenium import webdriver
from ddt import ddt, data
import unittest
import time
from selenium.common.exceptions import NoSuchWindowException
'''
简单数据驱动测试
'''

@ddt
class addTest(unittest.TestCase):
    # 数据 可以是元组、列表、字典
    value = [['15682007112@souhu.com', 'c337323012','https://mail.souhu.com/fe/#/homepage'],
             ]
    def setUp(self):
        self.testUrl = 'https://mail.souhu.com/fe/#/login'
        self.driver = webdriver.Chrome(r'/usr/local/bin/chromedriver.exe')
        self.driver.get(self.testUrl

        @data(* value) # 解析数据
        @unpack # 用来解包，将每组的第一个数据传递给uname依次类推

    def test_case1(self, uname, password, expected):
        try:
            # 传入用户名
            username = self.driver.find_element_by_xapth("//input[@placeholder='请输入您的邮箱']")
            username.send_keys(uname)
            time.sleep(2)
            # 传入用户密码
            userpassword = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的密码']")
            userpassword.send_keys(password)
            # 提交表单
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            currenturl = self.driver.current_url
            self.assertEqual(expected, currenturl, '登录失败')
        except NoSuchWindowException as e:
            print(e)
            raise
        except AssertionError:
            print('期望值是{}, 实际值是{}'.format(expected, currenturl))
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()