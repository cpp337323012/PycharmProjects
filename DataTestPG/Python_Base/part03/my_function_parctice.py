# 定义一个人类，实例化对象调用类方法

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self, message):
#         print(f'{self.name}说：{message}')
#
# zhangsan = Person('张三', '2')
# zhangsan.say('您好')


'''
装饰器基于闭包的基础，一般用于判断用户登录状态
特点：1. 函数作为参数
     2. 闭包的特点
'''
# 定义一个装饰器

def decorate(func):
    a = 100
    print('wrapper外层打印')

    def wrapper():
        print('------刷漆')
        print('------装地板', a)

    print('wrapper内层打印')

    return wrapper

# 使用定义装饰器
@decorate
def house():
    print('我是清水房---')

# 调用函数house
house()
print(house)
'''
1.house被装饰函数，
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house
'''

# 定义一个变量记录行数
x = 1
while x <= 9:

    y = 1
    while y <= x:
        print(f'{x} * {y} = {x*y}', end='\t')
        y += 1

    x += 1
