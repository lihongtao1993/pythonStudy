class Parent:
    def __init__(self):
        self.__age = 40
        self.name = "爸爸"

    def __prive(self):
        print("我是你%s，但是不能告诉别人" % self.name)

    def indirect(self):
        print("父类私有属性的年龄是%s" % self.__age)
        self.__prive()

class Children(Parent):
    def intro(self):
        print("准备访问父类的私有属性")
        # 不能直接访问父类的私有属性或方法
        # print(self.__age)
        # self.__prive
        # 间接访问，可以在父类的公有方法中方位父类的私有方法，简接的访问父类私有属性和方法
        self.indirect()

Dad = Parent()
son = Children()

son.intro()

# Dad._Parent__prive()