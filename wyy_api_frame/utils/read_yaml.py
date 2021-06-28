"""
@Time : 2021/06/23 9:53
@Auth : xse
"""
import yaml
from wyy_api_frame.common.public import filepath

class Openyaml():
    #读取yaml文件为列表格式
    def read_list_yaml(self):
        with open(filepath('data','login.yaml'),'r') as file_r:
            return list(yaml.safe_load_all(file_r))
    def read_dict_yaml(self,filedir,filename):
        with open(filepath(filedir,filename),'r') as file_r:
            return yaml.safe_load(file_r)
if __name__ == '__main__':
    openyaml=Openyaml()
    print(openyaml.read_list_yaml())
    print(openyaml.read_dict_yaml('config','data.yaml'))