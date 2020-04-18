# 使用return返回，return返回并结束函数
def test():
    return 1

result = test()
print(result)

# 多个返回值时，return的返回值用逗号隔开。返回的是元组数据类型

def testb():
    return 1, 2


B = testb()
print(B)
print(type(B))

# return返回元组、列表、字典

def TEST():
    return (10, 23, 30), [1, 2, 3],{'name': 'tom','age': 26}


A = TEST()

print(A)


