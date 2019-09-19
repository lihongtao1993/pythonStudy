# 定义字典1
personal_info = {"name": "xiaoming",
                 "age": 18,
                 "male": True,
                 "height": "180cm",
                 "weight": 68.3
                 }
# 定义字典1
personal_info2 = {"name": "xiaoming",
                 "male": "男人",
                 "height": "180cm",
                 }
# 遍历字典

for key in personal_info:
    print(key,"-",personal_info[key])

