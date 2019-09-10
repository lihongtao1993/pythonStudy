# 定义一个列表

name_list = ["zhangsan", "lisa", "wangwu"]


# 取数组的值

print(name_list[1])

# 取索引值

print(name_list.index("wangwu"))


# 修改数组的值,只需要对相应的数组进行重新赋值即可


name_list[0] = "mike"

# 增加数组

# 1、append方法，在列表末尾增加一个数据

name_list.append("James")
print(name_list)

# 2、insert方法,在列表指定的索引位置插入一个数据
name_list.insert(1, "jane")
print(name_list)

# 3、extend方法，将其他列表的内容增加的当前列表的末尾
name_list2 = ["sun", "zhu"]
name_list.extend(name_list2)
print(name_list)


# 删除数组数据
# remove方法，删除指定的数据,删除列表中第一次出现的数据
name_list.remove("lisa")
print(name_list)
# pop方法，删除指定索引值指向的数据,默认最后一个
name_list.pop()
print(name_list)

# del方法删除,不建议使用，delete是将变量从内存中删除
del name_list[2]
print(name_list)

# 统计数组长度的函数len()
print(len(name_list))
# 统计列表中某个元素出现的次数
print(name_list.count("jane"))

# clear方法，清空列表
name_list.clear()
print(name_list)