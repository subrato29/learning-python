# list is mutable
score = [10, 20, 78, 45, 90]
print(score)
print(score[0])
print(score[2])
# print(score[6])
print(score[-1])  # slicing feature: maintain negative index in reverse order starting from -1

print(score[:])  # return duplicate new/shallow copy

print(score + [1, 2, 3])
print(score + ['A', 'C'])

# append:
score.append(300)
print(score)

name = ['a', 'b', 'c', 'd', 'e']
print(len(name))
name[2 : 5] = ['C', 'D', 'E']
print(name)
name[2:5] = []
print(name)
name[:] = []
print(name)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
nested_list = [list1, list2]
print(nested_list)
print(nested_list[1])
print(nested_list[1][2])