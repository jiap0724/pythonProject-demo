import unittest
from ddt import ddt,data,unpack,file_data


@ddt
class TestDemoJp(unittest.TestCase):

    @data(['晓明', '23'], ['baby', '24'])
    @unpack
    def test_ddttt(self, username, age):
        print('用户名:%s 年龄:%s' % (username, age))

    @file_data('/Users/jiapeng/Downloads/python-exercises/jiapeng/UItest/jiapengdemo/data.yaml')
    def test_yamldd(self, **kwargs):
        # print('用户名：',kwargs['username'])
        # print('密码：',kwargs['password'])
        result = kwargs['validata']['jieguo']
        for key, values in kwargs['validata'].items():
            print(key, values)
            if values == "登陆成功":
                self.assertEqual('登陆成', values)
                print('成功！')
            else:

                print('失败！！！！')


if __name__ == '__main__':
    unittest.main()
