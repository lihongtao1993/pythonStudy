class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "%s的颜色是%s" % (self.name, self.color)


tom = Cat("Tom", "black")
jacky = Cat("Jacky", "blue")

print(tom, jacky)


