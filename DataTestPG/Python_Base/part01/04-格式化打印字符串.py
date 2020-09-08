# coding:utf-8
# {}中什么都不写，会读取后面的内容
x = '大家好，我是{},今年{}岁了'.format('张三', 19)
print(x)

# 根据{数字},顺序填入value
x1 = '大家好，我是{1},今年{0}岁了'.format(20, '李四')
print(x1)

# 根据{变量名},顺序填入value
x2 = '大家好，我是{name},今年{age}岁了'.format(age=22, name='王五')
print(x2)

# 使用数据结构列表
lis_info = ['zhangsan', 19, '上海', '180']
x3 = '大家好我是{},今年{}岁了，来自{}, 身高{}cm'.format(*lis_info)
print(x3)

# 使用数据结构字典
dic_info = {'name': '赵六', 'age': 20, 'addr': '北京', 'height': 190}
x4 = '大家好我是{name},今年{age}岁了，来自{addr}, 身高{height}cm'.format(**dic_info)
print(x4)
