# encoding:utf-8

for i in range(1,10):
    for j in range(1, i+1):
        print(f'{i}*{j}= {i*j}',end='\t')
    print('\n')