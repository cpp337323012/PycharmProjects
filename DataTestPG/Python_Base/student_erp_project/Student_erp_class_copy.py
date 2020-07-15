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
        'name': 'Tom',
        'sex': '男',
        'birthday': '19920920'
    },
    {
        'name':'Jerry',
        'sex':'女',
        'birthday':'19890920'
    },
    {
        'name':'Kitty',
        'sex':'女',
        'birthday':'19800921'
    },
    {
        'name':'Kitty',
        'sex':'女',
        'birthday':'19700921'
    }
]


# 定义Student类

class Student:
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday


    # 获取学生age
    def get_age(self):
        this_year = datetime.now().year
        age = this_year - int(self.birthday[:4])
        return age


# 定义学生操作系统
class Student_System:
    def __init__(self, name):
        self.name = name
        self.data = []


    # 美化输出
    def beauty_print(self, data_list):
        for index, student in enumerate(data_list):
            print(f'序号:{index}', end='\t')
            print(f'名字:{student.name}', end='\t')
            print(f'性别:{student.sex :2}', end='\t')
            print(f'年龄:{student.get_age()}')


     # 数据加载
    def load_data(self):
        for item in student_data:
            student = Student(item['name'], item['sex'], item['birthday'])
            self.data.append(student)


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


    # 启动系统
    def start(self):
        self.load_data()
        while True:
            self.show_menu()
            operation  = input('请选择操作：').strip()
            if operation == '1':
                self.show_all_student()
            if operation == '2':
                self.create_new_student()
            if operation == '3':
                self.find_student()
            if operation == '4':
                self.modify_student()
            if operation == '5':
                self.delete_student()
    # 输入学生名
    def input_name(self):
        while True:
            name = input('请输入学生名称：').strip()
            if name:
                return name
            else:
                continue


    # 选择性别
    def choose_sex(self):
        sex = int(input('1.男 | 2.女')).strip()
        if sex == '1':
            return '男'
        elif sex == '2':
            return '女'
        else:
            return '未知'


    # 通过名字查询学生
    def find_student_by_name(self):
        name = self.input_name()
        find_list = []
        for student in self.data:
            if name.lower() in student.name.lower():
                find_list.append(student)
        if  find_list:
            return find_list
        else:
            print(f'没有找到学生:{name}')

    # 1. 显示所有学生
    def show_all_student(self):
        self.beauty_print(self.data)


    # 2. 新建学生信息
    def create_new_student(self):
        new_name = self.input_name()
        new_sex = self.choose_sex()
        new_bir = input('请输入出生日期：')
        new_student = Student(new_name, new_sex, new_bir)
        self.data.append(new_student)


    # 3.查询学生信息
    def find_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)


    # 4.修改学生信息
    def modify_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('选择要修改学生信息的序号：'))
            modify_student = find_list[index]
            print('当前修改的是:')
            self.beauty_print([modify_student])
            mod_name = input('修改后的额名字：').strip()
            mod_sex = self.choose_sex()
            mod_bir = input('输入修改后的出生日期：')
            if mod_name:
                modify_student.name = mod_name
            modify_student.sex = mod_sex
            modify_student.birthday = mod_bir


    # 5.删除学生信息
    def delete_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('选择删除学生的序号：'))
            print('当前删除的学生是')
            delete_student = find_list[index]
            self.beauty_print([delete_student])
            self.data.remove(delete_student)


if __name__ == '__main__':
    student_sys = Student_System('cp')
    student_sys.start()


'''    
# 3.查询学生信息
    def find_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
添加 if find_list:
            self.beauty_print(find_list)
避免查询姓名结果为空，beauty_print（）报错提示返回结果为空
            '''
