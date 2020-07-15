'''多态也成为鸭子'''

class Person(object):
    def __init__(self):
        self.name = 'xiaowang'
        self.age = 20

    def eat(self):
        print(f'吃饭{self.name}')

class Dog(object):
    def __init__(self):
        self.name = 'wangcai'
        self.age = 2

    def eat(self):
        print(f'{self.name}坑骨头')

# 函数(object 为使用Person创建出来的对象服务的)
def my_print(object):
    # Python不关心函数(方法)中参数的类型，只要这个参数有这个属性或方法，都可以使用
    print(object.name)
    print(object.age)
    object.eat()

per = Person()
my_print(per)

do = Dog()
my_print(do)


'''多态：定义时的类型和运行时类型不一致，此时就为多态，Python和java、C强类型语言不一样。它崇尚鸭子类型：虽然我想要一个鸭子
，但是传入一个鸟，只要鸟走路像鸭子，叫声像鸭子，游泳也像鸭子，我就认为这就是鸭子'''

# 多态的好处，给函数、方法，增加的扩展性和提高开发效率


class Student(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name}会吃饭')


stu1 = Student('xiaohong')
stu2 = Student('xiaoming')

def stu_print(object):
    print(f'{object.name}实例化对象属性地址:{id(object.name)}')
    print(f'{object.name}实例化对象地址:{id(object)}')
    print(f'{object.name}实例化对象方法地址:{id(object.eat())}')

stu_print(stu1)
stu_print(stu2)

'''对象需要占用地址（和对象属性地址不相同）表达是不同的人
对象属性需要占用地址（和对象的地址不相同）不同人的属性特征是不同的
不同对象但是调用的方法id（地址相同）和（方法相同 因为方法中有一个形参self，可以区分是哪个对象调用）'''