# coding:utf-8

import pytest
import allure

@allure.feature('购物车功能') #feature定义功能
class TestShopingTrolley(object):
    @allure.story('加入购物车') # story 定义用户场景
    def test_add_shopping_trolley(self):
        login('刘春明', '密码') # 调用"步骤函数"
        with allure.step("浏览商品"): # 讲一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('商品1', '刘春明') # attach可以打印一些附加信息
            allure.attach('商品2', 'liuchunming')
        with allure.step("点击商品"): # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            pass
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 'sucess' == 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车')
    def test_delete_shopping_trolley(self):
        pass

@allure.step('用户登录')# 还可以将一个函数作为一个步骤，调用此函数时，报告中输出一个步骤
def login(user, pwd):
    print(user, pwd)

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])


'''
使用了allure的特性：
@allure.feature 用于定义被测的功能，被测产品的需求点
@allure.story 用于定义被测功能的用户场景，既子功能点
with allure.step 用户讲一个测试用例，分成几个步骤在测试报告中输出
allure.attach 用于向测试报告中输入一些附加信息，通常是一些测试数据信息
@pytest.allure.step 将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤


'''