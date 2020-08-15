# encoding:utf-8

from selenium import webdriver
import unittest
import time
import ddt
from selenium.common.exceptions import NoSuchElementException
import logging, traceback
from XmlUtil import ParseXML
import os

# 初始化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='/Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_03/report.log',
    filemode='w'
)

currentPath = os.path.dirname(os.path.abspath(__file__))
dataFilePath = os.path.join(currentPath, "TestData")
print(dataFilePath)

xml = ParseXML(dataFilePath)


@ddt.ddt
class TestDome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    @ddt.data(*xml.getDataFromXml())
    def test_dataDrivenByXml(self, data):
        testData, expectData = data['name'], data['author']
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        print(testData, expectData)
        self.driver.implicitly_wait(3)

        try:
            self.driver.find_element_by_id('kw').send_keys(testData)
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error('查找页面不存在元素,异常堆栈信息：'+ str(traceback.format_exc()))
        except AssertionError as e :
            logging.info(f'搜索：{testData}，期望：{expectData}，失败')
        except Exception as e :
            logging.error('未知错误，错误信息'+ str(traceback.format_exc()))
        else:
            logging.info(f'搜索：{testData}，期望：{expectData}，失败')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()
