# 当父类的方法不能满足子类的需求时，比如柯基狗的叫声不是汪汪汪，而是哈哈哈
# 实现的方法，在子类中定义一个同名的方法
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

# 比如柯基狗不仅可以叫唤，还可以卖萌打滚。。。。


class Keji(Dog):
    def shout(self):
        print("我是柯基犬")

    def bark(self):
        # 1、针对子类特有需求，编写代码
        print("柯基狗小短腿，爱卖萌")
        # 2、使用super().在需要的位置调用原本在父类中封装的方法
        super().bark()
        super().sleep()
        # 3、其他代码
        print("哈哈哈……，柯基叫的不一样")


Kj = Keji()

Kj.shout()
Kj.bark()
