# object is the super class of all the classes like java
class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    def isEmployee(self):
        return True


# Test Person
emp = Person("Subrato")
print(emp.name)
print(emp.getName(), emp.isEmployee())

emp1 = Employee("David")
print(emp1.name)
print(emp1.getName(), emp1.isEmployee())  # overridden isEmployee() method is called
