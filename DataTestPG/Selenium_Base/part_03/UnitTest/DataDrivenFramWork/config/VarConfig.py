# encoding:utf-8

import os
# 获取当前文件所在的目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放在页面元素定表达式文件
pageElemenetLocatorPath = parentDirPath + './config/PageElementLocator.ini'
