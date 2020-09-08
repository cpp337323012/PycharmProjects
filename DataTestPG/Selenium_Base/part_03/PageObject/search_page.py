# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage
from base_page import Page


class SearchPage(BasePage):
    input_id = (By.ID, 'kw')
    click_id = (By.ID, 'su')

    def input_text(self, input_text):
        self.locator_ele(self.input_id).send_keys(input_text)

    def click_element(self):
        self.locator_ele(self.click_id).click()

    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()
        self.quit_browser()


class Search(Page):

    search_input = (By.ID,"kw")
    search_button = (By.ID, 'su')

    def __init__(self, driver, base_url='http://www.baidu.com'):
        Page.__init__(self, driver, base_url)

    def gotoBaiduHome(self):
        self.driver.get(self.base_url)

    def input_search_text(self, text='selenium'):
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        self.click(self.search_button)
        



if __name__ == '__main__':
    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    url = 'http://www.baidu.com'
    sp = SearchPage(driver)
    #
    sp.check(url, '西天取经')


