# break跳出并终止循环
print("判断条件放在循环执行的语句前")
list1 = [1, 2, 3, 4, 5, 6, 7]
for i in list1:
    if i == 3:
        break
    print(i)

print("-------------------------------")
print("判断条件放在循环执行的语句后")
for i in list1:
    print(i)
    if i == 3:
        break


