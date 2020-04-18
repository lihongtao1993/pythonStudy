# # 定义一个列表
import random
# name_list = ["zhangsan", "lisa", "wangwu"]
#
#
# # 取数组的值
#
# print(name_list[1])
#
# # 取索引值
#
# print(name_list.index("wangwu"))
#
#
# # 修改数组的值,只需要对相应的数组进行重新赋值即可
#
#
# name_list[0] = "mike"
#
# # 增加数组
#
# # 1、append方法，在列表末尾增加一个数据
#
# name_list.append("James")
# print(name_list)
#
# # 2、insert方法,在列表指定的索引位置插入一个数据
# name_list.insert(1, "jane")
# print(name_list)
#
# # 3、extend方法，将其他列表的内容增加的当前列表的末尾
# name_list2 = ["sun", "zhu"]
# name_list.extend(name_list2)
# print(name_list)
#
#
# # 删除数组数据
# # remove方法，删除指定的数据,删除列表中第一次出现的数据
# name_list.remove("lisa")
# print(name_list)
# # pop方法，删除指定索引值指向的数据,默认最后一个
# name_list.pop()
# print(name_list)
#
# # del方法删除,不建议使用，delete是将变量从内存中删除
# del name_list[2]
# print(name_list)
#
# # 统计数组长度的函数len()
# print(len(name_list))
# # 统计列表中某个元素出现的次数
# print(name_list.count("jane"))
#
# # clear方法，清空列表
# name_list.clear()
# print(name_list)
#
#
# # 列表排序
# # 升序：.sort     降序 .sort(revers)
# Name_list = ["wangxiaoer","wangwu","ahui","huangchao"]
# Name_list.sort()
# print(Name_list)
# Name_list.sort(reverse=True)
# print(Name_list)
#
# number = [12, 2, 34, 38, 22, 13, 45, 23]
#
# number.sort(reverse=False)
#
# print(number)
#
#
# for name in Name_list:
#     print("名字是%s" %name)


teacher_name = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[], [], []]

# i = 0
# while i < len(teacher_name):
#     offices[random.randint(0, 2)].append(teacher_name[i])
#     i += 1
#
# print(offices)

# for teacher in  teacher_name:
#     office_num = random.randint(0, 2)
#     office_len = len(offices[office_num])
#     if office_len >=3:
#         continue
#     offices[office_num].append(teacher )
#
# print(offices)




#随机分配，每个办公室最多3个

x = 0
while x < 8: # 这里的8是数组最开始的长度
    j = x // 3 # 每隔3个换一个办公室+1
    i = random.randint(0, len(teacher_name)-1) #从剩余的老师中随机取一个
    offices[j].append(teacher_name[i])
    teacher_name.pop(i) #删除已经选中的老师
    # print(teacher_name)
    x += 1

print(offices)

