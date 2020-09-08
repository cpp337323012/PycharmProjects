# encoding:utf-8

import unittest
from selenium import webdriver
from part_03.PageObject.search_page import Search

class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome

    def testSearch(self):
        driver =  self.driver
        url = 'http://www.baidu.com'
        text = 'selenium'
        assert_title = 'selenium_搜索'
        search_Page = Search(driver, url)

        search_Page.gotoBaiduHome()
        search_Page.input_search_text(text)
        search_Page.click_search_btn()

        self.assertEqual(search_Page.get_title(), assert_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()