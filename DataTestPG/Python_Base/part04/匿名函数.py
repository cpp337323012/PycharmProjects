# 定义一个列表
my_lis = [1, 3.14, "hello", True]
# 拆包
num, pi, my_str, my_bool = my_lis
print(pi)
print(my_bool)

# num1, pi1, my_str1 = my_lis
# print(num1)
# print(my_str1)

# 定义一个元祖
my_tuple = (1, 3.15, "world")
num2, pi2, my_str3 = my_tuple
print(pi2)

# 定义一个字典
my_dic = {"name":"Tom", "age":"19"}
person_name, person_age = my_dic
print(person_age, person_name)

# 一次定义多个变量
num1 = 10
num2 = 20
num3 = 30
num4 = 3.14
num1, num2, num3, num4 = 10, 20, 39, 3.14
print(num4)

# 龟叔称之为 pythonic 自夸

# 匿名函数，有入参和无返回值
def my_name(name):
    print(f'你好{name}')

f = lambda name : print(f'你好{name}')
f('龟叔')

# 匿名函数，有入参有返回值
def add2num(a, b):
    return a + b

f = lambda a, b : a + b
print(f(1, 3))


'''
列表按照年龄排序
'''
stus = [{'name': 'zhangsan', 'age': 14}, {'name': 'lisi', 'age': 19}, {'name': 'wangwu', 'age': 9}]
print(f'年龄没排序前：{stus}')
stus.sort(key=lambda my_dict: my_dict['age'])
print(f'年龄排序后：{stus}')

stus.sort(key=lambda my_dict: my_dict['name'])
print(f'名字排序：{stus}')


'''按照列表最后一个元素排序'''
my_list = [[10,9,11], [7,10,19], [9, 10, 29]]
my_list.sort(key=lambda new_list: new_list[2])
print(f'排序后的列表{my_list}')