"""
What is class?
Taking an example of a human being
there are common things a human has

1) Name
2) Gender 
3) Occupation

all of these things are must for every human being which makes it a property

same way there is a thing called method
method is like an act done by a human being for e.g

1) Sleep
2) talk
3) walk
4) eat

which bring us to a conclusion that class is a combination of propertise and methods or a blue print or template

Now what is object?
it is an instance of a class or the entity created according to the blue print
any two object of the same class can have similar propertise and methods
"""

# making a class in python
class Human:

# we are defining the propertise of a class 
# self here means the class it self or we can say to initialise the attributes of an object
    def __init__(self,n,o): 
        self.name = n
        self.occupation = o

    
# now we are defining the methods     
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "Actor":
            print(self.name,"is an Actor")

    def speaks(self):
        print(self.name,"says how are you")


# now creating the an instance

bilal = Human("Tom Cruise", "Actor")
bilal.do_work()
bilal.speaks()

Ali = Human("Ali","tennis player")
Ali.do_work()
Ali.speaks()