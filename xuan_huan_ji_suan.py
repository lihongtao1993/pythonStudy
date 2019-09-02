'''
计算0~100直接整数的和
result = 0
i = 0
while i <= 100:
    result += i
    i += 1

print("0~100之间整数的和是:%d" % result)

'''

# """计算0~100直接偶数的和"""
# 定义计算结果
result = 0
# 定义循环计数器变量
i = 0

while i<= 100:
    # 判断计算条件—--偶数
    if(i % 2 == 0):
        # 循环计算，结果加计算器变量
        result += i
    i += 1
print(result)