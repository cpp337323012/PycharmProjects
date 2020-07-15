

'''多继承，有多个父类'''

# 自定义一个师傅类（古法）
class Master(object):

    # 构造方法
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    # 擅长做煎饼果子
    def make_cake(self):
        print(f'按照{self.kongfu}烹饪煎饼')



# 自定义一个新东方(现代)
class School(object):

    # 构造方法
    def __init__(self):
        self.kongfu = '现代煎饼果子配方'

    # 擅长做煎饼果子
    def make_cake(self):
        print(f'按照{self.kongfu}烹饪煎饼')



# 自定义一个徒弟类
class Prentice(Master, School):

    # 构造方法
    def __init__(self):
        self.kongfu = '猫式现代煎饼果子工艺'

    '''子类继承父类，子类重写父类方法。
        重写：子类继承父类，做了自己特有的事情'''

    def make_cake(self):
        print(f'按照{self.kongfu}烹饪')

# 定义一个大猫
# 如果子类的方法名(子类已经重写父类的方法）和父类的相同时，默认会使用子类的方法
# 为啥会使用子类属性(kongfu)，子类重写了父类__init__方法
damao = Prentice()
damao.make_cake()


