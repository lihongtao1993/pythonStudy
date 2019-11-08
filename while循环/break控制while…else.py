i = 1
result = 0
while i <= 5:
    if i == 4:
        break
    print(f"{i}")
    result = result + i
    i += 1
else:
    print("---------------")
    print(f"和是{result}")
