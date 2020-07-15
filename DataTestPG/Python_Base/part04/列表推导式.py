'''定义一个列表添加1-100个数字'''
my_list = []
for i in range(1, 101):
    my_list.append(i)

print(my_list)


my_list = [i for i in range(1, 101)]
print(f'列表推导式,快速创建列表：{my_list}')

my_list = [i for i in range(1, 101, 2)]
print(f'列表推导式,快速创建列表为奇数：{my_list}')

'''创建1-100偶数列表'''
new_list = []
for i in range(1, 101):
    if i % 2 == 0:
        new_list.append(i)
print(new_list)


my_list = [i for i in range(1, 101) if i % 2 == 0]
print(f'列表推导式,快速创建列表为偶数：{my_list}')