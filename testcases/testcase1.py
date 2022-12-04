print("start of testcase1")
print ("Hello there")

def hello():
    print ("hello from function")

hello()

myvar=10 #global variable
def myfunc():
    myvar=5 #local variable in function
    print(myvar)

print(myvar)  #printing global variable
myfunc()  #calling function

print("end of testcase1")
