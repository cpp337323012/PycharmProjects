'''
列表：一组数据
list是有序的序列，每个元素分配索引，从0开始

'''

list1 = ['xiaoming', 12, 'xiaowang']
print(type(list1))
print(list1)

# 列表访问
print(list1[0])
print(list1[:2])

# 更新
list2 = ['xiaoming2', 122, 'xiaowang2']
list2[1] = '14'
print(list2)

# 增加
list2.append('new_add_name')
print(list2)

# 删除
del list2[1]
print(list2)


# 嵌套列表
list3 = ['fristpara', ['second', 'third']]
print(list3[1][0])

# 返回列表元素个数
count3 = len(list3)
print(count3)

# 对列表中元素排序
list4 = [11, 12, 14, 16, 9, 1]
list4.sort()
print(list4)

# 查看列表中第一个匹配元素索引值
list5= [1, 12, 14, 16, 9, 1]
l = list5.index(1)
print(l)

'''
北京地铁一号线，有两个人 A 和 B
过2站，天安门站到了，C上车，B下车
过5站，国贸站到了，D上车， A下车
过2站，四惠站到了，E上车
问：如果地铁停一次，在三个站停靠，车上还有谁
'''

Station = input('请输入站名：')
car_list = ['A', 'B']

if Station == '天安门站':
    car_list.append('C')
    car_list.remove('B')
    print(car_list)
elif Station == '国贸站':
    car_list.append('C')
    car_list.remove('A')
    print(car_list)
elif Station == '四惠站':
    car_list.append('E')
    print(car_list)
else:
    print('只能输入："天安门站"、"国贸站"、"四惠站"')


