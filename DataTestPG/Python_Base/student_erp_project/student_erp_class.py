# encoding:utf-8
'''
【学生管理系统】：
1. 显示所有学生信息
2. 新建学生信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息
0. 退出系统

'''
from datetime import datetime

# 所有学生数据
student_data = [
    {
        'name':'Tom',
        'sex':'男',
        'birthday':'19920920'
    },
    {
        'name':'Jerry',
        'sex':'女',
        'birthday':'19900920'
    },
    {
        'name':'Kitty',
        'sex':'女',
        'birthday':'19900921'
    },
    {
        'name':'Kitty',
        'sex':'女',
        'birthday':'19800921'
    }
]


# 学生类
class Student:
    # 学生初始化
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday


    # 获取学生年龄
    def get_age(self):
        this_year = datetime.now().year
        age = this_year - int(self.birthday[:4])
        return age
'''学生类需要处理的功能：
1.声明该类的属性
2.通过datetime（）处理得到age
'''

# 学生管理系统类
class Student_System:
    # 初始化
    def __init__(self, name):
        self.name = name
        self.data = []


    # 美化输出打印
    def beauty_print(self, data_list):
        for index, student in enumerate(data_list):
            print(f'序号：{index}', end='\t')
            print(f'姓名：{student.name}', end='\t')
            print(f'性别：{student.sex:2}', end='\t')
            print(f'年龄：{student.get_age()}')


    # 加载学生数据
    def load_data(self):
        for item in student_data:
            student = Student(item['name'], item['sex'], item['birthday'])
            self.data.append(student)


    # 启动学生管理系统
    def start(self):
        # 在系统启时，加载数据
        self.load_data()
        while True:
            self.show_menu()
            operation = input('选择操作：')
            if operation == '1':
                self.show_all_student()
            elif operation == '2':
                self.create_student()
            elif operation == '3':
                self.find_student()
            elif operation == '4':
                self.modify_student()
            elif operation == '5':
                self.remove_student()
            elif operation == '0':
                print('退出程序')
                break
            else:
                print('请输入正常的操作！')


    #输入学生名
    def input_name(self):
        while True:
            name = input('请输入名字：').strip()
            if name:
                return name
            else:
                continue


    # 选择性别
    def choose_sex(self):
        sex = input('选择性别：(1. 男|2. 女)').strip()
        if sex == '1':
            return '男'
        elif sex == '2':
            return '女'
        else:
            return '未知'


    # 根据名字查找学生
    def find_student_by_name(self):
        name = self.input_name()
        find_list = []
        for student in self.data:
            if name.lower() in student.name.lower():
                find_list.append(student)
        if find_list:
            return find_list
        else:
             print(f'没有找到学生:{name}')


    # 显示菜单
    def show_menu(self):
        # f-string
        print(f'''**********
                欢迎{self.name}
                1. 显示所有学生信息
                2. 新建学生信息
                3. 查询学生信息
                4. 修改学生信息
                5. 删除学生信息
                0. 退出系统 
                **********''')


    # 1.显示所有学生信息
    def show_all_student(self):
             self.beauty_print(self.data)


    # 2.新建学生信息
    def create_student(self):
        name = self.input_name()
        sex = self.choose_sex()
        birthday = input('输入出生日期：')
        student = Student(name, sex, birthday)
        self.data.append(student)


    # 3.查询学生信息
    def find_student(self):
        find_list = self.find_student_by_name()
        self.beauty_print(find_list)


    # 4.修改学生信息
    def modify_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('选择修改的序号：'))
            student = find_list[index]
            print('当前修改的是：')
            self.beauty_print([student])
            name = input('输入修改后的名字：').strip()
            sex = self.choose_sex()
            birthday = input('输入修改后的出生日期：')
            if name:
                student.name = name
            student.sex = sex
            student.birthday = birthday


    # 5.删除学生
    def remove_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('选择删除学生的序号：'))
            print('当前删除的学生是：')
            student = find_list[index]
            self.beauty_print([student])
            self.data.remove(student)


if __name__ == '__main__':
        # 当这个py文件有__name__属性，被执行而不是被导入的时候，会执行main方法
        student_sys = Student_System('曹鹏的学生管理系统')
        student_sys.start()