class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    #
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("吃")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")
    def bark(self):
        print("汪汪汪……")


wangcai = Animal()
wangcai.sleep()
xiaohuang = Dog()
xiaohuang.eat()
xiaohuang.run()
xiaohuang.drink()
xiaohuang.sleep()
xiaohuang.bark()


