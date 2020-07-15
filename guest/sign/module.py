# coding:utf-8

'''
这是一个简单地计算器，用于计算加、减、乘除
'''

class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
    # 加法运算
    def add(self):
        return self.a + self.b

    # 减法运算
    def sub(self):
        return self.a - self.b

    # 乘法运算
    def mul(self):
        return self.a * self.b

    # 除法运算
    def div(self):
        return self.a / self.b
