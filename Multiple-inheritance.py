# Multiple Inheritance is used when there are 2 different class and their propertise are used in 
# a child class for calling a specific function

class Father():
    def gardening(self):
        print("I do gardening")

class Mother():
    def cooking(self):
        print("I do Cooking")

class Child(Father,Mother):
    def sport(self):
        print("I am child one enjoy sports")

class Uncle():
    def skills(self):
        print("I do programing and API stuff")

class Aunty():
    def skills(self):
        print("I do cloud engineering")

class Child_two():
    def learning(self):
        print("I am child two learning programing")
        Uncle.skills(self)
        Aunty.skills(self)
        

c = Child()
c.sport()
c.gardening()
c.cooking()
print("\n\n")

c_2 = Child_two()
c_2.learning()
