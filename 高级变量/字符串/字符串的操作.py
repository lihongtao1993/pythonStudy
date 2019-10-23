# 1。统计字符串的长度，使用len()函数

str_example = "hello world"
result_len = len(str_example)
print("示例字符串是:%s" % str_example)
print("字符串长度:%d" % result_len)

# 统计谋个小字符串出现的次数，使用count()方法
result_count = str_example.count("ll")
print('字符串"ll"出现的次数是:%d次' % result_count)

# 判断子字符串在大字符串中的位置使用index()方法
result_index = str_example.index("o")
print('字符串长度是:%d,"o"出现的第一个位置是:%d' % (result_len,result_index))

