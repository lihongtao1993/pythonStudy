dict1 = {"name": "Tom","age": 18,"gender": "男"}

# 第一种查找方法：直接用字典的key值
print(dict1["age"])


# 第二种方法：使用函数
# 1、get()函数 方法 ：字典序列.get(key,默认值)
print(dict1.get("gender"))  #如果key存在，则返回key的value值
print(dict1.get("gende"))  #如果key不存在，返回None
print(dict1.get("names","mike"))  #如果key不存在，但是有默认值，则返回默认值
print(dict1.get("name","mike"))   #如果key存在，且也有默认值，则返回key的value值
print("____________________________________________",end="\n")
print()
#2、keys函数 方法：字典序列.keys()
print(dict1.keys()) #查找字典中所有的key值，返回一个可迭代的对象

#3、values()函数，方法：字典序列.values()
print(dict1.values())  #查找字典中所有的value值，返回一个可迭代的对象

#4、 items()函数
print(dict1.items())  #查找字典中所有的键值对，返回一个可迭代的对象。对象里面的数据是元组，元组数据1是key,2是value

