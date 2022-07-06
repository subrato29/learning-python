# set - not order based unlike list or tuple
# stores different type of data
# performs different mathematical operation
# does not store duplicate elements
# how to define set: use {}

s1 = {100, "Tom", 45.89, True}
s2 = {3, 4, 1, 3, 8, 4}
print(s2)
print(s1)

# set() function
s3 = set("Python")
print(s3)

s4 = set([5, 8, 3, 6])
print(s4)

s5 = set((78, 54, 3, 34))
print(s5)

# while creating a set object, you can store numbers, strings, tuples
# list and dictionary objects are not allowed

set1 = {(10, 20), 30, 40}
print(set1)

# set2 = {[10, 20], 30, 40}
# print(set2)  # TypeError: unhashable type: 'list

# set operations
# union: |
p1 = {1, 2, 3, 4, 5}
p2 = {4, 5, 6, 7, 8}
print(p1 | p2)
print(p1.union(p2))
print(p2.union(p1))

# intersection: &
p3 = {1, 2, 3, 4, 5}
p4 = {4, 5, 6, 7, 8}
print(p3 & p4)
print(p3.intersection(p4))

# difference of sets: or difference()
p5 = {1, 2, 3, 4, 5}
p6 = {4, 5, 6, 7, 8}
print(p5 - p6)
print(p6 - p5)
print(p5.difference(p6))

# symmetric difference: ^
p7 = {1, 2, 3, 4, 5}
p8 = {4, 5, 6, 7, 8}
print(p7 ^ p8)
print(p8 ^ p7)
print(p7.symmetric_difference(p8))

# set- inbuilt method
# 1. add ()
s1 = {"A", "D", "C", "E"}
s1.add("G")
print(s1)

# 2. update ()
s1 = {"A", "D", "C", "E"}
s1.update(["H", "M"])
print(s1)

s1.update(("R", "N"))
print(s1)

# 3. clear ()
s2.clear()
print(s2)

# 4. copy ()
s1 = {"A", "D", "C", "E"}
copy_set = s1.copy();
print(copy_set)

# 5. discard
s1 = {"A", "D", "C", "E"}
s1.discard("C")
print(s1)

# remove
s1 = {"A", "D", "C", "E"}
s1.discard("C")
print(s1)