# -*- coding:utf-8 -*-
# @Time : 2022/10/5 23:39
# @Author : jiapeng
# @File : RunCase.py
import unittest
# 创建测试套件
from BeautifulReport import BeautifulReport

from UIproject.Testcase.test_LoginCase import LoginCase

# suite=unittest.TestSuite()
# 创建装载器
# loader=unittest.TestLoader()
# 执行某一个指定类的测试用例
# suite.addTests(loader.loadTestsFromTestCase(LoginCase))
# 运行某个文件夹里所有test_*开头的测试用例
suite=unittest.defaultTestLoader.discover('./Testcase')

# 创建运行器
# r=unittest.TextTestRunner()
# 运行测试用例
# r.run(suite)

# 生成测试报告
runner=BeautifulReport(suite)
runner.report(description='UI测试报告',report_dir='./Report')

