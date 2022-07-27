# -*- coding:utf-8 -*-
# @Time : 2022/7/25 21:28
# @Author : jiapeng
# @File : RunCase.py

'''
运行所有测试用例 并生成测试报告
'''
import unittest

from BeautifulReport import BeautifulReport

from ApiProject.testcase.testdemo import TestDemoJp
from ApiProject.testcase.testtianqi import TestTianQi


def zhidingcase():
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(TestTianQi("test_query_tianqi"))
    allsuite=loader.loadTestsFromTestCase(TestDemoJp)
    suite.addTests(allsuite)
    return suite

if __name__ == '__main__':
    runner=BeautifulReport(zhidingcase())
    runner.report(description='demoAPi测试',report_dir='./report')
