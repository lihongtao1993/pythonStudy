# 提供调用函数
# 1、菜单函数


def menu_list():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1、添加名片")
    print("2、显示全部")
    print("3、查询名片", end="\n\n")
    print("0、退出系统")
    print("*" * 50)


card_list = [{"name": "mike", "telephone": "999", "email": "mike@123.com"}]


# 添加名片函数
def card_add():
    card_dict = {"name": input("请输入姓名："),
                 "telephone": input("请输入电话："),
                 "email": input("请输入邮箱：")
                 }
    card_list.append(card_dict)


# 显示全部函数
def card_showAll():
    if len(card_list) == 0:
        print("当前系统没有名片信息!")
    else:
        print("姓名         电话        邮箱")
        for dic in card_list:
            print(dic["name"], end="        ")
            print(dic["telephone"], end="        ")
            print(dic["email"], end="        ")
            print("")


# 查询名片
def card_search():
    searchName = input("请输入要查询的姓名：")
    for dic in card_list:
        if dic["name"] == searchName:
            # print("姓名         电话        邮箱")
            # print(dic["name"], end="        ")
            # print(dic["telephone"], end="        ")
            # print(dic["email"], end="        ")
            # print("")
            print(dic)
            actionCode = input("1、修改名片  2、删除名片")
            if actionCode == "1":
                # name = input("请输入姓名：")
                # if name != "":
                #     dic["name"] = name
                # else:
                #     dic["name"] = dic["name"]
                # telephone = input("请输入电话：")
                # if telephone != "":
                #     dic["telephone"] = telephone
                # else:
                #     dic["telephone"] = dic["telephone"]
                # email = input("请输入邮箱：")
                # if email != "":
                #     dic["email"] = email
                # else:
                #     dic["email"] = dic["email"]
                dic["name"] = change_card(dic["name"], "请输入姓名：")
                dic["telephone"] = change_card(dic["telephone"], "请输入电话：")
                dic["email"] = change_card(dic["email"], "请输入邮箱：")
            elif actionCode == "2":
                card_list.remove(dic)
                print("删除成功！")
            else:
                print("输入错误!")
            break
    else:
        print("查无此人")


def change_card(origin, tip):
    newInformation = input(tip)
    if newInformation == "":
        return origin
    else:
        return newInformation
