class Base(object):
    pass


class Child(Base):
    pass


# Test code
print(issubclass(Child, Base))
print(issubclass(Base, object))

child = Child()
base = Base()

print(isinstance(base, Base))
print(isinstance(base, Child))
print(isinstance(child, Child))
