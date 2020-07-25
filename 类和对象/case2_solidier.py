# 士兵突击演练

# 定义一个枪的类


class Gun:

    def __init__(self, name):
        self.name = name
        # 定义枪子弹的数量，子弹是人添加的，创建枪类的时候不需要给值
        self.count = 0

    def add_bullet(self, count):
        # 添加子弹
        self.count += count
        print("子弹装填完成，当前剩余子弹%d" % count)

    def shoot(self):
        # 发射前判断有没有子弹
        if self.count <= 0:
            print("没有子弹了，不能开枪")
            return
        else:
            print("突突突……")
            self.count -= 1
            print("完成一次射击，子弹剩余%d" % self.count)


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        # 士兵开枪
        # is用来判断两个变量引用的对象是不是同一个(内存地址是否相等）
        # ==用来判断两个变量的值是否相等，
        # 在python中针对None的比较，建议使用is
        if self.gun is None:
            print("%s没有枪,请用拳头" % self.name)
            return
        # 让士兵装填子弹
        self.gun.add_bullet(30)
        # 发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")
# ak47.add_bullet(0)
# ak47.fire()

xusanduo = Soldier("许三多", ak47)

xusanduo.fire()
