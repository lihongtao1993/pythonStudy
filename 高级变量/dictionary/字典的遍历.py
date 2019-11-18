dict1 = {"name": "Tom","age": 18,"gender": "男"}
# 1、遍历字典的key
for key in dict1.keys():
    print(key)

print()

# 2、遍历字典的value
for value in dict1.values():
    print(value)
print()

#遍历字典元素
for item in dict1.items():
    print(item)
print()

# 4、遍历键值对
for key, value in dict1.items():
    print(f"{key}:{value}")