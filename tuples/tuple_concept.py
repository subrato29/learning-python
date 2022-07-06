# Tuple: collection of elements on any python data type
# Tuple vs List
# 1) tuple => {}, list => []
# 2) tuple is immutable but list is mutable

name = ("Java", "DotNet", "Python", "CSharp")
marks = (100, 20, 30, 400)
employee_data = ("A", 60, 'm', 78.67, True)

print(employee_data)
print(employee_data[3])

print(employee_data[-1])
print(employee_data[-3])

print(name)
# del name
print(name)

# concatenation
t1 = (1, 2, 3)
t2 = (5, 9, 4)
print(t1 + t2)
print(t1 * 3)

print(employee_data[1 : 3])

print(60 in employee_data)
print(46 not  in employee_data)

print(len(employee_data))

numbers = (56, 3, 78, 42, 89)
print(max(numbers))
print(min(numbers))