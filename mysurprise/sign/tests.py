from django.test import TestCase

# Create your tests here.


import pymysql

# 创建链接
conn = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='6666', db='project_mysql', charset='utf8')
# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行sql
cursor.execute("select id,title from class")
class_list = cursor.fetchall()
cursor.close()
conn.close()
print(class_list)