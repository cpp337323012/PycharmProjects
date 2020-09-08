# coding:utf-8
from selenium import webdriver
from selenium.webdriver import Remote


def brower(url):
    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    driver.get(url)
    return driver


if __name__ == '__main__':
    dr = brower(url="http://www.baidu.com")
    dr.quit()
