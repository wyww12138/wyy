"""
@Time : 2021/06/23 14:42
@Auth : xse
"""
from wyy_api_frame.utils.connect_mysql import Test_mysql
from wyy_api_frame.utils.read_yaml import Openyaml

class Test_select():
    def select_file(self,sql):
        openyaml=Openyaml()
        dict_db=openyaml.read_dict_yaml('config','mysql_login_data.yaml')
        test_mysql=Test_mysql(host=dict_db['host'],user=dict_db['user'],password=dict_db['password'],
                              db=dict_db['db'],port=dict_db['port'])
        return test_mysql.select_sql(sql)[0][0]
if __name__ == '__main__':
    test_select=Test_select()
    print(test_select.select_file('select * from sys_user'))