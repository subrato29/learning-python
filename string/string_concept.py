s = "hello world"
print(s[0])
print(s[3:7])
print(s[2:])
print(s * 3)
print(s + " python")

print("test " * 5)

print("hello" in s)
print("ff" not in s)

print("My name is %s and my age is %d" % ("David", 32))  # formatting operator

s1 = '''hello
I am 
trying 
to learn Python'''  # making paragraph
print(s1)

s2 = "hello world hello I am learning hello"
print(s2)
print(s2.capitalize())

print(s2.count("hello"))

print(s2.find("world"))
print(s2.find("ggg"))

print(len(s2))
print(s2.lower())

s2 = "  hello    "
print(s2.lstrip())
print(s2.rstrip())

s2 = "zoo"
print(max(s2))
print(min(s2))

s2 = "hello world"
print(s2.replace("hello", "hi"))
print(s2.split(" "))
print(s2.upper())