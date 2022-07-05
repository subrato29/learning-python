# multiple inheritance is possible in Python unlike Java
class Base1:
    def __init__(self):
        self.str1 = "Tom"
        print("Base2")


class Base2:
    def __init__(self):
        self.str2 = "Harry"
        print("Base2")


class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Child")

    def printString(self):
        print(self.str1, self.str2)


child = Child()
child.printString()
