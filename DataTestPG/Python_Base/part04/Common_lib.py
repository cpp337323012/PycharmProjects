from selenium import webdriver
import time

class Commonshare(object):
    # 初始化方法
    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

        # 设置隐式等待
        self.driver.implicitly_wait(3)
        # 设置浏览器最大化
        self.driver.maximize_window()

    def open_url(self, url):
        # 请求指定站点
        self.driver.get(url)
        time.sleep(3)

    def locateElement(self, locate_type, value):
        # 判断定位方法并调用相关方法
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        # 如果el不为None,则返回
        if el is not None:
            return el

     # 指定为某一个元素的点击操作
    def click(self, locate_type, value):
        # 调整定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()
        time.sleep(1)

    # 对指定的元素进行数据输入
    def input_data(self, locate_type, value, data):
        # 调整定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        # 执行输入操作
        el.send_keys(data)

    # 获取指定元素的文本内容
    def get_text(self, locate_type, value):
        # 调整定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        return el.text

    # 获取指定元素的属性值
    def get_attr(self, locate_type, value, data):
        # 调整定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)

    # 收尾清理方法
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    pass


