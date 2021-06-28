"""
@Time : 2021/06/22 17:35
@Auth : xse
"""
import os
# print(os.path.dirname(__file__))#获取当前路径
base_path=os.path.dirname(os.path.dirname(__file__))#获取当前路径的父级路径

def filepath(filedir='data',filename='data.xlsx'):
    return os.path.join(base_path,filedir,filename)
if __name__ == '__main__':
    print(filepath())