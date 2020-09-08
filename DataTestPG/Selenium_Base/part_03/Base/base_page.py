# encoding:utf-8
# 这是基础类
from selenium import webdriver


class BasePage:
    #driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator_ele(self, locator):
        return self.driver.find_element(*locator)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 访问url
    def visit(self, url):
        self.driver.get(url)

class BasePage:
    def __init__(self, driver):
        self.driver = driver


