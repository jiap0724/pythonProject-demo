# -*- coding:utf-8 -*-
# @Time : 2022/10/4 22:35
# @Author : jiapeng
# @File : BaseObject.py
'''
第一层 基础层，封装一些页面常用方法：元素定位、元素操作

'''
from UIproject.Log.Log import logger


class Basepage():
#     相同属性 获取浏览器对象
    def __init__(self,driver):
        self.driver=driver
        # self.url=driver.get(url)
#     相同动作
#     元素定位
    def findelement(self,loc):
        # logger.info(f'请求方式: {method}，请求url: {url}, 请求参数：{res.request.body}, 服务器返回结果：{res.text}')
        return self.driver.find_element(*loc)
#     输入
    def sendkeys(self,loc,text):
        try:
            logger.info('正在定位{}元素，输入框输入值为{}'.format(loc,text))
            self.findelement(loc).send_keys(text)
        except Exception as e:
            logger.error('输入内容错误,%s'%e)


#     点击事件
    def click(self,loc):
        try:
            logger.info('正在定位{}元素，点击按钮'.format(loc))
            self.findelement(loc).click()
        except Exception as e:
            logger.error('未点击到相应元素,%s'%e)

#     访问链接
    def GetUrl(self,url):
        self.driver.get(url)

#     元素等待
    def wait(self):
        pass


