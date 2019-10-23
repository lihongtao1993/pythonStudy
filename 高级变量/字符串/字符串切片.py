# 定义一个字符串
num_str = "0123456789"


# 1、截取2-5之间的字符串
print(num_str[2:6])

# 2、截取2-末尾的字符串
print(num_str[2:])

# 截取开始-5之间的字符
print(num_str[:6])

# 截取完整的字符串
print(num_str[:])

# 从1开始，隔一个取一个
print(num_str[1::2])

# 倒叙切，切取最后两个自字符串
print(num_str[-2])

# 字符串逆序

print(num_str[::-1])