# -*- coding:utf-8 -*-
# @Time : 2022/10/6 15:14
# @Author : jiapeng
# @File : runlog.py
import logging

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='runlog.log',  # 日志输出文件
                    filemode='a')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")
