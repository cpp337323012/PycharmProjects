# 返回一个函数

def my_calc_return (x):
    if x == 2:
        def calc(y):
            return y * y
    if x == 3:
        def calc(y):
            return y * y * y
    return calc   # 使用calc()return失败：TypeError: calc() missing 1 required positional argument: 'y'

mcalc = my_calc_return(3)
print(mcalc(3))


'''
递归：函数中自己调用自己
    重点：要明确递归结束的条件
    优点：写法简单
    缺点：效率低
    要求：运算量每次递归逐渐减小
    逻辑：每一次运算结果是，下一次运算的条件
'''
# def myfunction(x):
#     print(x)
#     myfunction(x+1)
#
# myfunction(1)
# 执行结果：RecursionError: maximum recursion depth exceeded while calling a Python object

'''
阶乘计算，5的阶乘 5 * 4 * 3 * 2 * 1
'''

def f(x):
    if x == 1:
        return 1
    print('计算' + str(x) + '*' + str(x-1))
    return x * f(x-1)
print(f(5))