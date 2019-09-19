personal_info = {"name": "xiaoming",
                 "age": 18,
                 "male": True,
                 "height": "180cm",
                 "weight": 68.3
                 }
# 取字典的值，使用字典名[key]
name = personal_info["name"]
print(name)

# 新增，如果没有key就会新增
personal_info["address"] = "上海市南京东路1号"
print(personal_info["address"])

# 修改，如果key存在，就是修改
personal_info["age"] = 17
print(personal_info["age"])

# 删除字典的值
personal_info.pop("weight")
print(personal_info)