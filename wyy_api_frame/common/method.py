"""
@Time : 2021/06/22 17:22
@Auth : xse
"""
import requests
class Requests():
    def __init__(self):
        self.session=requests.Session()
    def reques(self,url,method='get',**kwargs):
        if method=='get':
            return self.session.request(url=url,method=method,**kwargs)
        elif method=='post':
            return self.session.request(url=url,method=method,**kwargs)
        elif method=='put':
            return self.session.request(url=url,method=method,**kwargs)
        elif method=='delete':
            return self.session.request(url=url,method=method,**kwargs)
    def get(self,url,**kwargs):
        return self.reques(url=url,**kwargs)
    def post(self,url,**kwargs):
        return self.reques(url=url,method='post',**kwargs)
    def put(self,url,**kwargs):
        return self.reques(url=url,method='delete',**kwargs)