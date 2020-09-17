# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage


class SearchPage(BasePage):
    # 定义一个id = kw的元素
    input_id = (By.ID, 'kw')
    click_id = (By.ID, 'su')

    def input_text(self, text):
        self.locator_ele(self.input_id).send_keys(text)

    def click_element(self):
        self.locator_ele(self.click_id).click()

    def check(self, text):
        self.visit()
        self.input_text(text)
        self.click_element()
        self.quit_browser()


if __name__ == '__main__':
    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    sp = SearchPage(driver, url='http://www.baidu.com')
    #
    sp.check(text='西天取经')
