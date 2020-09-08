# encoding:utf-8
from pageObjects.LoginPage import LoginPage


class LoginAction:
    def __init__(self):
        print('login...')

    @classmethod
    def login(cls, driver, username, password):
       try:
            loginpage = LoginPage(driver)
            loginpage.switchToFrame()
            loginpage.usernameObj().send_keys('xxx')
            loginpage.passwordObj().send_keys('xxx')
            loginpage.loginButton().click()
       except Exception as e:
           raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    url = 'http://mail.126.com'
    driver.get(url)
    LoginAction.login(driver, username='XXX', password='123')
    time.sleep(4)
    driver.quit()





