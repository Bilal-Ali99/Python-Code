# exceptions are error detected at the time of execution of program
# taking the example of division by 0 which is not possible or it is infinity
# in this example we will put 0 as second input
a = int(input("number 1:"))
b = int(input("number 2: "))
c = a/b
print(c)
# the output will show a traceback or error where division is not possible

# Now we will write the code for the execption handling
a = int(input("number 1:"))
b = int(input("number 2: "))
try:
    c = a/b
except ZeroDivisionError as e:
    c = None
    print("Zero Exception occured: ",e)
print(c)
# we could use anything in the place of ZeroDivisionError but it is by default used for division by zero

# for handling multiple exceptions 
# taking example that the number 2 input is a string 
a = int(input("number 1:"))
b = input("number 2: ")
try:
    c = a/b
except ZeroDivisionError as e:
    c = None
    print("Zero Exception occured: ",e)
except TypeError as f:
    c = None
    print("TypeError exception occured")
print(c)

