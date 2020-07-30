import unittest
from selenium_key_value import TestKeyWords
import time
from ddt import ddt, data, unpack


@ddt
class TestForKey(unittest.TestCase):

    def setUp(self):
        self.tk = TestKeyWords('http://www.baidu.com', 'chrome')

    def tearDown(self):
        self.tk.quit_browser()

    # 测试用例1
    @data(['id', '虚竹'], ['id', '西天取经'])
    @unpack # list二次分解为多个参数
    def test_1(self, locator, input_value):
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element(locator, 'su')
        time.sleep(3)

    # 测试用例2
    # def test_2(self, input_value):
    #     self.tk.input_text('id', 'kw', input_value)
    #     self.tk.click_element('id', 'su')
    #     time.sleep(3)


if __name__ == '__main__':
    unittest.main()
