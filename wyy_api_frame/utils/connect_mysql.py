"""
@Time : 2021/06/23 14:16
@Auth : xse
"""
import pymysql
from wyy_api_frame.utils.read_yaml import Openyaml

class Test_mysql():
    def __init__(self,host,user,password,db,port):
        try:
            self.db=pymysql.connect(host=host,user=user, password=password, db=db, port=port)
            self.cursor=self.db.cursor()
        except Exception as e:
            print('连接异常',e)

    def select_sql(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print('查询异常',e)
        finally:
            self.cursor.close()
            self.db.close()

if __name__ == '__main__':
    test_mysql=Test_mysql('192.168.31.220','root','123456','test_cms',3306)
    print(test_mysql.select_sql('select count(id) from sys_user'))