# encoding;utf-8

from selenium import webdriver
import unittest
import ddt
import time
import logging, traceback
from part_03.UnitTest.test_data_excel.ExcelUtil import ParaseExcel
from selenium.common.exceptions import NoSuchElementException

# 初始化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='/Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_03/report.log',
    filemode='w'
)
excelPath = './测试数据.xlsx'
sheetName = '工作表1'
excel = ParaseExcel(excelPath, sheetName)


@ddt.ddt
class TestDome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    @ddt.data(*excel.getDatasFromSheet())
    def test_dataDrivenByFile(self, data):
        testData, expectData = tuple(data)
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
            logging.error('查找元素不存在，异常堆栈信息：' + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info(f'搜索：{testData}，期望：{expectData}，失败')
        except Exception as e:
            logging.error('未知错误，错误信息：'+ str(traceback.format_exc()))
        else:
            logging.info(f'搜索：{testData}，期望：{expectData}，失败')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

