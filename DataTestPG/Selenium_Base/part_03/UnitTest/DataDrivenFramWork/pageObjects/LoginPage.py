# encoding:utf-8
from util.ObjectMap import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def switchToFrame(self):
        self.driver.swich_to.frame('x-xrs')

    def switchToDefaultFrame(self):
        self.driver.swich_to.default_content()

    def usernameObj(self):
        try:
            elementObj = getElement(self.driver, 'xpath', '/input[@name="email"]')
            return elementObj

        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            elementObj = getElement(self.driver, 'xpath', '//input[@name="password"]')
            return elementObj

        except Exception as e:
            raise e

    def loginButton(self):
        try:
            elemenObj = getElement(self.driver, 'id', 'dologin')
            return elemenObj

        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    driver.implicitly_wait(3)
    driver.maximize_window()

    url = 'http://mail.126.com'
    driver.get(url)