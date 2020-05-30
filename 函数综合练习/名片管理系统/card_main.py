# from 函数综合练习.名片管理系统 import card_tools
# 下面这种引用方式需要将目标文件所在文件夹标记为源文件
import card_tools

# 函数入口
while True:
    # print("菜单")
    card_tools.menu_list()
    action_str = input("请选择使用的功能：")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_tools.card_add()
        elif action_str == "2":
            card_tools.card_showAll()
        else:
            card_tools.card_search()
    elif action_str == "0":
        break
    else:
        print("输入错误")
