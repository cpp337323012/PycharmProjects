# encoding:utf-8
# 9*9乘法表算法
for n in range(1, 10):
    for m in range(1, n+1):
        print(f'{n} * {m} = {n*m}', end=' ')
    print()


lista = [1, 2, 4, 5, 4, 6]
for n in lista:
    if n == 5:
        continue # 结束Y这次魂环，进入到t的循环
    print(n)


'''
在1-100之间产生一个整数
让用户反复猜测
只是提示"大了"和"小了"
猜对游戏结束
'''
import random # 引入随机数模块
# 使用随机数模块生成1-100整数一个
target = random.randint(1, 100)
# 如果猜次数大于5，结束游戏
total = 5 # 可以猜测的次数

count = 0 # 初始化猜测次数
while True:
    n = int(input('请猜一个1-100整数：'))
    if n < target:
        print('猜小了')
    elif n > target:
        print('猜大了')
    else:
        print('猜对了')
        break
    count += 1 # count + 1 = count
    if count > total:
        print(f'你猜了{total}次了')
        break