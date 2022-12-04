
def hello():
    print("Hello world")
hello()
print("=================")
def sum():
    x=10
    y=20
    c=x+y
    return c
print("Sum is",sum())

print("=================")
def sum(x,y):
    c=x+y
    return c
print("Sum is",sum(3,4))
print("=================")
# def sum(x,y):
#     c=x+y
#     return c
# x=input("Enter num1:")
# y=input("Enter num2:")
# print("Sum is",sum(int(x),int(y)))
print("=================")

def helloUser(name="John"):
    print("hello",name)

helloUser("Rita")
helloUser("Troy")
helloUser()

print("=================")
def helloPerson(**name):
    print("Hello",name["fname"],name["lname"])
helloPerson(fname="Tina",lname="Gill")

print("=====functionality not yet implemented============")
def notImplemented():
    pass
