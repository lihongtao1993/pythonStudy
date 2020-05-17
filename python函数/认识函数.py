#
"""
1、定义函数
def 函数名(参数)
    代码1
    代码2
2、调用函数
函数名(参数)
python中，函数必须先定义在使用
"""

def calculate(a,b):
    '''说明文档，计算两个数的和的函数'''
    return a+b

# result = calculate(5,6)
# print(result)
help(calculate)



def ca(a,b):
    S = int(input("请选择运运算类型1(+),2(-),3(*),4(/) :"))
    if S==1:
        print(a+b)
    elif S == 2:
        print(a-b)
    elif S == 3:
        print(a*b)
    elif S == 4:
        print(a/b)
    else:
        print("输入正确的运算符")