#encoding:utf-8

import unittest
from selenium   import webdriver
from selenium.common.exceptions import WebDriverException
import traceback
import time

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    def test_executeScript(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        # 构造JavaScript查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('kw').value='光荣之路'；"
        # 构造javaScript 查找百度首页的搜多按钮的代码字符串
        searchButtonJS = "document.getElementById('su').click()"
        try:
            # 通过javascript代码在百度首页搜索输入框中输入'光荣之路'
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            # 通过javascript代码单击百度首页的上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue(u'百度百科'in self.driver.page_source)
        except WebDriverException as e:
            # 当定位失败时，会抛出WebDriverException
            print('在页面中没有找到操作的页面元素', traceback.print_exc())
        except AssertionError as e:
            print('页面不存在断言的关键字')
        except Exception as e:
            # 发生其他异常时，打印堆栈信息
            print(traceback.print_exc())


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.mian()
