"""
@Time : 2021/06/23 15:20
@Auth : xse
"""
from wyy_api_frame.databases.select_to_file import Test_select
from wyy_api_frame.common.public import filepath

class User_Write_Read():
    def test_write(self,sql):
       test_sql= Test_select().select_file(sql)
       with open(filepath('config','user_id.test'),'w',encoding='utf-8') as file_w:
           file_w.write(str(test_sql))
    def test_read(self):
       with open(filepath('config','user_id.test'),'r',encoding='utf-8') as file_r:
           return file_r.read()
if __name__ == '__main__':
    test_w_r=User_Write_Read()
    test_w_r.test_write('select max(id) from sys_user')
    print(test_w_r.test_read())
