class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍……" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 爱飞到天上去玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s快乐的玩耍……" % (self.name, dog.name))
        dog.game()

dog1 = XiaoTianDog("旺财")

xiaoming = Person("小明")

xiaoming.game_with_dog(dog1)

