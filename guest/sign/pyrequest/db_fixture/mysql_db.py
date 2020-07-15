from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/db_config.ini'


cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')

# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
            )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    # 清除表数据
    def clear(self, table_name):
        # real_sql = "truncate table" + table_name + ";"
        real_sql = "delete from" + table_name + ";"

        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()


    # 插入数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INFO" + table_name + "(" + key + ") VALUES (" + value + ")"

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()


    # 关闭数据库连接
    def close(self):
        self.conn.close()


    # 输入插入表
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    table_name = 'sign_event'
    data = {'id':1, 'name':'红米','limit':2000, 'status':1, 'address':'北京会展中心',
            'start_time':'2019-02-21 00:23:29'}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
'''首先，读取db_config.ini文件中的MySQL连接数据配置
   创建DB类，__init__()方法初始化数据库连接，通过connect()连接数据库
   
   因为初始化测试数据只需要清除数据和插入数据，所以只封装了clear()和insert(),其中insert()对插入数据格式化，
   将字典转化为插入SQl语句，极大方便测试数据创建。
   
    最后通过close()关闭数据库连接
    
'''