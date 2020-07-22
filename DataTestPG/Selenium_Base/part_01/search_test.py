import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        self.driver.get('http://www.baidu.com')

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys("铜钱贯")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.assertEqual(11, len(products))


    def test_search_by_category1(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys("铜钱贯")
        self.search_field.submit()


        products = self.driver.find_element_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.assertEqual(10, len(products))


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)



