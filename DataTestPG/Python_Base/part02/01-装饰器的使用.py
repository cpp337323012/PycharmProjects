# coding:utf-8
# 执行之前获取时间，执行结束获取时间
import time


def cal_time(fn):
    print('我是外部函数，被调用了')
    print('fn={}'.format(fn))

    def inner(x, *args, **kwargs):
        start = time.time()
        s = fn(x)
        end = time.time()
        return s, end-start
    return inner


@cal_time  # 第一件事调用cal_time;第二件事把装饰器函数传递给fn
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


# 第三件事；当再次调用demo是，才是的demo函数已不再是上面的demo
print('装饰后的demo={}'.format(demo))
m = demo(100000, 'hello', 'world')
print('m的值是', m)