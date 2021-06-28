# -*- coding: utf-8 -*-
"""
@Time : 2021/06/23 11:11
@Auth : xse
"""
import pytest,json
from wyy_api_frame.common.method import Requests#导入接口请求方法
from wyy_api_frame.utils.read_yaml import Openyaml#导入读取yaml文件
from wyy_api_frame.utils.read_execl import ReadExcel#导入读取excel文件
from wyy_api_frame.common.file_write_read import User_Write_Read
from wyy_api_frame.utils.logger import trace_log
obj=Requests()
openexcel=ReadExcel()
test_w_r=User_Write_Read()

class Test_cms():
    @trace_log
    def test_login(self):
        resp=obj.post(url=openexcel.get_url(1),data=openexcel.get_body(1))
        print(resp.json())
        assert resp.json()['msg']==json.loads(openexcel.get_expect(1))['msg']
        return resp.json()

    # @pytest.mark.skip
    @trace_log
    def test_useradd(self):
        resp=obj.post(url=openexcel.get_url(2),data=openexcel.get_body(2))
        test_w_r.test_write('select max(id) from sys_user')
        return resp.json()

    # @pytest.mark.skip
    @trace_log
    def test_usercheck(self):
        resp = obj.post(url=openexcel.get_url(3), data=openexcel.get_body(3))
        print(resp.json()['model']['userList'][0]['userName'])
        return resp.json()
        # print(json.dumps(resp.json()))
        # global user_id
        # user_id=resp.json()['model']['userList'][0]['id']
        # self.user_name = resp.json()['model']['userList'][0]['userName']

    # @pytest.mark.skip
    @trace_log
    def test_userdelete(self):
        data={'ids':test_w_r.test_read()}
        resp = obj.post(url=openexcel.get_url(4), data=data)
        assert resp.json()['msg']==json.loads(openexcel.get_expect(4))['msg']
        return resp.json()

if __name__ == '__main__':

    pytest.main(['-vs','test_001.py','--alluredir','../report/result'])
    import subprocess
    subprocess.call('allure generate ../'
                    'report/result/ -o ../report/html --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8881 ../report/html',shell=True)

    # pytest.main(['-vs', 'test_001.py'])
