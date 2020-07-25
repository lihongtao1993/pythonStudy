def run():
    return "跑步减肥1公斤"


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s体重%.2f公斤" % (self.name, self.weight)

    def run(self, distance):
        if self.weight > 1:
            loseWeight = distance * 0.05
            self.weight = self.weight - loseWeight
            print("%s跑步%.2f公里，减重%.2f公斤" % (self.name, distance, loseWeight))
            print("%s现在体重%.2f公斤" % (self.name, self.weight))
        else:
            print("体重错误！！！！")

    def eat(self):
        self.weight += 0.5
        print("%s体重%.2f公斤" % (self.name, self.weight))


mike = Person("Mike", 1)

print(mike)

mike.run(10)
