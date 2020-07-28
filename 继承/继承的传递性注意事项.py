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

    def bark(self):
        print("汪汪汪……")

class Keji(Dog):
    def shout(self):
        print("我是柯基犬")

class Cat(Animal):
    def catch(self):
        print("猫可以抓老鼠！！！")


Kj = Keji()

Kj.shout()
Kj.run()
Kj.eat()

tom = Cat()

tom.catch()
tom.sleep()

# cat类不可以调用Keji类的方法，
# tom.shout()、
