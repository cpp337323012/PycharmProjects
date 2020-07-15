# 定义师傅类-古法
class Master(object):

    # 方法
    def make_cake(self):
        print('古法煎饼果子')


# 自定义师傅类-现代
class School(object):

    # 方法
    def make_cake(self):
        print('现代煎饼果子')


# 自定义徒弟类
class Prentice(Master, School):

    # 方法
    def make_cake(self):
        print('猫式煎饼果子')

    # 古法
    def make_old_cake(self):
        # 如果子类重写了父类已有的方法
        # 但是子类还想用父类同名的方法
        # 解决方法：父类名.对象方法名（self）
        Master.make_cake(self)
        '''方式二：新式类使用super (子类类名， self).父类方法名（）'''
        super(Prentice, self).make_cake()
    # 现代
    def make_new_cake(self):
        School.make_cake(self)


damao = Prentice()
damao.make_cake()

# 古法
damao.make_old_cake()
# 现代
damao.make_new_cake()