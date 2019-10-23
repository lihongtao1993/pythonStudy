#
str1 = "hello world"
# 1、判断是否以指定字符串开始
print(str1.startswith("hello"))
# 区分大小写
print(str1.startswith("Hello"))

# 2、判断是否以指定字符串结束
print(str1.endswith("ld"))

# 判断是否包含指定字符串
print(str1.find("or"))
print(str1.index("or"))
# rfind和index的区别，若果字符串不包含指定的字符串，index方法会报错，find不会报错，返回-1
print("字符串不存在时，find()会返回：%d" % str1.find("ol"))

# 替换字符串，replace()方法
example_str = str1.replace("world","python")
print("替换后的字符串：%s" % example_str)





