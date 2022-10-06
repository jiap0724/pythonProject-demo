# -*- coding:utf-8 -*-
# @Time : 2022/10/6 15:53
# @Author : jiapeng
# @File : Log.py
import logging
import os

logger = logging.getLogger("XX项目UI自动化")
logger.setLevel(logging.DEBUG)
# 创建格式器
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
# 创建控制台处理器
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)
# 添加控制台输出
logger.addHandler(sh)

# 定义日志存放文件路径
logs = os.path.join(os.path.dirname(__file__),'../Log')
if not os.path.exists(logs):
    os.mkdir(logs)
logfile = os.path.join(logs,'Runlog.log')
# 创建文件处理器
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
# 输出到指定文件
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info("this is test")
