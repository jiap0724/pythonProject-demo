import requests
import json
import unittest
import random
from ddt import ddt, data, unpack,file_data




@ddt
class ApiDemo(unittest.TestCase):
    @unittest.skip
    def test_query(self):
        url='https://zzkfapi.zhuanspirit.com/api/kfim/through/getSubConversations'
        data={
            'pageNum': '1',
            'pageSize': '20',
            'conversationId': 'CONV_455251430264578944_1638777987352',
            'kefuRealName':'',
                'skillCode':'',
        'athenaChannelId': '24',
        'startTime': '1638288000000',
        'endTime': '1638806400000',
        'startLineTime':'',
        'endLineTime':''
        }
        header={
            'cookie':'t_sso_code=Y8b1EBSXn0Qc91PBrfFuecbY_NPwaUTKaimbHHL8cIk; sso_uid=qy01706069c786b20728a50c428b; sso_company_code=0; aid=2950422220238007202; ln=jiapeng03; un=%E8%B4%BE%E9%B9%8F; kid=2929170973383049403; sso_code=VIoppzT5QBDkikfKmxTQdNXykErlUV7CnoGkfO-hlDo; gsso_uid=jiapeng03; ginfo=%7B%22realName%22%3A%22%E8%B4%BE%E9%B9%8F%22%2C%22img%22%3A%22%22%2C%22orgName%22%3A%22%22%2C%22userId%22%3A51350373756421%2C%22orgId%22%3A%22%22%2C%22username%22%3A%22jiapeng03%22%7D; zzsctoken=yXCblDZLWobHcEdppWjycHQTIqswFMvQurIKGcrdPIlbUQigPdmDkjJvBzEXkgew; ticket=ln%3Djiapeng03%26s%3D446e1de15f5bb2c15f6beef563e316728013de55%26v%3D1%26kid%3D2929170973383049403%26seq%3D1%26et%3D1638790762582'
        }
        r=requests.post(url,data,verify=False,headers=header)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))

    @unittest.skip
    def test_qonedata(self):

        import json
        # filename = 'C:\\Users\\Administrator\\PycharmProjects\\python-exercises\\jiapeng\\task1\\City_json.json'
        filename='C:\\Users\\Administrator\\PycharmProjects\\python-exercises\\jiapeng\\task1\\city.json'
        with open(filename, 'r', encoding='utf-8') as file:
            china_data = json.load(file)
            # print(len(china_data))
            # print(china_data[1]['childs'][0]['childs'][0]['standardLocationName'])
            for i in range(len(china_data)):
                # print(i)
                sheng=china_data[i]['standardLocationName']
                # print(sheng)
                for j in range(len(china_data[i]['childs'])):
                    shi=china_data[i]['childs'][j]['standardLocationName']
                    # print(shi)
                    for k in range(len(china_data[i]['childs'][j]['childs'])):
                        qu=china_data[i]['childs'][j]['childs'][k]['standardLocationName']
                        # print(qu)
                        mingcheng=qu
                        print(mingcheng)

                        # print(qu)

    @unittest.skip
    def test_config(self):
        list=[{'2022-01-13 21:00:00','广东省深圳市福田区'},{'2022-01-13 10:00:00','北京市北京市海淀区'}]
        # print(len(list))
        # num=random.randint(0,1)
        # print(num)

        # print(list[1])
        for i in range(1858):
            # print(i)
            # num = random.randint(0, 1)
            # print(list[num])
            print(list[1])

    @unittest.skip
    def test_readdata(self):
        filename = 'C:\\Users\\Administrator\\PycharmProjects\\python-exercises\\jiapeng\\task1\\chengshi.Log'
        with open(filename, 'r', encoding='utf-8') as file:
            list1=file.read().split()
            # print(type(list1))
            for i in range(500):
                num=random.randint(0,len(list1))
                mingcheng=list1[num]
                print(mingcheng)
        #         print('1')
        #         print(mingcheng[0:mingcheng.rfind("省")+1])
        #         print(mingcheng[0:mingcheng.rfind("市")+1])

        # filename = 'C:\\Users\\Administrator\\PycharmProjects\\python-exercises\\jiapeng\\task1\\city.json'
        # with open(filename, 'r', encoding='utf-8') as file:
        #     china_data = json.load(file)
        #     for i in range(500):
        #         for j in range(len(china_data)):
        #             # print(i)
        #             sheng = china_data[j]['standardLocationName']
        #         num=random.randint(0,)

    citylist=['北京','上海','广州','深圳']
    @data(*citylist)
    def test_apiTest(self,citylist):
        url='http://wthrcdn.etouch.cn/weather_mini?city='+str(citylist)
        r=requests.get(url)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))

    userinfo=(['晓明','23'],['baby','24'])
    @data(['晓明','23'],['baby','24'])
    @unpack
    def test_ddttt(self,username,age):
        print('用户名:%s 年龄:%s'%(username,age))

    @file_data('/Users/jiapeng/Downloads/python-exercises/jiapeng/UItest/jiapengdemo/data.yaml')
    def test_yamldd(self,**kwargs):
        # print('用户名：',kwargs['username'])
        # print('密码：',kwargs['password'])
        result=kwargs['validata']['jieguo']
        for key,values in kwargs['validata'].items():
            print(key,values)
            if values=="登陆成功":
                self.assertEqual('登陆成',values)
                print('成功！')
            else:

                print('失败！！！！')


if __name__ == '__main__':
    # unittest.main()
    # 加载测试用例
    # suite=unittest.defaultTestLoader.discover('./task3',pattern='queryApi.py')
    suite=unittest.TestSuite
    loader=unittest.TestLoader
    suite.addTest(ApiDemo("test_yamldd"))

    #生成html测试报告
    # files=open('index.html','wb')
    # Runner=HTMLTestRunner(stream=files, verbosity=1,title='贾鹏测试demo',description=None,tester="贾鹏")
    # Runner.run(suite)
    # unittest.main(defaultTest=suite)



























