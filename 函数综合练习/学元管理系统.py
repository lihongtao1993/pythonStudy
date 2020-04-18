# 需求分析
"""进入系统选择需要操作的功能，执行相应的功能"""

def student_info_system():
    print("*"*20)
    print("1、添加学员")
    print("2、删除学员")
    print("3、修改学员信心")
    print("4、查询学员信息")
    print("5、显示所有学员信息")
    print("6、退出系统")
    print("*"*20)


student_list = []       # 定义一个列表，存储学员信息

# 定义一个添加学员的函数


def stu_add():                              # 新增学员函数
    student_dict = {}
    student_dict['Name'] = input("请输入姓名：")
    student_dict['Id'] = input("请输入学号：")
    student_dict['Tel'] = input("请输入手机号码：")
    global student_list
    for i in student_list:
        if student_dict["Id"] == i["Id"]:
            print("学号已经存在")
            return
    student_list.append(student_dict)


def stu_del():                             #删除学员函数
    id = input("请输入要删除学员的学号：")
    for i in student_list:
        if id == i["Id"]:
            student_list.remove(i)
            break
    else:
#for ……else…… else后面是for正常结束后执行的代码
        print("学号不存在！")


def update_stu():                           #修改学员函数
    id = input("请输入需要修改的学员学号:")
    for i in student_list:
        if id == i["Id"]:
            i["Name"] = input("请输入新的姓名：")
            i["Tel"] = input("请输入新的手机号码")
            break
    else:
        print("学员不存在！！！！1")

def search_stu():
    id = input("请输入需要查找的学员学号：")
    for i in student_list:
        if id == i["Id"]:
            print(i)
            break
    else:
        print("学员不存在！！！")


while True:
    student_info_system()
    a = int(input("请选择所需要的操作："))
    if a == 1:
        # print("删除学员")
        stu_add()
        print(student_list)
    elif a == 2:
        stu_del()
        print(student_list)
    elif a == 3:
        # print("修改")
        update_stu()
        print(student_list)
    elif a == 4:
        # print("查询")
        search_stu()
        print(student_list)
    elif a == 5:
        print("查所有")
    elif a == 6:
        print("退出系统")
    else:
        print("请输入正确的序号")