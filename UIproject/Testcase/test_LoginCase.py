# -*- coding:utf-8 -*-
# @Time : 2022/10/4 23:58
# @Author : jiapeng
# @File : LoginCase.py

'''
登陆测试用例
'''

import unittest


from selenium import webdriver

from UIproject.Page.LoginPage import LoginPage

from ddt import file_data,ddt
@ddt
class LoginCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @unittest.skip
    @file_data('/Users/jiapeng/PycharmProjects/pythonProject-demo/UIproject/TestData/login_data.yaml')
    def test_zhengchang_login(self,**canshu):

        LoginPage(self.driver).Login(userName='15210068667',passWord='jiapeng0724')
        print(canshu['username'])
        print(canshu)

#     使用数据分离
    @file_data('/Users/jiapeng/PycharmProjects/pythonProject-demo/UIproject/TestData/login_data.yaml')
    def test_datafile_login(self, **kwargs):

        username=kwargs['username']
        password=kwargs.get('password')
        LoginPage(self.driver).Login(userName=username,passWord=password)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
