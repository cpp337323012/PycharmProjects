'''
【学生管理系统】：
1. 显示所有学生信息
2. 新建学生信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息
0. 退出系统

'''
# 所有学生数据
student_data = [
    {
        'id':'17100',
        'name':'Tom',
        'sex':'男',
        'address':'上海'
    },
    {
        'id':'17101',
        'name':'Jerry',
        'sex':'女',
        'address':'北京'
    },
    {
        'id':'17102',
        'name':'Kitty',
        'sex':'女',
        'address':'澳门'
    }
]

# 优化学生信息显示
def beauty_show(data_list):
    for index, student in enumerate(data_list):
        print(f'序号：{index}', end=' ')
        print(f'姓名：{student["name"]}', end=' ')
        print(f'性别：{student["sex"]}', end=' ')
        print(f'地址：{student["address"]}')


# 显示所有学生信息
def show_all():
    beauty_show(student_data)


# 输入名字
def input_name():
    while True:
        name = input('请输入名字：').strip()
        if name:
            return name
        else:
            continue


# 选择性别
def choose_sex():
    while True:
        print('1(男)|2(女)')
        n = input('选择性别：')
        if n == '1':
            return '男'
        elif n == '2':
            return '女'
        else:
            continue


# 新建学生信息
def create_student():
    name = input_name()
    sex = choose_sex()
    address = input('输入地址：')
    student = {
        'name':name,
        'sex': sex,
        'address': address
    }
    student_data.append(student)


# 查询学生信息
def find_student():
    name = input('查询学生姓名：')
    for student in student_data:
        if student['name'] == name:
            print(student)
            return
        else:
            print('无学生数据')
            return


# 修改学生信息
def modify_student():
    name = input('查询学生姓名：')
    for student in student_data:
        if student['name'] == name:
            print(student)
            student['name'] = input('请输入修改名称：')
            student['sex'] = input('请输入修改性别：')
            student['address'] = input('请输入修改地址：')
        else:
            print('无学生数据')
            return


# 删除学生信息
def remove_student():
    name = input('查询学生姓名：')
    for student in student_data:
        if student['name'] == name:
            print(student)
            student_data.remove(student)
            return
        else:
            print('无学生数据')
            return

while True:
    print('''**********
        1. 显示所有学生信息
        2. 新建学生信息
        3. 查询学生信息
        4. 修改学生信息
        5. 删除学生信息
        0. 退出系统 
        **********''')
    op = input('请输入序号：')
    if op == '1':
        print('显示所有学生信息')
        show_all()
    elif op == '2':
        print('新建学生信息')
        create_student()
    elif op == '3':
        print('查询学生信息')
        find_student()
    elif op == '4':
        print('修改学生信息')
        modify_student()
    elif op == '5':
        print('删除学生信息')
        remove_student()
    else:
        print('退出系统')
        break