#encoding:utf-8

from selenium import webdriver
import sys
from.driver import brower
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = brower()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
