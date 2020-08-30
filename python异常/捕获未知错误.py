try:
    # 不能确定是不是能正常执行的代码
    nub = int(input("请输入一个整数："))
    result = 8 / nub
except ZeroDivisionError:
    # 针对错误做异常处理 ValueError
    print("不能为0")
# 不能预判所有的错误类型，通过下面的语法捕获未知错误
except Exception as result:
    print("错误类型 %s" % result)


print("*" * 50)
