# coding:utf-8

from mock import mock
# 模拟mock封装
def mock_test(mock_method, request_data, url, method, response_data):
    mock_data = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return  res


