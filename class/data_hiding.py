class Employee:
    # hidden data member or private member of employee class
    __salary = 1000


emp = Employee()
# print(emp.__salary) - this is NOT the right way to access private variable

# accessing private hidden variable
print(emp._Employee__salary)
