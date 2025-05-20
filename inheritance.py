"""taking an example of a class vehicle as vehicle is known as a mode of transportation
now a car and motor cycle both are vehicle which are used for any transportation
both have their own propertise methods
we can say we have derived a subclass from main class vehicle
or we can say that both the class "car" and "motorcycle" are classes that inherit some propertise from the class "Vehicle"

Benefits of inheritance
1) code reuse -> we can use same code on other app as well
2) extensibility -> we can customize the code according to our need
3) readability -> it provides a proper structure of the code """

class Vehicle:
    def general_usage(self):
        print("used for transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.roof = True

    def specific_usage(self):
        print("use to commute to work")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am MotorCycle")
        self.wheels= 2
        self.root = False

    def specific_usage(self):
        print("used for Bike racing")

c = Car()
c.general_usage()
c.specific_usage()
print("\n")
m = MotorCycle()
m.general_usage()
m.specific_usage()
print("\n")
# we use two builtin methods which are isinstance and issubclass method
# it tell us if an object is an instance of a specific class

print(isinstance(c,Car))
print(issubclass(Car,Vehicle))


"""We can remove the general usage function call and we can call it directly by calling it in the child class for example 

class Vehicle:
    def general_usage(self):
        print("used for transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.roof = True

    def specific_usage(self):
        print("use to commute to work")
        self.general_usage()

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am MotorCycle")
        self.wheels= 2
        self.root = False

    def specific_usage(self):
        print("used for Bike racing")
        self.general_usage()

c = Car()
c.specific_usage()

print("\n")

m = MotorCycle()
m.specific_usage()


using this code we can simply call the specific_usage function and in that function we are also
calling the general_usage function as well
"""