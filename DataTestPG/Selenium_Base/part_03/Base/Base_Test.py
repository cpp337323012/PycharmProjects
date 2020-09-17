# coding:utf-8

from selenium import webdriver
import unittest


# # 启动浏览器
# driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
# # 打开请求地址
# driver.get(url='http://www.baidu.com')
# # 浏览器最大化
# driver.maximize_window()
# # 隐式等待
# driver.implicitly_wait(3)
# # 退出浏览器
# driver.quit()

class Test_Dome(unittest.TestCase):
    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
        # 打开请求地址
        self.driver.get(url='http://www.baidu.com')
        # 浏览器最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

    def test_demo(self):
        print('03')
        current_title = self.driver.title
        print(self.driver.title)
        self.assertEqual(current_title, '百度一下')

    def test_01(self):
        print('01')
        self.driver.find_element_by_id('kw').send_keys('曹鹏')
        self.driver.find_element_by_id('su').click()

    def test_demo2(self):
        print('02')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test_Dome('test_demo'))
    suite.addTest(Test_Dome('test_demo2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
