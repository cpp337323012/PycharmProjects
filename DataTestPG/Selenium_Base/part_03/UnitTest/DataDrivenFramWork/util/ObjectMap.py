# encoding:utf-8
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个元素
def getElement(driver, locatetype, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locatetype, value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个元素
def getElements(driver, locatetype, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locatetype, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
    driver.implicitly_wait(3)
    driver.maximize_window()

    url = 'http://www.baidu.com'
    driver.get(url)
    searchBox = getElement(driver, 'id', 'kw')
    print(searchBox.tag_name)
    alist = getElements(driver, 'tag name', 'a')
    print(alist)
    driver.quit()
