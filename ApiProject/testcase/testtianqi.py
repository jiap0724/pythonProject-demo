# -*- coding:utf-8 -*-
# @Time : 2022/7/25 21:45
# @Author : jiapeng
# @File : testtianqi.py
import json
import unittest

import requests


class TestTianQi(unittest.TestCase):
    def test_query_tianqi(self):
        url='http://wthrcdn.etouch.cn/weather_mini?city=北京'
        r = requests.get(url)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_query_tianqi1(self):
        url='http://wthrcdn.etouch.cn/weather_mini?city=北京'
        r = requests.get(url)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
