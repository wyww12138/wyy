"""
@Time : 2021/06/23 9:58
@Auth : xse
"""
import pytest
from wyy_api_frame.common.method import Requests
from wyy_api_frame.utils.read_yaml import Openyaml
obj=Requests()#实例化请求的类

@pytest.mark.parametrize('data',Openyaml().read_list_yaml())
def test_login_1(data):
    # print(data['url'])
    # print(data['body'])
    resp=obj.post(url=data['url'],data=data['body'],headers=data['header'])
    print(resp.json())

if __name__ == '__main__':
    pytest.main(['-vs','test_login.py'])