i = 1
result = 0
while i <= 5:
    if i == 4:
        i += 1   #continue退出循环之前要把计数器+1，不然会死循环
        continue
    print(f"{i}")
    result = result + i
    i += 1
else:
    print("---------------")
    print(f"和是{result}")
