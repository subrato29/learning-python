class Base(object):
    def __init__(self, x):
        self.x = x


class Child(Base):
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printWork(self):
        print(Base.x, self.y)


# Test code
child = Child(10, 20)
child.printWork()

