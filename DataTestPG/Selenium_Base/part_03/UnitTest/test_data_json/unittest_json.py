# encoding:utf-8

from selenium import webdriver
import time
import unittest
from ddt import ddt, file_data, unpack
import logging, traceback
from part_03.UnitTest.ReportTemplate import htmlTemplate
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='/Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_03/report.log',
    filemode='w'
)


@ddt
class TestDome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 整个测试用例只被执行一次
        TestDome.trStr = ""

    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
        status = None
        flag = 0

    @file_data("test_data_list.json")
    def test_dataDrivenByFile(self, value):
        flagDict = {0: 'red', 1: '#00AC4E'}
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        print(value)
        # 将json中的数据处理
        testdata, expectdata = tuple(value.strip().split("||"))

        self.driver.implicitly_wait(3)

        try:
            start = time.time()  # 当前时间时间戳
            startTime = time.strftime("%Y - %m - %d %H:%M:%S", time.localtime())

            self.driver.find_element_by_id("kw").send_keys(testdata)

            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)

        except NoSuchElementException as e:
            logging.error('查找的元素不存在，异常堆栈信息:' + str(traceback.format_exc()))
            status = 'fail'
            flag = 0

        except AssertionError as e:
            logging.info(f'搜索{testdata}, 期望{expectdata}, 失败')
            status = 'fail'
            flag = 0

        except Exception as e:
            logging.error('未知错误,错误信息:' + str(traceback.format_exc()))
            status = 'fail'
            flag = 0

        else:
            logging.info(f'搜索{testdata}, 期望{expectdata},通过')
            status = 'pass'
            flag = 1

        wasteTime = time.time() - start - 3
        TestDome.trStr += u'''
           <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style="color:%s">%s</td>
        </tr>
        <br>
        ''' % (testdata, expectdata, startTime, wasteTime, flagDict[flag], status)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        htmlTemplate(TestDome.trStr)


if __name__ == '__main__':
    unittest.main()
