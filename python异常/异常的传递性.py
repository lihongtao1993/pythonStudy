def demo1():
    nub = int(input("输入一个整数"))
    result = 8 / nub
    return result


def demo2():
    return demo1()


# 在主程序中捕获异常
try:
    print(demo2())
except Exception as result:
    print("异常错误%s" % result)
