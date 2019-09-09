import function.test

function.test.table()
# 输出99乘法表
print()
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # n = i*j
        if i == 3 or i == 4:
            if j == 3:
                print(" ",end="")
        print("%d*%d=%d " % (j,i,(i*j)),end="")
        j += 1
    i += 1
    print()
