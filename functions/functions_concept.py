def func(lang):
    print("I am learning functions in " + lang)


func("Python")


# Default/Optional parameter
def country(name='India'):
    print("Name of the country " + name)


country("Australia")
country()  # print India


# function with return statement
def total(a, b):
    return a + b


print(total(2, 4))


def login(username, password):
    print("Username is %s and Password is %s" % (username, password))


login("test123", "pass123")