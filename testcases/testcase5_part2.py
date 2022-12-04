import testcase1
print("hello from testcase5_part2")

str1="""This is a multi line
string 1"""
str2='''This is a multi
line string 2'''
print(str1)
print(str2)

str3="Hello"
print(str3[0])
print(str3[0:4])
print(len(str3))

print("For loop:")
for x in "Grape":
    print(x)

print("hell" in "hello")
print("hell" not in "hello")

x=99999999
print("Integer:",x)

print("Float numbers")
x=-5.67
print(x)
x=-5.2e2
print(x)

print("Complex numbers")
x=2-1j
print(x)
x=-10j
print(x)
x=10j
print(x)

import random
print(random.random())
print(random.randrange(1,25))

print(10>2)
print(bool("Hello"))
print(bool(0))
print("Hello" in "hello World")