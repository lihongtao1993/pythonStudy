import tool1
# 为了方便，可以使用as给被导入的模块起个别名
import 测试被导入的模块 as Tool2


print(Tool2.demo(4, 6))
print(tool1.demo(4, 6))
wangcai = tool1.Dog("旺财")

print(wangcai)
print(wangcai.name)
print(tool1.tool_name)

