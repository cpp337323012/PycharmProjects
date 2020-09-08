# encoding:utf-8
from selenium import webdriver
from appModules.LoginAction import LoginAction
import time


def testMailLogin():
    try:
        driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
        driver.implicitly_wait(3)
        driver.maximize_window()
        time.sleep(3)

        LoginAction.login(driver, 'xxx', 'xxx')
        time.sleep(3)
        assert '未读邮件' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()


if __name__ == '__main__':
    testMailLogin()
