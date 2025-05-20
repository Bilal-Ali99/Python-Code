# function made code modulars
# using function for list calculation
""" in this code we have used function to calculate the values in the list a and b"""
list_a = [2000,1234,4543,3453]
list_b = [2131,5435,1231,3243]

def calculation(value):
    """ this variable named as total will be only available in this function and cannot be called outside this function"""
    total = 0
    for values in value:
        total = total + values
    print("list total is: ",total)
    return total

list_a_total = calculation(list_a)
list_b_total = calculation(list_b)

""" now making a second funtion to take the sum of two integers by taking 2 arguements in the function"""

def sum(x,y):
    total = x + y
    return total
a = sum(5,7)
print("sum is:",a)
