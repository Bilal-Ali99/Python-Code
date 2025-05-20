class Accident(Exception): # creating a user defined exception where (Exception) is a predefined method in python
    def __init__(self,msg):
        self.msg = msg
    def other_route(self):
        print("Accident ahead take alternative route",self.msg)



try:
    raise Accident('Crash of 2 cars')
except Accident as e:
    e.other_route()

# exception is basicaly an object/instance of a class

"""Finally Statement is used because when ever we are writing the code and in the TRY section of code there are 1000 line of code where we dont know how many exception are happening therefore we use the finally key word for closing the file because if we dont use it and an exception occurs the execution might stop but the file which we might have accessed would still be using the resources. """
# writing a code for finally key word

def process_file():
    try:
        f = open("d:\\Notebook\\python\\calculation.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

process_file()