# if statement is used when there are multiple conditions used when an input is taken from a user
# for e.g taking an input from the user and then deciding whether it is an odd or even number

num = int(input("Enter A Number:")) #We use input() to read a number and int() to convert it to an integer, as input returns a string.

if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")



