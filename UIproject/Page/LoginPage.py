# -*- coding:utf-8 -*-
# @Time : 2022/10/4 23:19
# @Author : jiapeng
# @File : LoginPage.py
'''
登陆页面
'''
import time

from selenium.webdriver.common.by import By

from UIproject.Base.BaseObject import Basepage


class LoginPage(Basepage):
    # 页面属性
    url='https://passport.ctrip.com/user/login'
    username=(By.ID,'nloginname')
    password=(By.ID,'npwd')
    loginbutton=(By.ID,'nsubmit')
    selectbox=(By.CLASS_NAME,'agreement-checkbox')
    # 页面方法
    def Login(self,userName,passWord):
        self.GetUrl(url=self.url)
        time.sleep(2)
        self.sendkeys(loc=self.username,text=userName)
        time.sleep(2)
        self.sendkeys(loc=self.password,text=passWord)
        time.sleep(2)
        self.click(loc=self.selectbox)
        time.sleep(2)
        self.click(loc=self.loginbutton)

