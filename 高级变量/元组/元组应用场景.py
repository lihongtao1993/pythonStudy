# 1、格式化字符串后面的（） 本质上就是元组
info = ("小明", 12, 1.60)

print("%s的年龄是%d身高%.2f" % info)


# 2、列表类型与元组类型之间的转换

num_list = [1,2,3,4,12,22,14,1]
# 列表转成元组 使用 tuple() 方法
num_tuple = tuple(num_list)
print(type(num_tuple))

# 元组转成列表使用list()方法
num_list2 = list(num_tuple)
print(type(num_list2))


