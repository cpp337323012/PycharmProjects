# coding:utf-8
# list(可迭代对象)
import random

name = list(('兰陵王', '东皇', '猴子'))
print(name)
print(type(name))

# 和字符串一样，可以使用索引修改元素
# 字符串是不可变字符类型
print(name[2])

# 一个学校，有三个办公室，有10位老师等待工位的分配，请随机分配
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)  # choice从列表里随机选择一个数据
    room.append(teacher)

print(rooms)

# 第0个房间有三个人，分别是。。。
for i, room in enumerate(rooms):
    print('房间%d里有%d个老师' % (i, len(room)))
    for teacher in room:
        print(teacher, end='\t')
    print()