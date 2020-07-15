'''只有一个父类'''
class Master(object):
    def __init__(self):
        # 属性
        self.kongfu = '古法煎饼果子'

        # 擅长做煎饼果子
    def make_cake(self):
        print(f'按照{self.kongfu}制作')


# 创造李师傅
lishifu = Master()
print(lishifu.kongfu)
lishifu.make_cake()

# 自定义一个徒弟类，子类继承了父类，就有了父类的方法和属性
# 子类有了父类的属性，是因为子类使用了父类的__init__(对属性赋值的地方)
class Prentice(Master):
    pass

# 自定义一个大猫
damao = Prentice()
print(f'这是大猫的属性{damao.kongfu}')
damao.make_cake()

'''多继承，有多个父类'''

# 自定义一个师傅类（古法）
class Master(object):
    # 构造方法
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    # 擅长做煎饼果子
    def make_cake(self):
        print(f'按照{self.kongfu}烹饪煎饼')

    # 父类不相同的方法
    def dayandai(self):
        print('大烟袋')


# 自定义一个新东方(现代)
class School(object):
    # 构造方法
    def __init__(self):
        self.kongfu = '现代煎饼果子配方'

    # 擅长做煎饼果子
    def make_cake(self):
        print(f'按照{self.kongfu}烹饪煎饼')

    # 父类不相同的方法
    def xiaoyandai(self):
        print('小烟袋')

# 自定义一个徒弟类
class Prentice(Master, School):
    pass

# 定义一个大猫
damao = Prentice()
print(damao.kongfu)
# 如果父类两个方法名相同，子类会指定第一个父类的
damao.make_cake()
# 如果父类的方法名不相同，子类会分别执行
damao.dayandai()
damao.xiaoyandai()


