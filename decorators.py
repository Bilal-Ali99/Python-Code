# what problem does decorators resolve?
# decorator allow us to wrap our function into another function 
# sometimes we have a need of measuring the performance of a function
# by performance we mean the time taken for completion of function
# for time measuring we import time library

import time


def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print("square time calculation took" " "+ str((end-start)*1000) +" " "mili second")
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("cube time calculation took " " "  + str((end-start)*1000) +" " " mili second")
    return result

array = range(1,100000)
squred = calc_square(array)
cubed = calc_cube(array)


# considering this code we have to measure the performance of many functions by measure the time taken for execution
# at this point we use decorator which wrap the function into another function 
# For example 


# defining wrapper function which is taking func as an arguement  
def time_it(func): 
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+ " ""took "+ str((end-start)*1000)+" ""time in mil sec")
        return result
    return wrapper


# we call 
@time_it # this is the decorate function called 
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
squred = calc_square(array)
cubed = calc_cube(array)



