# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
driver.implicitly_wait(3)
driver.maximize_window()

url = 'http://mail.126.com'
driver.get(url)
time.sleep(3)
userName = driver.find_element_by_xpath('//input[@name="email"]')
userName.send_keys('XXXX')
pwd = driver.find_element_by_xpath('//input[@name="password"]')
pwd.send_keys('XXXX')
pwd.send_keys(Keys.RETURN)

time.sleep(3)
driver.find_element_by_xpath('//div[text()="通讯录"]').click()
time.sleep(2)
driver.find_element_by_xpath('//span[text()="新建联系人"]').click()
time.sleep(2)
# 添加姓名
driver.find_element_by_xpath('//*[@id="input_N"]').send_keys('lucy')
# 添加电子邮箱
driver.find_element_by_xpath('//*[@id="_mail_input_25_388"]').send_keys('XXXX@qq.com')
# 设置为星标联系人
driver.find_element_by_xpath('//*[@id="fly1"]').click()
time.sleep(2)
driver.quit()
