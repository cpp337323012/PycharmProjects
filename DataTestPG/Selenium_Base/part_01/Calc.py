# coding:utf-8
class Calc(object):

    def add(self, x, y, *d):
        # 加法计算
        result = x + y
        for i in d :
            result += i
        return result

    def sub(self, x, y, *d):
        # 减法计算
        result = x - y
        for i in d:
            result -= i
        return result

    @classmethod
    def mul(cls, x, y, *d):
        # 乘法计算
        result = x * y
        for i in d:
            result *= i
        return result

    @staticmethod
    def div(x, y, *d):
        # 除法计算
        if y != 0:
            result = x/y
        else:
            return -1
        for i in d:
            if i != 0:
                result /= i
            else:
                return -1
        return result
