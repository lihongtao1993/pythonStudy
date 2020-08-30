# 异常的完整语法


try:
    # 尝试执行的代码
    nub = int(input("请输入一个整数："))
    result = 8 / nub
except ZeroDivisionError:
    # 错误类型1
    print("数字不能为0")
except ValueError:
    # 错误类型2
    print("请输入正确的整数")
except Exception as result:
    # 捕获未知错误
    print("错误异常： %s" % result)

else:
    # 没有异常时，执行的语法
    print("尝试成功，输入的数字是：%d，结果为：%.2f " % (nub, result))
finally:
    # 无论是否有异常，都会执行的代码
    nub = int(input("重新输入："))