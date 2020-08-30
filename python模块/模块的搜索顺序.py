# 注意开发的文件不能和系统模块文件重名
# 每一个开发的文件都应该被导入
import random
print(random.__file__)
