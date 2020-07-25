# 在python中设置私有属性和方法是在前面加上两个__
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def intro(self):
        print("%s年龄是%d" % (self.name, self.__age))

    def __secret(self):
        print("%s年龄是%d" %(self.name, self.__age))


xiaofang = Women("小芳", 18)

print(xiaofang.name)
xiaofang.intro()

