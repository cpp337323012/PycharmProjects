# coding:utf-8
import allure
import yaml
import pytest
from selenium import webdriver

driver = None
@pytest.mark.hookwrapper()
@pytest.fixture()


def login():
    print('请先输入账号')

def pytest_runtest_makereport(item):
    '''
    当案例失败时，截图保存到html测试报告中
    :param item:
    :return:
    '''
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

@pytest.fixture(scope='session', autouse=True)
def env(request):
    '''
    parse env config info
    :param request:
    :return:
    '''
    root_dir = request.config.rootdir
    config_path = '{0}/config/env_config.yml'.format(root_dir)
    with open(config_path) as f:
        env_config = yaml.load(f) # 读取配置文件
        
    allure.environment(host=env_config['host']['domain'])# 测试报告中展示host
    allure.environment(browser=env_config['host']['browser']) # 测试报告中展示browser
    
    return env_config
