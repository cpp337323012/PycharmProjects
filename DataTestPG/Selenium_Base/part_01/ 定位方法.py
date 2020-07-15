from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')

# driver.get('file:///Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_01/choose_test.html')
driver.get('file:///Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_01/Alert_test.html')
time.sleep(2)
driver.maximize_window()
# 隐式等待最多2s
driver.implicitly_wait(2)

# id选择元素,返回元素为webelement对象
# element = driver.find_element_by_id('kw')
# # 通过webelement对象，就可以控制页面元素进行操作
# element.send_keys('python')
# # 查找单个元素,返回符合条件的第一个元素，如果没有查询结果则报错
# element = driver.find_element_by_id('su')
# element.click()
# 查找多个元素，返回多个符合条件，如果没有查询结果则返回空列表
# elements = driver.find_elements_by_class_name('animal')
# for ele in elements:
#     print(f'动物类的{ele.text}')


# elements = driver.find_elements_by_tag_name('span')
# for ele in elements:
#     print(ele.text)
#
# css_elem = driver.find_element_by_css_selector('.animal')
# print(f'css选择结果:{css_elem.text}')

# 切换iframe
#
# element = driver.find_element_by_css_selector('#s_radio input[checked="checked"]')
# print(f"当前选种是:{element.get_attribute('value')}")
# time.sleep(2)

# checkbox选择
'''1.先取消checkbox勾选
   2.再选择目标'''

# elements = driver.find_elements_by_css_selector('#c_checkbox input[checked="checked"]')
#
# for element in elements:
#     print(f'当前CheckBox选择是:{element.get_attribute("value")}')
#     element.click()
#
# new_element = driver.find_element_by_css_selector('#c_checkbox input[value="小雷老师"]')
# new_element.click()
# print(f'修改后的CheckBox选择是：{new_element.get_attribute("value")}')

# 创建Select对象
# select = Select(driver.find_element_by_id("ss_single"))
#
# # 通过Select对象选择小雷老师
# new_select = select.select_by_visible_text("小雷老师")
#
# print(f"current select：{new_select}")

# 多个对象的Select对象操作时，先全选取消select选择
# element = driver.find_element_by_id("ss_multi")
# # 清除所select选项
# element_select = Select(element)
# element_select.deselect_all()
#
# # 选择新的select目标
# new_select_one = element_select.select_by_visible_text("小雷老师")
# new_select_sec = element_select.select_by_visible_text("小江老师")

'''prompt'''
driver.find_element_by_id('b3').click()

# 获取Alert对象
alert = driver.switch_to.alert

# 打印弹出框内容
print(alert.text)

# 输入信息，并且点击ok
alert.send_keys('AI人工智能')
alert.accept()

# 点击Cancel按钮取消
driver.find_element_by_id('b3').click()
alert = driver.switch_to.alert
alert.dismiss()
'''弹出对话框'''
driver.close()


