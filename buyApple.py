price = input("输入苹果单价:")
# 计算总金额，计算公式：总金额=单价*重量

#定义购物重量变量，单位:kg
weight = input("输入购买重量:")
#定义单价变量，单位：元/kg

money = float(price) * float(weight)

print("你买了%s斤苹果，单价是%s元，共计%.2f元/斤" % (weight, price, money))
# print("您此次购买需支付:%d元" %money)

#输出百分数

scale = 0.25

print("输出的比例是：%.2f%%" % (scale*100))

num = 2
print("学号是：%05d" % num)

