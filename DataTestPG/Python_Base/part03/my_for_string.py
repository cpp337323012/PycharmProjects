'''
格式化输出：format（）
Python3.6 后有f-string格式化输出

'''

# user_1 = '韩金'
# user_2 = '另类'
# print('{}对{}说："你好"'.format(user_1, user_2))
#
# print(f'{user_1}对{user_2}说："你好"')


'''
+ 连接多个字符串
'''
# print('py' + 'th' + 'on')


# price = 100000
# has_good_redit = True
#
# if has_good_redit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment:{down_payment}')

'''while if循环汽车功能'''
# command = ''
# print('You can input ("help"、"quit"、"stop"、"start")')
# while command.lower() != 'quit':
#     command = input('>').lower()
#     if command == 'start':
#         print('Car started ..')
#     elif command == 'stop':
#         print('Car  stopped...')
#     elif command == 'help':
#         print('''
#             start - to start thecar
#             stop - to stop the car
#             quit - to quit
#         ''')
#     elif command == 'quit':
#         break
#     else:
#         print("Sorry l don't understand")


''' 输入1234，回显对应英文'''
# phone = input('Phone:')
# digits_mapping = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'three'
# }
# output = ''
# for ch in phone:
#     output += digits_mapping.get(ch, '!') + ' '
# print(output)


''':emojis表情'''
# message = input(">")
# words = message.split(' ')
# print(words)
# emojis = {
#     ':)': '😀',
#     ':(': '😟'
# }
#
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)


'''Functions（函数）'''
# def greet_user(first_name, last_name):
#     print("Hi there!")
#     print(f'{first_name} {last_name}')
#     print("Welcome aboard")
#
# print("Start")
# greet_user('Lucy', 'Smith')
# print("finished")


'''异常Exception'''
# try:
#     age = int(input('age: '))
#     print(age)
# except ValueError as e:
#     print('Invalid Value')


'''构建一个Person的类，包含talk()的方法以及name属性'''
# class Persion:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"l'm {self.name}, Nice to meet you!")
#
# per = Persion('Lucy')
# per.talk()

'''继承inheritance'''
# class Mamal:
#     def walk(self):
#         print("l can walk")
#
# class Cat(Mamal):
#     def catch_mouse(self):
#         age = '10'
#         print("l good at catch_mouse")
#         return age
#
# black_cat = Cat()
# black_cat.catch_mouse()

'''随机选择一个成员'''
# import random
#
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# member = ['Mary', 'Stone', 'Peter', 'Mosh', 'Bob']
# leader = random.choice(member)
# print(leader)

'''写一个掷骰子的程序，使用Dice类，方法为roll()，每次仍2个骰子，显示结果，格式为tuple'''
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return (first, second)
#
# dice = Dice()
# print(dice.roll())

'''Directories and Files 目录和文件'''
# from pathlib import Path
#
# path = Path()
# for file in path.glob('*.py'):
#     print(file)

# import copy
# lis = [1, 2, ['a', 'b']]
# lis_co = lis.copy() # 浅拷贝
# lis_co_deep = copy.deepcopy(lis) # 深拷贝
#
# print(f'浅拷贝：{lis_co}')
# print(f'深拷贝：{lis_co_deep}')
#
# lis.append(3)
# lis[2].append('E')
#
# print(f'添加元素后原始list：{lis}')
# print(f'添加元素后浅拷贝：{lis_co}')
# print(f'添加元素后深拷贝：{lis_co_deep}')
'''输出'''
'''
浅拷贝：[1, 2, ['a', 'b']]
深拷贝：[1, 2, ['a', 'b']]
添加元素后原始list：[1, 2, ['a', 'b', 'E'], 3]
添加元素后浅拷贝：[1, 2, ['a', 'b', 'E']]    
添加元素后深拷贝：[1, 2, ['a', 'b']]
'''
'''总结：深拷贝和浅拷贝都会拷贝对象的父对象和子对象，如果父对象和子对象均发生变动，
浅拷贝只更新子对象变动，而深拷贝都不更新'''

import os
import glob
# 运行当前目录
# print(os.getcwd())
# # 判断当前目录下是否为文件夹
# for file in os.scandir():
#     print(file.name, file.path, file.is_dir())
# # 发现所有当前目录下所有文件夹及文件
# for dirpath, dirname, filenames in os.walk('./'):
#     print(f'发现文件夹：{dirname}')
#     print(filenames)
# 文件模糊匹配
# print(glob.glob('*.py'))

my_dic = {'name': '小明','age': 12, 'address':'shanghai'}
print(type(my_dic))
print(len(my_dic))
dic1= {}
print(len(dic1))