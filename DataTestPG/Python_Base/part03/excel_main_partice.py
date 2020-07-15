#encoding:utf-8
'''
工作簿下有多个工作表，每个工作表下有多个单元格
'''
import xlrd
import xlwt
# 打开Excel对象文件
xlsx = xlrd.open_workbook('入库表1月份.xlsx')
# 选择Excel工作表，方法1：通过标签索引找到
table = xlsx.sheet_by_index(0)
# 选择Excel工作表，方法2：通过工作表name找到
# table = xlsx.sheet_by_name('sheet1')
# 输出单元格的值
print(table.cell_value(3, 1))
print(table.cell(3, 1).value)
print(table.row(3)[1].value)

'''
新建工作簿
'''
new_workbook = xlwt.Workbook()
work_sheet = new_workbook.add_sheet('new_sheet')
work_sheet.write(0, 0, 'test')
new_workbook.save('入库表2月份.xlsx')
