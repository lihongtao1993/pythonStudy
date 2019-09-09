# 联系循环嵌套，打印五行星星，一次递增

i = 1

while i <= 5:#外层循环，输出五行
    j = 5
    while j >= i:
        print("*",end="")
        j -= 1
    print("")
    i += 1
