class Car:
    # class variable
    wheels = 4

    # Constructor of this class
    def __init__(self):
        self.price = None

    # Constructor overloading is NOT possible in Python unlike Java
    def __init__(self, color):
        print("color is " + color)
        self.color = color

    def test(self):
        print("This is a test method")

    # variable declared inside method or constructor is called instance variable
    def set_price(self, price):
        self.price = price

    def get_price(self):
        print("Default constructor")
        return self.price


# how to create object of the class
c1 = Car("Black")
print(c1.wheels)
print(Car.wheels)
c1.test()
c1.set_price(200)
print(c1.get_price())

c2 = Car("Red")
c1.set_price(1000)
print(c1.get_price())