
x=10
y=10

if x>y:
    print(x,"is greater")
elif y>x:
    print(y,"is greater")
else:
    print("both are equal")

for x in range(1,5):
    print(x)

for x in ["apple","orange","banana"]:
    print(x)
print("===================")
for x in "Hello":
    if x=="l":
        break
    print(x)
print("===================")
for x in "Hello":
    if x=="l":
        continue
    print(x)

print("===================")
x=5
while x<=8:
    print(x)
    x += 1  # x=x+1

print("===================")
x=5
while x<=8:
    if x==7:
        break
    print(x)
    x += 1  # x=x+1
print("===================")
x=5
while x<=8:
    x += 1  # x=x+1
    if x==7:
        continue
    print(x)

