class Superclass1:
    def __init__(self):
        self.Fname = "test"

    def FatherDuty(self):
        print("%s世上只有爸爸好" % self.Fname)


class Superclass2:

    def __init__(self):
        self.Mname = "demo"

    def MomDuty(self):
        print("%s世上只有妈妈好" % self.Mname)


# 多继承
class son(Superclass1, Superclass2):
    def __init__(self):
        Superclass1.__init__(self)
        Superclass2.__init__(self)
        self.name = "%s+%s" % (self.Fname, self.Mname)

Mike = son()
#
Mike.FatherDuty()
Mike.MomDuty()
# Mike.name = "hhh"
print(Mike.Fname)
print(Mike.name)
