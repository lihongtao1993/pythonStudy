#定义性别
ticket = True
age = 19
# 判断是否为男性
if ticket:
    print("初审通过")

    if age > 20:
        print("你不能进去，因为你已经%d了，年龄太大！" % age)
    else:
        print("年龄为%d请进"%age)
else:
    print("你没票")