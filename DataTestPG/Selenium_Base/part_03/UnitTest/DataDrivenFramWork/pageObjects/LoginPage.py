# encoding:utf-8
from util.ObjectMap import *
from util.ParaseConfigurationFile import ParaseCofigFile


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.paraseCf = ParaseCofigFile()
        self.loginOptions = self.paraseCf.getItemSection('126mail_login')
        print(self.loginOptions)

    def switchToFrame(self):
        try:
            # 从定位表达式配置文件中读取frame的定位表达式
            locatorExpression = self.loginOptions['loginPage.frame'.lower()].split('>')[1]
            self.driver.swich_to.frame(locatorExpression)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.swich_to.default_content()
        except Exception as e:
            raise e

    def usernameObj(self):
        try:
            locateType, locatorExpression = self.loginOptions['loginPage.username'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj

        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType, locatorExpression = self.loginOptions['loginPage.password'.lower().split('>')]
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj

        except Exception as e:
            raise e

    def loginButton(self):
        try:
            locateType, locatorExpression = self.loginOptions['loginPage.loginButton'.lower().split('>')]
            elemenObj = getElement(self.driver, locateType, locatorExpression)
            return elemenObj

        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time

    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    driver.implicitly_wait(3)
    driver.maximize_window()

    url = 'http://mail.126.com'
    driver.get(url)
    time.sleep(3)
    login = LoginPage(driver)
    login.switchToFrame()
    login.usernameObj().send_keys('xxx')
    login.passwordObj().send_keys('xxx')
    login.loginButton().click()
    login.switchToDefaultFrame()
    driver.quit()
