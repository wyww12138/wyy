"""
@Time : 2021/06/22 17:47
@Auth : xse
"""
import xlrd
from wyy_api_frame.common.public import filepath
from wyy_api_frame.utils.read_yaml import Openyaml
class ReadExcel():
    def __init__(self):
        self.id=0
        self.describe=1
        self.url=2
        self.method=3
        self.params=4
        self.expect=5
        self.open_1=Openyaml()
    def get_sheet(self):
        book=xlrd.open_workbook(filepath('data','Data.xlsx'))
        return book.sheet_by_index(0)
    # 获取单元格
    def get_value(self,rows,cols):
        return self.get_sheet().cell_value(rows,cols)
    def get_caseid(self,row):
        return self.get_value(row,self.id)
    #获取url
    def get_url(self,row):
        return self.get_value(row,self.url)
    # 获取请求方法
    def get_method(self,row):
        return self.get_value(row,self.method)
    # 获取请求体对应的标签
    def get_data(self,row):
        return self.get_value(row,self.params)

    #通过read_dict_yaml方法获取接口的参数
    #通过get_data方法找到对应接口的标签，然后作为键取对应的值
    def get_body(self,row):
        return self.open_1.read_dict_yaml(f'config','data.yaml')[self.get_data(row)]
    # 获取期望结果
    def get_expect(self,row):
        return self.get_value(row,self.expect)

if __name__ == '__main__':
    readexcel=ReadExcel()
    # print(readexcel.get_url(1))
    print(readexcel.get_body(1))