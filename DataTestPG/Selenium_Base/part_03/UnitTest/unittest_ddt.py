# encoding:utf-8

from selenium import webdriver
import unittest
from ddt import ddt, data, unpack
import time
import logging
import traceback
from selenium.common.exceptions import NoSuchElementException

# 初始化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='/Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_03/report.log',
    filemode='w'
)


@ddt
class TestDome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    @data(['神奇的动物在哪里', '叶青'], ['疯狂的动物城', '古文特'])
    @unpack
    def test_dataDriverByObj(self, testdata, expectdata):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)

        except NoSuchElementException as e:
            logging.error('查找页面元素不存在'+str(traceback.format_exc()))

        except AssertionError as e:
            logging.info(f'搜索{testdata}，期望{expectdata}，失败')

        except Exception as e:
            logging.error('未知错误信息' + str(traceback.format_exc()))

        else:
            logging.info(f'搜索{testadata}， 期望{expecteddata}， 失败')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

