'''该项目实现调用orm对象操作数据库增删改查
'''
import pymysql
#
# database = pymysql.connect('127.0.0.1', 'root', '6666', 'project_mysql', charset='utf8')
# # 服务器地址、用户名、密码、数据库名、字符集格式
# cursor = database.cursor()
# 初始化指针

# 新增
# 格式："INSERT INTO 表名 （字段1， 字段2）VALUES（内容1，内容2）;"
# sql = "INSERT INTO auto_goods (date, company, province, price, weight)" \
#       "VALUES ('2020-4-20', '南京粮油有限公司', '南京', '2210', '45.1');"
# cursor.execute(sql)

'''改
格式："UPDATE 表名 SET 字段1 = 内容1 WHERE = 条件1"
'''
# sql = "UPDATE auto_goods SET date = '2019-04-20' WHERE ID = 13;"
# cursor.execute(sql)
# database.commit() # 对数据修改后，需要提交commit
# database.close()

'''查询
格式"select 字段 from 表名 where 条件1"
'''
# sql = "select company,sum(weight) from auto_goods where date = '2018-08-01' group by company;"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

'''删除
格式"delete from 表名 where 条件1"'''

# sql = "delete from auto_goods where id =13;"
# cursor.execute(sql)
# database.commit()
# database.close()

'''向Excel增量插入'''
# import openpyxl
# workbook = openpyxl.load_workbook('入库表1月份.xlsx')
# sheet0 = workbook['Sheet1']
# sheet0['B6'] = '广州第一建筑有限公司'
# workbook.save('入库表1月份.xlsx')