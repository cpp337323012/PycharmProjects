'''
for 的优先级高于if

'''
lists = ['2', '3', '4']
for i in lists:
    print(i)
if i < '1':
    print('this is if start')
else:
    print('this is else start')


