# 字符串内建函数
# 查找字符串

s = 'Hello World'.find('H')
print(s)

s1 = 'Hello World'.find('l')
print(s1)  # find()查询返回的是目标字符串的索引位置

# 转化为小写字符
print('Hello World'.lower())
print('Hello World'.upper())

# 字符串长度
print('Hello Python'.__len__()) # 返回的是自然长度

# 判断字符串只包含空格
print('a '.isspace())
print(''.isspace())

# 字符串替换
print('Hello String'.replace('o', '66'))