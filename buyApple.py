#定义单价变量，单位：元/kg
price = input("输入苹果单价：")
#定义购物重量变量，单位:kg
weight = input("输入购买重量:")
# 计算总金额，计算公式：总金额=单价*重量
money = int(price) * int(weight)
print("您此次购买需支付:",money,"元")
