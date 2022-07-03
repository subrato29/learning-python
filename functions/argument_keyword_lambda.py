def login(username, password):
    print(username, password)


login("test123", "pass123")
login(username="prod123", password="pass56")


# *arg
def getMarks(*arg):
    for i in arg:
        print(i)


getMarks(20, 10, 50, 30)
getMarks("B", "D", "A", 50, 87, "E")


# keyword args:
# **arg
def getStudentMarks(**arg):
    for key, value in arg.items():
        print("%s : %s" % (key, value))


getStudentMarks(A=10, B=78)
getStudentMarks(A="AA", B="BB")

# lambda function: A function without any name
cube = lambda x: x * x * x
print(cube(4))
