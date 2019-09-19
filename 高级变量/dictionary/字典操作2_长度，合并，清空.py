
# 定义字典1
personal_info = {"name": "xiaoming",
                 "age": 18,
                 "male": True,
                 "height": "180cm",
                 "weight": 68.3
                 }
# 计算长度
result = len(personal_info)

print(result)

# 定义字典2
personal_info2 = {"like":" movies",
                  "study": 5,
                  "age": 17
                  }

# 合并字典
print("合并前的字典：%s" % personal_info)

personal_info.update(personal_info2)

print("被合并的字典：%s" % personal_info2)

print("合并后的字典：%s" % personal_info)

# 清空字典
personal_info2.clear()
print("清空后的字典：%s" % personal_info2)

