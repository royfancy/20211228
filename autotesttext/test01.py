# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:34:22 2021

@author: user
"""

import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'#当前路径
discover = unittest.defaultTestLoader.discover(test_dir, 'iot_*.py')#iot_*.py表示iot_开头的所有测试用例
with open("./iot.html","wb") as fp:
    
    runner = HTMLTestRunner(stream=fp, title='科信云测试报告',description='测试用例情况:')
    runner.run(discover)

