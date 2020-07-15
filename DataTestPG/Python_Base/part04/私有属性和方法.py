# class Master(object):
#
#     # 构造方法
#     def __init__(self):
#         self.kongfu = '古法煎饼'
#         self.__money = '1000'
#
#     # 制作煎饼
#     def make_cake(self):
#         print(f'{self.kongfu}制作')
#         # 在类内部使用
#         print(self.__money)
#
# # 自定义一个对象
# lishifu = Master()
# # 如果一个属性私有后，不能使用对象调用这个属性（类外使用）
# # print(lishifu.__money)
# lishifu.make_cake()
#
#
#
# '''修改私有属性的值'''
#
# class Person(object):
#
#     def __init__(self):
#         self.__name = 'xiaoming'
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
# per = Person()
# print(f'私有化初始值:{per.get_name()}')
# per.set_name('xiaowang')
# print(f'私有化修改后的值:{per.get_name()}')

