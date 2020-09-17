# encoding:utf-8

import unittest
from selenium import webdriver
from part_03.PageObject.search_page import SearchPage
from ddt import ddt, data


@ddt
class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    @data('http://www.baidu.com')
    def testSearch(self, url):
        self.sp = SearchPage(self.driver, url)
        self.sp.check('西天取经')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
