try:
    # 不能确定是不是能正常执行的代码
    nub = int(input("请输入一个整数："))
    result = 8 / nub
except ZeroDivisionError:
    # 针对错误做异常处理 ValueError
    print("不能为0")

# 可以几个错误类型以前判断
except (ValueError, ZeroDivisionError):
    print("请输入正确的整数")

print("*" * 50)
