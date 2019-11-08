"""
while 条件:
    执行代码1
else:
    循环正常结束后执行代码
"""
i = 1
result = 0
while i <= 5:
    print(f"{i}")
    result = result + i
    i += 1
else:
    print("---------------")
    print(f"和是{result}")
