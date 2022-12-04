class Car:
    x=10
    def carFunc(self):
        print("I am inside Car class")

car1=Car()
print(car1.x)
car1.carFunc()

print("=============")
class Car:
    x=10
    def __init__(self,name, model, topspeed):
        self.name=name
        self.model=model
        self.topspeed=topspeed
    def carFunc(self):
        print("Name of the car is:",self.name)

car1=Car("BMV",2020,250)
print(car1.name, car1.model, car1.topspeed)
print(car1.x)
car1.carFunc()