'''带有参数的__init__()'''

# 定义一个老师类
class Teacher(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 添加属性并赋值


# 创建学生有学号、年龄、名字
class Student(object):

    def __init__(self, name, age, no):
        self.no = no
        # 子类重写了父类同名方法，然后调用父类同名方法
        Teacher.__init__(self, name, age) # 01



xm = Student()