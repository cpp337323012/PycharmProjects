# encoding:utf-8
# 这是基础类


class BasePage:
    # driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

    # 构造函数
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 元素定位
    def locator_ele(self, locator):
        return self.driver.find_element(*locator)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 访问url
    def visit(self):
        self.driver.get(self.url)

