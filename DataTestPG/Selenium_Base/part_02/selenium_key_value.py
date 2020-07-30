# encoding:utf-8
from selenium import webdriver


class TestKeyWords:
    # 初始化
    def __init__(self, url, browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)

    # 调用浏览器
    def open_browser(self, browser_type):
        if browser_type == 'chrome':
            driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
            return driver
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print('不在支持范围内')

    # 获取元素
    def locator(self, locator_type, value):
        if locator_type == 'xpath':
            el =  self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el

    # 输入
    def input_text(self, locator_type, value, text):
        self.locator(locator_type, value).send_keys(text)

    # 点击
    def click_element(self, locatr_type, value):
        self.locator(locatr_type, value).click()

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    tk = TestKeyWords('http://www.baidu.com', 'chrome')
    tk.input_text('id', 'kw', '虚竹')
    tk.click_element('id', 'su')
