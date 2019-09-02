# 在循环语句中，可以通过break跳出循环。
i = 0
while i <= 10:
    # break 某一特定条件满足时，退出循环，不再继续执行循环代码
    if(i == 3): # break条件
        break
    print(i)
    i += 1
print("over")

