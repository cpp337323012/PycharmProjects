#encoding:utf-8

# import requests
#
# # 查询发布会接口
#
# url = 'http://127.0.0.1:8000/api/get_event_list/'
# r = requests.get(url, params={'eid': '1'})
# result = r.json()
#
# # 断言接口返回值判断
# assert result['status'] == 200
# assert result['message'] == 'success'
# assert result['data']['name'] == 'XX产品发布会'
# assert result['data']['address'] == '北京国家会议中心


'''
将测试脚本集成到uniitest中
'''

# import unittest
# import requests
#
#
# class GetEventListTest(unittest.TestCase):
#     '''查询发布会接口测试'''
#
#
#     def setUp(self):
#         self.url = 'http://127.0.0.1:8000/api/get_event_list/'
#
#
#     def test_get_event_null(self):
#         '''发布会id为空'''
#         r = requests.get(self.url, params={'eid':''})
#         result = r.json()
#         self.assertEqual(result['status'], 10021)
#         self.assertEqual(result['message'], 'parameter error')
#
#
#     def test_get_event_error(self):
#         '''发布会id错误'''
#         r = requests.get(self.url, params={'eid':'901'})
#         result = r.json()
#         self.assertEqual(result['status'], 10022)
#         self.assertEqual(result['message'], 'query result is empty')
#
#
#     def test_get_event_success(self):
#         '''发布会id为1， 查询成功'''
#         r = requests.get(self.url, params={'eid':'1'})
#         result = r.json()
#         self.assertEqual(requests['status'], 200)
#         self.assertEqual(result['message'], 'success')
#         self.assertEqual(result['data']['name'], "小米5发布会")
#         self.assertEqual(result['data']['address'], "北京国家会议中心")
#         self.assertEqual(result['data']['stat_time'], "2016-12-08T14:29:21")
#
# if __name__ == '__main__':
#     unittest.main()

''' unittest已经完成大部分工作，只需要继承数据初始化功能，和HTMLTestRunner来生成测试报告，即接口测试框架就完成了
    接口自动化测试框架处理过程：
    1. 接口测试框架先向数据库中插入测试数据
    2. 调用被测系统所提供的接口
    3. 系统接口根据传参(username='Tom')向测试数据库中进行查询得到Tom个人信息
    4. 将查询结果组成json格式数据，返回给测试框架
    5. 通过单元测试框架断言接口返回的数据（Tom的个人信息），并生成测试报告
    
'''

